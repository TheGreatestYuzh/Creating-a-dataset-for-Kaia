FROM python

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python

RUN pip install animeface

COPY . ./app

VOLUME /app/faces_output

CMD ["python", "./app/face_detection.py"]