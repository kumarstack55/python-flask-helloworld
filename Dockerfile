FROM alpine:latest
ADD . /python-flask-helloworld
WORKDIR /python-flask-helloworld
RUN set -x \
  && apk --update-cache add python3 \
  && pip3 install --upgrade pip \
  && pip3 install flask
CMD python3 ./app.py
