FROM python:3.7-slim

WORKDIR /app

# install python
RUN apt update && apt install protobuf-compiler libprotoc-dev libomp-dev -y

# mount repo files
COPY . .

# install python and system requirements
RUN python3.7 -m pip install -r requirements.txt
