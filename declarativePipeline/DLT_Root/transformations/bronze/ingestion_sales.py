import dlt

# Sales Expections
sales_rules = {
    "rule_1": "sales_id IS NOT NULL"
}


# Creating Empty Streaming Table
dlt.create_streaming_table(
    name="sales_stg",
    expect_all_or_drop=sales_rules
)


# Creating East Sales Flow --> creating flow says that i don't want to create any table or view, just attach this flow to the target
@dlt.append_flow(target="sales_stg")
def east_sales():
    df = spark.readStream.table("dlt_pipelines.source.sales_east")
    return df

# Creating West Sales Flow
@dlt.append_flow(target="sales_stg")
def west_sales():
    df = spark.readStream.table("dlt_pipelines.source.sales_west")
    return df