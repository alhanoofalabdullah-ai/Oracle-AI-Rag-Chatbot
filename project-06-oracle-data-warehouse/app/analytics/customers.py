class CustomerAnalytics:

    TOP_CUSTOMERS = """

    SELECT

        c.customer_name,

        c.customer_segment,

        SUM(f.net_amount)
            AS revenue,

        COUNT(
            DISTINCT f.order_id
        ) AS orders

    FROM fact_sales f

    JOIN dim_customer c

        ON c.customer_key =
           f.customer_key

    GROUP BY

        c.customer_name,

        c.customer_segment

    ORDER BY revenue DESC

    FETCH FIRST 10 ROWS ONLY

    """

    def __init__(
        self,
        repository,
    ):

        self.repository = repository

    def top_customers(self):

        return self.repository.query(
            self.TOP_CUSTOMERS
        )
