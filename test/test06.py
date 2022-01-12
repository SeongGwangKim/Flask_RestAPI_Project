'''
s3 = boto3.client('s3')
with open('FILE_NAME', 'wb') as f:
    s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)

* download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
- param wb : 파일 매개 변수의 모드(rb는 열려있는 파일)
- param BUCKET_NAME : s3의 버켓 이름
- param OBJECT_NAME : s3의 파일의 객체이름(파일명+확장자)
- param FILE_NAME : 내가 받을 경로+설정할 파일이름(파일명+확장자)
'''
# import boto3
#
# s3 = boto3.client('s3')
# with open('../flaskRestAPI01/temp1.jpg', 'wb') as f:
#     s3.download_fileobj('transimagetest', 'temp.jpg', f)


'''
import boto3

s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

* download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
- param BUCKET_NAME : s3의 버켓 이름
- param OBJECT_NAME : s3의 파일의 객체이름(파일명+확장자)
- param FILE_NAME : 내가 받을 경로+설정할 파일이름(파일명+확장자)
'''
import boto3

s3 = boto3.client('s3')
s3.download_file('transimagetest', 'temp.jpg', '../flaskRestAPI01/imgs/temp.jpg')