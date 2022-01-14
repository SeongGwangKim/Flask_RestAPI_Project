# Rest API 조절 파라미터

# 다운로드 받을 url
download_url = "https://transimagetest.s3.ap-northeast-2.amazonaws.com/"
# s3에 업로드할 버켓 이름
s3_upload_bucket_name = "transimagetest"


# 유명 화가풍으로 이미지 변환 모델
'''
* eccv16
   composition_vii.t7,
   la_muse.t7,
   starry_night.t7,
   the_wave.t7,

* instance_norm
   candy.t7
   feathers.t7
   la_muse.t7
   mosaic.t7
   starry_night.t7
   the_scream.t7
   udnie.t7
'''
model_catagory = "eccv16"
trans_image_model = "starry_night.t7"