%python

try:
    # Check if the mount point already exists
    if any(mount.mountPoint == '/mnt/real_estate_short_sample_5k' for mount in dbutils.fs.mounts()):
        # Unmount the existing mount point
        dbutils.fs.unmount('/mnt/real_estate_short_sample_5k')
        print("Unmount successful")
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
    if isinstance(e, FileNotFoundError):
        print("File or directory not found:", str(e))
    else:
        print("Error occurred during mount:", str(e))
finally:
    # Code to run regardless of whether an exception occurred or not
    print("Mount process completed")
