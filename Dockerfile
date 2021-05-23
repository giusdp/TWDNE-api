FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app

# install python
RUN apt update && apt install protobuf-compiler libprotoc-dev libomp-dev -y

# mount repo files
COPY . .

# install python and system requirements
RUN python -m pip install -r requirements.txt
