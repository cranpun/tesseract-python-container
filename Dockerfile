FROM python:latest

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn
RUN apt-get clean

RUN pip install --upgrade pip; \
    pip install \
    pillow \
#    opencv-python \
    pytesseract

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]
