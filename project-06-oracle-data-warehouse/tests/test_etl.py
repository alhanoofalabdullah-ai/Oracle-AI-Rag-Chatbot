def test_gross_amount():

    quantity = 5

    unit_price = 100

    gross = (
        quantity *
        unit_price
    )

    assert gross == 500
