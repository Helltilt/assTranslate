# assTranslate
A Python 3.5+ script that automatically translates ass subtitles files with Google Translate

### Dependency
--------
assTranslate uses [TextBlob](https://github.com/sloria/textblob), so you need to install it like this:
```sh
$ pip install -U textblob
$ python -m textblob.download_corpora
```
### Usage
--------
```sh
assTranslate.py [-h] -i INPUT -l LANG

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input ass filename
  -l LANG, --lang LANG  destination language
```
