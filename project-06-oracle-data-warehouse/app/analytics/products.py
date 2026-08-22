class ProductAnalytics:

    CATEGORY_REVENUE = """

    SELECT

        p.category,

        SUM(f.net_amount)
            AS revenue,

        SUM(f.quantity)
            AS units

    FROM fact_sales f

    JOIN dim_product p

        ON p.product_key =
           f.product_key

    GROUP BY

        p.category

    ORDER BY revenue DESC

    """

    def __init__(
        self,
        repository,
    ):

        self.repository = repository

    def category_revenue(self):

        return self.repository.query(
            self.CATEGORY_REVENUE
        )
