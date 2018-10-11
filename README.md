# tesseract-python-container
Docker container for tesseract by python (pytesseract).

# environment
only docker & docker-compose

# how to use

``` commandline
$ docker-compose build # (only first)
$ docker-compose up -d
$ docker-compose exec tesseractpython python /path/to/your/script/on/container
```

# notice
This docker container maps top of git repository directory to `/opt/` on container. 

# how to use tesseract command
If you use tesseract command (without python), run on commandline `docker-compose exec tesseractpython tesseract ....`.

# sample

```commandline
$ docker-compose exec tesseractpython python /opt/sample/sample.py
  # output result of reading samle1.png to sample4.png

$ docker-compose exec tesseractpython tesseract /opt/sample/textsample.png
  # output result of reading sampletext.png
```

