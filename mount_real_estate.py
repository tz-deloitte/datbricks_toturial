# Databricks notebook source
try:
    # Check if the mount point already exists
    if any(mount.mountPoint == '/mnt/real_estate_short_sample_5k' for mount in dbutils.fs.mounts()):
        # Unmount the existing mount point
        dbutils.fs.unmount('/mnt/real_estate_short_sample_5k')
    else:
        # Mount the storage location
        dbutils.fs.mount(
            source="wasbs://testfiles@dadatabrickstorage.blob.core.windows.net",
            mount_point="/mnt/real_estate_short_sample_5k",
            extra_configs={
                "fs.azure.account.key.dadatabrickstorage.blob.core.windows.net": "6pWizCt8/w9K9S+Sc9z/LNGUo/YeRy7rpUJFvBB3vv/D4W1HLyelW/+bTnuk5rGPQFzX2PFcpbUT+AStLbebqw=="
            }
        )
        print("Mount successful")
except Exception as e:
    # Handle any errors that occur during mount
    print("Error occurred during mount:", str(e))

# COMMAND ----------

try:
    # Read the file using Python
    file_path = "/mnt/real_estate_short_sample_5k/real_estate_short_sample_5k.csv"
    df = spark.read.format("csv").option("header", "true").load(file_path)

    # Display a limited number of rows in the DataFrame
    display(df.limit(10))  # Displaying only the first 10 rows
except Exception as e:
    # Handle any errors that occur during file reading
    print("Error occurred during file reading:", str(e))
