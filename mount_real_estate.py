# Databricks notebook source
# MAGIC %python
# MAGIC
# MAGIC try:
# MAGIC     # Check if the mount point already exists
# MAGIC     if any(mount.mountPoint == '/mnt/real_estate_short_sample_5k' for mount in dbutils.fs.mounts()):
# MAGIC         # Unmount the existing mount point
# MAGIC         dbutils.fs.unmount('/mnt/real_estate_short_sample_5k')
# MAGIC         print("Unmount successful")
# MAGIC     else:
# MAGIC         # Mount the storage location
# MAGIC         dbutils.fs.mount(
# MAGIC             source="wasbs://testfiles@dadatabrickstorage.blob.core.windows.net",
# MAGIC             mount_point="/mnt/real_estate_short_sample_5k",
# MAGIC             extra_configs={
# MAGIC                 "fs.azure.account.key.dadatabrickstorage.blob.core.windows.net": "6pWizCt8/w9K9S+Sc9z/LNGUo/YeRy7rpUJFvBB3vv/D4W1HLyelW/+bTnuk5rGPQFzX2PFcpbUT+AStLbebqw=="
# MAGIC             }
# MAGIC         )
# MAGIC         print("Mount successful")
# MAGIC except Exception as e:
# MAGIC     # Handle any errors that occur during mount
# MAGIC     if isinstance(e, FileNotFoundError):
# MAGIC         print("File or directory not found:", str(e))
# MAGIC     else:
# MAGIC         print("Error occurred during mount:", str(e))
# MAGIC finally:
# MAGIC     # Code to run regardless of whether an exception occurred or not
# MAGIC     print("Mount process completed")
