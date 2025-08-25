import dlt

# Customers Expections
customer_rules = {
    "rule_1":"customer_id IS NOT NULL",
    "rule_2":"customer_name IS NOT NULL"
}


# Ingesting Customers
@dlt.table(
    name="customers_stg"
)
@dlt.expect_all_or_drop(customer_rules)
def products_stg():
    df = spark.readStream.table("dlt_pipelines.source.customers")
    return df