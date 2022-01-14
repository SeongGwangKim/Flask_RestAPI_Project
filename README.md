# [ 이미지 변환 플라스크 Rest API ver01 ]

## 0. Flask Rest API - in  SunnyWeb : 이미지 변환 웹의 Flask Rest API


 <img src="https://user-images.githubusercontent.com/78336335/149068626-6f9eec38-6478-4f3b-8a39-12efc77f0bb7.png"  width="15%" height="15%"/>



## 1. 구성

<img src="https://user-images.githubusercontent.com/78336335/149068958-a7bd759c-b64b-4d37-9718-d7c0eebc12cf.png"  width="30%" height="30%"/>


#### 1) flaskRestAPI01 : 이미지 변환 기능 중 유명 화가풍으로 변환, 안경과 동물들의 특징을 이미지에 추가하는 기능을 담당하는 flask Rest API<br>
 * a) imgs : 안경, 돼지(코), 쥐(코, 귀) 이미지<br>
 * b) models<br>
   * b-1) instance_norm<br>
   * b-2) eccv16<br>
 * c) api_test01.py : json으로 request를 주었을 때를 테스트하는 모듈<br>
 * d) app01.py : flask로 웹 서버를 올려 json request를 json response를 보내주는 flask Rest API<br>
 * e) img_download.py : s3에서 이미지를 다운 받아서 임시 저장소에 이미지를 저장하는 함수를 가진 모듈<br>
 * f) plusimage.py : 이미지와 파일 이름을 넣으면 이미지를 추가해주는 함수를 가진 모듈<br>
 * g) total_pram : Rest API를 쉽게 사용할 수 있도록 조절할 파라미터만 모아 놓은 모듈<br>
 * h) transiamge : 이미지와 파일 이름을 넣으면 이미지를 변환해주는 함수를 가진 모듈<br>
 * i) upload_image : AWS S3의 버켓에 이미지를 업로드 하는 함수를 가진 모듈
    

#### 2) flaskRestAPI02 : 이미지 변환 기능 중 저화질의 이미지를 초고화질로 바꿔주는 기능을 담당하는 flask Rest API
 * a) api_test02.py : json으로 request를 주었을 때를 테스트하는 모듈
 * b) app02.py : flask로 웹 서버를 올려 json request를 json response를 보내주는 flask Rest API
 * c) img_download.py : s3에서 이미지를 다운 받아서 임시 저장소에 이미지를 저장하는 함수를 가진 모듈
 * d) total_pram : Rest API를 쉽게 사용할 수 있도록 조절할 파라미터만 모아 놓은 모듈
 * e) upload_image : AWS S3의 버켓에 이미지를 업로드 하는 함수를 가진 모듈 
    
    
## 2. 핵심 기능 및 파라미터 설명
1) app01.py, app02.py

   <img src="https://user-images.githubusercontent.com/78336335/149072459-6b952f83-9116-486d-8a7b-30bcee3f3973.png"  width="30%" height="30%"/>

    
 * a) route /transimage : 이미지를 유명 화가풍으로 변환해주는 app
    
   <img src="https://user-images.githubusercontent.com/78336335/149072586-eb0c5186-2036-49b7-b2d5-a40e5193cf03.png"  width="30%" height="30%"/>

   
 * b) route /plussimage : 이미지에 쥐(코, 귀)의 이미지를 추가해주는 app


   <img src="https://user-images.githubusercontent.com/78336335/149072654-4a51557d-6dd3-4d24-bd28-6bc4d104f2c6.png"  width="30%" height="30%"/>
    
    
 * c) route /esrganimage : 저화질의 이미지를 초고화질의 이미지로 변환해주는 app


## 1. 라이브러리
 * 1) flask
 * 2) boto3
 * 3) openCV
 * 4) numpy
 * 5) dlib
 * 6) tansorflow


## 2. Rest API 조절 파라미터
 * 1)  download_url = "다운로드 받을 url"
 * 2)  s3_upload_bucket_name = "s3에 업로드할 버켓 이름"
 * 3)  trans_image_model = "변환할 모델"
  
  #### # 변환 가능한 모델 리스트 : 
 * eccv16
   *   composition_vii.t7,
   *   la_muse.t7,
   *   starry_night.t7,
   *   the_wave.t7
   
   <br>
   
 * instance_norm  
   *   candy.t7,
   *   feathers.t7,
   *   la_muse.t7,
   *   mosaic.t7,
   *   starry_night.t7,
   *   the_scream.t7,
   *   udnie.t7

## 3. 프로세스 및 예시
  1) json으로 이미지 파일의 이름을 보낸다.

<img src="https://user-images.githubusercontent.com/78336335/148682855-9379f0c4-54a6-4de6-bdb7-ce5007c16ad1.png"  width="50%" height="50%"/>

  2) json으로 받은 이미지의 이름으로 s3에서 찾아 임시저장소에 다운로드한다.

<img src="https://user-images.githubusercontent.com/78336335/148682864-51b41514-cf92-42c0-9de6-286d3bb0be81.png"  width="80%" height="80%"/>

  3) 임시 저장한 이미지를 변환한 후에 이미지를 잠시 로컬에 저장한다.
  4) 변환된 이미지를 s3에 업로드한다.

<img src="https://user-images.githubusercontent.com/78336335/148682861-22e23ae6-ccb9-41f4-92e4-55d39b6b07a3.png"  width="80%" height="80%"/>


  5) 업로드 후 변환된 이미지를 삭제한다.
  6) 변환된 이미지의 이름을 json으로 보낸다.

<img src="https://user-images.githubusercontent.com/78336335/148682859-cf74e473-70f4-40b5-89e5-903cc11478cf.png"  width="50%" height="50%"/>


## 결과

  #### # composition_vii.t7
<img src="https://user-images.githubusercontent.com/78336335/149509054-f04ed1c4-73cf-455b-991d-0432286956c9.png"  width="80%" height="80%"/>

  #### # la_muse.t7
<img src="https://user-images.githubusercontent.com/78336335/149509124-9ab69230-23b5-4612-9a7f-357019e34e96.png"  width="80%" height="80%"/>

  #### # starry_night.t7
<img src="https://user-images.githubusercontent.com/78336335/148682862-9387c06b-b856-4e17-9858-53b57312252a.png"  width="80%" height="80%"/>

  #### # the_wave.t7
<img src="https://user-images.githubusercontent.com/78336335/149509161-251a6ff3-856b-495e-85a9-bb2b231a40e7.png"  width="80%" height="80%"/>


# 참고 사이트
1) http://amroamroamro.github.io/mexopencv/opencv/dnn_style_transfer.html
