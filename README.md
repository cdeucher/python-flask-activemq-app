# Flask-Activemq-App

## DOCKER 
```
docker build -t activemq-cli:0.1 .
docker run -it --rm -p 8080:8080 -p 8181:8181 -v $(pwd):/usr/src/app activemq-cli:0.1
```

## RUN
```bash
python setup.py install
python run.py
```
