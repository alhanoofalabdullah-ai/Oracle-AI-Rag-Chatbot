class SalesAnalytics:

    MONTHLY_REVENUE = """
    SELECT

        d.year_number,

        d.month_number,

        d.month_name,

        SUM(f.net_amount)
            AS revenue

    FROM fact_sales f

    JOIN dim_date d

        ON d.date_key =
           f.date_key

    GROUP BY

        d.year_number,

        d.month_number,

        d.month_name

    ORDER BY

        d.year_number,

        d.month_number
    """

    TOP_PRODUCTS = """
    SELECT

        p.product_name,

        p.category,

        SUM(f.quantity)
            AS units_sold,

        SUM(f.net_amount)
            AS revenue

    FROM fact_sales f

    JOIN dim_product p

        ON p.product_key =
           f.product_key

    GROUP BY

        p.product_name,

        p.category

    ORDER BY revenue DESC

    FETCH FIRST 10 ROWS ONLY
    """

    def __init__(
        self,
        repository,
    ):

        self.repository = repository

    def monthly_revenue(self):

        return self.repository.query(
            self.MONTHLY_REVENUE
        )

    def top_products(self):

        return self.repository.query(
            self.TOP_PRODUCTS
        )
