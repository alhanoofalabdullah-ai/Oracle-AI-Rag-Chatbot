import streamlit as st

from app.database.connection import (
    OracleConnection,
)

from app.database.repository import (
    Repository,
)

from app.analytics.sales import (
    SalesAnalytics,
)

from app.analytics.customers import (
    CustomerAnalytics,
)

from app.analytics.products import (
    ProductAnalytics,
)


@st.cache_resource
def get_repository():

    connection = OracleConnection()

    return Repository(connection)


def run():

    st.set_page_config(

        page_title=
        "Oracle Data Warehouse",

        page_icon="📊",

        layout="wide",
    )

    st.title(
        "📊 Oracle Data Warehouse Analytics"
    )

    st.caption(
        "Enterprise Data Warehouse • ETL • Analytics"
    )

    repository = get_repository()

    sales = SalesAnalytics(
        repository
    )

    customers = CustomerAnalytics(
        repository
    )

    products = ProductAnalytics(
        repository
    )

    # =====================================================
    # MONTHLY REVENUE
    # =====================================================

    st.header(
        "Revenue Trend"
    )

    monthly = (
        sales.monthly_revenue()
    )

    if not monthly.empty:

        st.line_chart(
            monthly,
            x="MONTH_NAME",
            y="REVENUE",
        )

    # =====================================================
    # TOP PRODUCTS
    # =====================================================

    st.header(
        "Top Products"
    )

    top_products = (
        sales.top_products()
    )

    st.dataframe(
        top_products,
        use_container_width=True,
    )

    # =====================================================
    # TOP CUSTOMERS
    # =====================================================

    st.header(
        "Top Customers"
    )

    top_customers = (
        customers.top_customers()
    )

    st.dataframe(
        top_customers,
        use_container_width=True,
    )

    # =====================================================
    # CATEGORY
    # =====================================================

    st.header(
        "Revenue by Category"
    )

    categories = (
        products.category_revenue()
    )

    if not categories.empty:

        st.bar_chart(
            categories,
            x="CATEGORY",
            y="REVENUE",
        )
