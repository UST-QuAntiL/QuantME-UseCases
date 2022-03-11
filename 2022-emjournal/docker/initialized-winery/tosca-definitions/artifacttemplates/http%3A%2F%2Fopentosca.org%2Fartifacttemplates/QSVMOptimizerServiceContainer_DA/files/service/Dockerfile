FROM python:3.7-slim
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

COPY service.zip /tmp/service.zip

RUN apt-get update && apt-get install -y gcc python3-dev unzip
RUN pip install requests qiskit==0.33.1

RUN unzip /tmp/service.zip -d /

CMD python QSVMOptimizerService.py
