# To build & run this image, use the following command:
#   $ docker build -t jobhunter . && docker run --rm -it jobhunter

FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -e .


ENTRYPOINT ["/bin/bash"]