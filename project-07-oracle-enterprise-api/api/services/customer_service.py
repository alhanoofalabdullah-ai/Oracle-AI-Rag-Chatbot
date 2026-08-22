class CustomerService:

    def __init__(self, repository):

        self.repository = repository


    def list_customers(self):

        sql = """

        SELECT

            customer_id,

            customer_code,

            customer_name,

            email,

            phone,

            status,

            created_at

        FROM api_customers

        ORDER BY created_at DESC

        """

        return self.repository.fetch_all(
            sql
        )


    def get_customer(
        self,
        customer_id
    ):

        sql = """

        SELECT

            customer_id,

            customer_code,

            customer_name,

            email,

            phone,

            status,

            created_at

        FROM api_customers

        WHERE customer_id = :customer_id

        """

        result = self.repository.fetch_all(

            sql,

            {
                "customer_id":
                    customer_id
            }
        )

        return result[0] if result else None
