# import dlt
# from pyspark.sql.functions import *

# """Creating End-to-End basic pipeline"""

# # Staging Area
# @dlt.table(
#     name = "staging_orders"
# )
# def staging_orders():
#     df = spark.readStream.table("dlt_pipelines.source.order_1")
#     return df


# # Creating Transformed Area
# @dlt.view(
#     name = "transformed_orders"
# )
# def transformed_orders():
#     df = spark.readStream.table("staging_orders")
#     df = df.withColumn("order_status",lower(col("order_status")))
#     return df


# # Creating Aggregated Area
# @dlt.table(
#     name = "aggregated_orders"
# )
# def aggregated_orders():
#     df = spark.readStream.table("transformed_orders")
#     df = df.groupBy("order_status").count()
#     return df


