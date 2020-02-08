FROM alpine:latest
RUN apk --update-cache add git python3
RUN pip3 install --upgrade pip
RUN git clone https://github.com/kumarstack55/python-flask-helloworld.git
RUN pip install flask
#CMD ls -l
#CMD ls -l ./python-flask-helloworld
CMD python3 ./python-flask-helloworld/app.py
