# Simple KV Service
Simple KV service written with Flask and Sqlite. Service can be accessed via HTTP and CLI Packaged in same repo.

Topic:  
[Index](readme.md) | [CLI](cli.md)| [Deployment](deployment.md)

---
### Local Development:
With `Virtualenv`:
```
$ cd simpleKVService/
$ venv py3.8 --python 3.8
$ pip install -r ./requirements.txt


```

Setting up `Environment`:
```
$ export FLASK_APP=kvservice
$ export FLASK_ENV=development
$ flask run
$ # To run test
$ pytest
```


With `Docker`

```
docker-compose up
```
That's all for Docker !!


Service Running at  `http://127.0.0.1:5000`

---






