import os

from flask import Flask, jsonify, request
from flaskRestAPI01.img_download import download_img
from flaskRestAPI01.plusimage import plusimg
from flaskRestAPI01.transimage import transfer_image
from flaskRestAPI01.upload_image import upload_file


app = Flask(__name__)


@app.route('/transimage', methods=['POST'])
def transimage():
    data = request.get_json()[0]
    file_name = data["origin"]
    print(file_name)

    #이미지 다운로드(임시 저장)
    img = download_img(file_name)

    # 이미지 변환
    transfer_image(img, file_name)

    # json에 보내줄 이름
    rev_file_name = "rev_" + file_name
    response = {'results': rev_file_name}

    # s3에 이미지 업로드
    upload_file(rev_file_name)

    # 임시로 저장한 파일 제거
    os.remove(rev_file_name)

    return jsonify(response)


@app.route('/plussimage', methods=['POST'])
def plusimage():
    data = request.get_json()[0]
    file_name = data["origin"]
    print(file_name)

    #이미지 다운로드(임시 저장)
    img = download_img(file_name)

    # 이미지 변환
    plusimg(img, file_name)

    # json에 보내줄 이름
    rev_file_name = "rev_" + file_name
    response = {'results': rev_file_name}

    # s3에 이미지 업로드
    upload_file(rev_file_name)

    # 임시로 저장한 파일 제거
    os.remove(rev_file_name)

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)


