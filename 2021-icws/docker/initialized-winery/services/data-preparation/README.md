# QHana Data Preparation Microservice

Service providing the data preparation functionality of the [QHAna Tool](https://github.com/UST-QuAntiL/qhana).

### Setup the Environment

The requirements.txt file can be used to install the dependencies when using pip:

```
pip install -r requirements.txt
```

### Running the Service

The data preparation service is using Quart as hosting library and Hypercorn as ASGI server.
The API can be run from the working directory of the data preparation service:

```
hypercorn -b 127.0.0.1:<port> app:app
```

or

```
python app.py <port>
```

### Docker

The service can also be executed using Docker:

```
docker build -t quantil/data-preparation-service .
docker run -it -p 5000:5000 quantil/data-preparation-service
```