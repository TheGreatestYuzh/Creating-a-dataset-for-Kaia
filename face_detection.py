# create nn for faces real people detection

import cv2
import animeface
import os

# weights = './opencv_face_detector.pbtxt'
# nn_configuration = './opencv_face_detector_uint8.pb'

# faceNet = cv2.dnn.readNet(nn_configuration, weights)

# create nn for anime faces detection

# face_cascade = cv2.CascadeClassifier('cascade_model/lbpcascade_animeface2.xml')

# def highlightAnimeFace(frame):
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray_frame = cv2.equalizeHist(gray_frame)
#     faces_rect = face_cascade.detectMultiScale(gray_frame)
#     for (x, y, w, h) in faces_rect:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     return frame

def get_crop_image(image, x, y, crop_width=512, crop_height=512):
    cropped_image = image[y:y+crop_height, x:x+crop_width]
    return cropped_image

def highlightFaceByAnimeface(frame):
    faces = animeface.detect(frame)
    face = faces[0].face.pos
    x = face.x
    y = face.y
    w = face.width
    h = face.height

    crop_img = get_crop_image(frame, x - 50, y - 50)

    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return crop_img

video = cv2.VideoCapture('./videos/one_piece_trailer.mp4')

output_folder = 'faces_output'

# Создаем папку для сохранения лиц, если её нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

face_count = 0

while cv2.waitKey(1) < 0:
    hasFrame, frame = video.read()
    print(1)
    if not hasFrame:
        print(0)
        cv2.waitKey()
        break

    # resultImg, faceBoxes = highlightFace(faceNet, frame)

    # if not faceBoxes:
    #     # выводим в консоли, что лицо не найдено
    #     print("Лица не распознаны")

    crop_img = highlightFaceByAnimeface(frame)

    face_filename = f'{output_folder}/face_{face_count}.jpg'
    try:
        cv2.imwrite(face_filename, crop_img)
    except:
        print(crop_img)
    face_count += 1

    # выводим картинку с камеры
    cv2.imshow("Face detection", crop_img)
