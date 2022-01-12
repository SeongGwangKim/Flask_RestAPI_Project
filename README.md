# 이미지 변환 플라스크 Rest API


## 1. 구성 라이브러리
1) flask
2) boto3 : s3 rest api - s3로 이미지 업로드
3) cv2 : opencv - 이미지 처리
4) 


## 2. Rest API 조절 파라미터
# 1) download_url = "다운로드 받을 url"
# 2) s3_upload_bucket_name = "s3에 업로드할 버켓 이름"
# 3) trans_image_model = "변환할 모델"
* 변환 가능한 모델 리스트
candy.t7
feathers.t7
la_muse.t7
mosaic.t7
starry_night.t7
the_scream.t7
udnie.t7

## 3. 프로세스 및 예시
1) json으로 이미지 파일의 이름을 보낸다.

![json1](https://user-images.githubusercontent.com/78336335/148682855-9379f0c4-54a6-4de6-bdb7-ce5007c16ad1.png)

2) json으로 받은 이미지의 이름으로 s3에서 찾아 임시저장소에 다운로드한다.

![업로드된원본](https://user-images.githubusercontent.com/78336335/148682864-51b41514-cf92-42c0-9de6-286d3bb0be81.png)

3) 임시 저장한 이미지를 변환한 후에 이미지를 잠시 로컬에 저장한다.
4) 변환된 이미지를 s3에 업로드한다.

![변환된이미지업로드](https://user-images.githubusercontent.com/78336335/148682861-22e23ae6-ccb9-41f4-92e4-55d39b6b07a3.png)


5) 업로드 후 변환된 이미지를 삭제한다.
6) 변환된 이미지의 이름을 json으로 보낸다.

![json2](https://user-images.githubusercontent.com/78336335/148682859-cf74e473-70f4-40b5-89e5-903cc11478cf.png)


# 결과
![변환전후](https://user-images.githubusercontent.com/78336335/148682862-9387c06b-b856-4e17-9858-53b57312252a.png)

