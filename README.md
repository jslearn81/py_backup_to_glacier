# py_backup_to_glacier
This is a simple python script to backup your local files to S3 Deep Glacier Archival which is super cheap and robust due to the geo-location redundancy.
Never worry about losing your data anymore !


# Usage
1. Please setup environment variable AWS_SERVER_PUBLIC_KEY and AWS_SERVER_SECRET_KEY.
2. Using command line, run the following sample command "python upload_to_s3_glacier.py -f "q:/blahblah.zip" -b mybackup2023sep"

# FAQ: Why not just use AWS CLI or console?

Web Console - Max size 160GB. And you get disconnected sometimes while uploading.<br/>
AWS CLI - Max size 5GB<br/>
AWS SDK (Which Python script is based on) - Max Size <b>5TB</b><br/>

See: https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html


# Author
https://github.com/quantumfusionlearn/
