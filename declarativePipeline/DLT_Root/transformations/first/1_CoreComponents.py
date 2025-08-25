# import dlt

# # Creating a Streaming Table
# @dlt.table(
#     name="stream_table_1"
# )
# def stream_table_1():
#   df = spark.readStream.table("dlt_pipelines.source.order_1")
#   return df



# # To create a Batch Table,
# # Creating a Materialized View
# @dlt.table(
#     name="mat_view_1"
# )
# def mat_view_1():
#   df = spark.read.table("dlt_pipelines.source.order_1")
#   return df



# # Creating Batch View
# @dlt.view(
#     name="batch_view_1"
# )
# def batch_view_1():
#   df = spark.read.table("dlt_pipelines.source.order_1")
#   return df


# # Create Streaming View
# @dlt.view(
#     name = "stream_view_1"
# )
# def stream_view_1():
#     df = spark.readStream.table("dlt_pipelines.source.order_1")
#     return df




