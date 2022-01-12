import cv2
import numpy as np

from flaskRestAPI01.total_param import trans_image_model


def transfer_image(image, filename):
    net = cv2.dnn.readNetFromTorch("models/eccv16/eccv16/"+trans_image_model)

    img = image

    # 전처리
    h, w, c = img.shape

    img = cv2.resize(img, dsize=(500, int(h / w * 500)))  # 사이즈 변경

    print(img.shape)

    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)  # img의 각 픽셀에서 MEAN_VALUE를 빼주는 연산

    print(blob.shape)  # 앞에 1을 추가시키고 차원의 순서를 변경

    # 후처리
    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))  # squeeze : 차원 축소, transpose : 차원 변경
    output += MEAN_VALUE  # MEAN_VALUE를 다시 더해줌

    output = np.clip(output, 0, 255)  # np.clip : 값을 0~255로 제한 시켜줌
    output = output.astype('uint8')  # astype('uint8') : 정수형태로 바꿔줌
    cv2.imwrite('rev_'+filename, output)
    return output

# # 동작확인 테스트
# if __name__ == "__main__":
#     image = cv2.imread('temp.jpg')
#     transfer_image(image, "temp.jpg")