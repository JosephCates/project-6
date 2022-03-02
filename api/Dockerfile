FROM python:3.8
LABEL maintainer="jcates5@uoregon.com"
RUN apt-get update -y
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["flask_brevets.py"]
