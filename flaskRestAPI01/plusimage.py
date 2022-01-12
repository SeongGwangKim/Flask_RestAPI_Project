import cv2
import dlib


def plusimg(image, filename):
    img = image
    detector = dlib.get_frontal_face_detector()
    sticker_img = cv2.imread('imgs/sticker01.png', cv2.IMREAD_UNCHANGED)  # cv2.IMREAD_UNCHANGED해야 투명도 포함해서 이미지 들어감
    dets = detector(img)
    print("number of faces detected:", len(dets))  # dets의 길이를 확인하여 얼굴의 갯수만큼 늘어난다.

    # 얼굴의 갯수만큼 적용
    for det in dets:
        x1 = det.left() - 40
        y1 = det.top() - 90
        x2 = det.right() + 40
        y2 = det.bottom() + 30

        # cv2.rectangle(img, pt1 = (x1,y1), pt2 =(x2,y2), color=(255,0,0), thickness=2)
        # print(det) # det에 얼굴의 좌표(x1,y1), (x2,y2)와 갯수가 저장되며 print로 보여줌.

        # 얼굴 영역에서 잘렸거단 에러가 났을 때의 상황을 방지해주는 코드
        try:
            # 올릴 이미지 카피
            overlay_img = sticker_img.copy()

            # 얼굴 크기만큼 resize
            overlay_img = cv2.resize(overlay_img, dsize=(x2 - x1, y2 - y1))

            # 오버레이를 실제로 덮어 씌움.
            overlay_alpha = overlay_img[:, :, 3:4] / 255.0
            background_alpha = 1.0 - overlay_alpha
        except:
            pass

        img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2]

    cv2.imwrite('rev_'+filename, img)
    return img


# # 동작확인 테스트
# if __name__ == "__main__":
#     img = cv2.imread('temp.jpg')
#     plusimg(img, "temp.jpg")

