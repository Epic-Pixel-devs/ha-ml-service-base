# IMAGE
FROM python:3.7.3

RUN pip install --upgrade pip

# Set working space directory
WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip

# install python packages
RUN pip install -r requirements.txt

# copy files to /app
COPY . .

# install audio libraries
# RUN apt-get update && apt-get install -y libsndfile1 libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg

# Runner
CMD [ "python", "app.py"]