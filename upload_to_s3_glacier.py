'''
Author: https://github.com/quantumfusionlearn

Description:
Simple script to use python and boto3 to upload to S3 Glacier deep archival. With a nice progressbar.
I use it to backup my personal files.
Please setup environment variable AWS_SERVER_PUBLIC_KEY and AWS_SERVER_SECRET_KEY.


Usage:
Command line sample code:
python upload_to_s3_glacier.py -f "q:/blahblah.zip" -b mybackup2023sep

'''

import progressbar
import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys
from argparse import ArgumentParser


#Get credential from environment variable
AWS_SERVER_PUBLIC_KEY = os.environ['AWS_SERVER_PUBLIC_KEY'] #this is also known as key ID in AWS CLI
AWS_SERVER_SECRET_KEY = os.environ['AWS_SERVER_SECRET_KEY'] #This is key secret in AWS CLI


#Get arguments from runtime variables
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="local file path to upload", metavar="FILE")
parser.add_argument("-d", "--dest_file", dest="dest_filename",
                    help="dest file path to write to. Optional", metavar="FILE")
parser.add_argument("-b", "--bucket", dest="bucket",
                    help="s3 bucket name", metavar="BUCKET")

args = parser.parse_args()


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    statinfo = os.stat(args.filename)
    up_progress = progressbar.progressbar.ProgressBar(maxval=statinfo.st_size)
    up_progress.start()


    def upload_progress(chunk):
      up_progress.update(up_progress.currval + chunk)


    # Upload the file
    s3_client = boto3.client('s3', 
                      aws_access_key_id=AWS_SERVER_PUBLIC_KEY, 
                      aws_secret_access_key=AWS_SERVER_SECRET_KEY
                      )
    try:
        s3_client.upload_file(Filename=file_name,Bucket=bucket,Key=object_name,Callback=upload_progress)
        up_progress.finish()
    except ClientError as e:
        logging.error(e)
        return False
    return True




#Main Call
if __name__ == "__main__":
  upload_file(file_name = args.filename,bucket=args.bucket,object_name=args.dest_filename)
