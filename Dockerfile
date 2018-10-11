FROM python:latest

RUN cd /root; \ 
    wget http://www.leptonica.com/source/leptonica-1.71.tar.gz; \
    tar xzvf /root/leptonica-1.71.tar.gz; \
    cd /root/leptonica-1.71; \
    ./configure; make; make install; \
    rm -rf /root/leptonica*;

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libleptonica-dev
RUN apt-get clean

RUN pip install --upgrade pip; \
    pip install \
    pillow \
#    opencv-python \
    pytesseract

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]