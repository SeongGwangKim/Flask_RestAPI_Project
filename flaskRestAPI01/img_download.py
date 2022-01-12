import cv2
import requests
from io import BytesIO
from PIL import Image
import numpy as np
import urllib.request

from flaskRestAPI01.total_param import download_url


def download_img(filename):

    # # 이미지 다운로드
    # urllib.request.urlretrieve(
    #     download_url+filename,
    #     filename)

    # 다운받을 이미지 url
    url = download_url+filename
    res = requests.get(url)

    #Img open
    img = np.asarray(Image.open(BytesIO(res.content)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# # 동작확인 테스트
# if __name__ == "__main__":
#     download_img("temp.jpg")