# python-flask-helloworld

```bash
git clone https://github.com/kumarstack55/python-flask-helloworld.git
cd python-flask-helloworld

sudo docker build -t python-flask-helloworld ./

sudo docker container stop python-flask-hellworld
sudo docker container rm python-flask-hellworld
sudo docker run --name python-flask-hellworld -d -p 20080:10080 python-flask-helloworld

curl -q http://127.0.0.1:20080/
```
