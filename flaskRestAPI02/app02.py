import os

from flask import Flask, jsonify, request
from flaskRestAPI02.img_download import download_img
from flaskRestAPI02.trans_esrgan import preprocess_image
from flaskRestAPI02.upload_image import upload_file


app = Flask(__name__)


@app.route('/esrganimage', methods=['POST'])
def esrganimage():
    data = request.get_json()[0]
    file_name = data["origin"]
    print(file_name)

    #이미지 다운로드(임시 저장)
    img = download_img(file_name)

    # 이미지 변환
    preprocess_image(img, file_name)

    # json에 보내줄 이름
    rev_file_name = "rev_" + file_name
    response = {'results': rev_file_name}

    # s3에 이미지 업로드
    upload_file(rev_file_name)

    # 임시로 저장한 파일 제거
    os.remove(rev_file_name)

    return jsonify(response)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5001", debug=True)



