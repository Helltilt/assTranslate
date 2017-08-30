assTranslate
====================================

A script that automatically translates ass subtitles files with Google Translate

Requirements
------------

- Python >= 3.5

Dependency
----------


    $ pip install -U textblob
    $ python -m textblob.download_corpora
    
Usage
----------


    assTranslate.py [-h] -i INPUT -l LANG

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input ass filename
      -l LANG, --lang LANG  destination language

