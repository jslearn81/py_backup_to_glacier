# py_backup_to_glacier
This is a simple python script to backup your local files to S3 Deep Glacier Archival which is super cheap and robust due to the geo-location redundancy.
Never worry about losing your data anymore !


# Usage
1. Please setup environment variable AWS_SERVER_PUBLIC_KEY and AWS_SERVER_SECRET_KEY.
2. Using command line, run the following sample command "python upload_to_s3_glacier.py -f "q:/blahblah.zip" -b mybackup2023sep"

# FAQ: Why not just use AWS CLI or console?

AWS Web Console - Max size 160GB. And you get disconnected sometimes while uploading.<br/>
AWS CLI - Max size 5GB via single PUT. <br/>
AWS SDK/Multipart (Which this Python script is based on) - Max Size <b>5TB</b><br/>

See: https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html

Anyway i just created it because i like to have something in python. hopefully , you find the code useful in your app as well.

# Author
https://github.com/quantumfusionlearn/
