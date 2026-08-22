# Dimensional Model

The project uses a Star Schema.

## Fact

FACT_SALES

Measures:

- Quantity
- Unit Price
- Discount
- Gross Amount
- Net Amount

## Dimensions

### DIM_CUSTOMER

Customer analytical attributes.

### DIM_PRODUCT

Product analytical attributes.

### DIM_DATE

Calendar-based analytical attributes.

### DIM_LOCATION

Geographical analytical attributes.

---

## Star Schema

                    DIM_DATE
                       |
                       |
DIM_CUSTOMER ---- FACT_SALES ---- DIM_PRODUCT
                       |
                       |
                 DIM_LOCATION
