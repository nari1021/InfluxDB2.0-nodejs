# InfluxDB2.0-nodejs
InfluxDB2.0 connected by Node.js

The environments are following.
- InfluxDB 2.0
- Node.js v14.17.2
- python v3.6.8
- pip v21.1.3

# How to install

```
$ git clone https://github.com/nari1021/InfluxDB2.0-nodejs.git
$ cd ./InfluxDB2.0-nodejs
$ npm install
$ npm run start
```


with python

```
$ yum install python3
$ python3 -V 
Python 3.6.8
$ pip -V
pip 21.1.3 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
```

# .env settings

```
INFLUX_URL = InfluxDB 2.0 installed server ip
INFLUX_TOKEN = InfluxDB 2.0 token
INFLUX_ORG = organization name
INFLUX_BUCKET = bucket name
INFLUX_USER = user name
INFLUX_PASS = user password
```
