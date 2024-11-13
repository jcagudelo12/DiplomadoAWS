import boto3

#Crear cliente para conectarme a S3 de AWS
s3 = boto3.client(
    's3',
    aws_access_key_id ='AKIAQWHCQCNBHE36CVXI',
    aws_secret_access_key='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')

#Listamos los buckets de S3
resultado = s3.list_buckets()

for bucket in resultado['Buckets']:
  print(bucket['Name'])