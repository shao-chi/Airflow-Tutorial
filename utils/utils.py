import requests
from typing import Callable

from bs4 import BeautifulSoup


def textToTxt(fn: Callable, filename: str):
    with open(filename, 'w') as f:
        f.write(fn())


def getRequest(url):
    return requests.get(url)


def getSoup(url, parser="html.parser"):
    r = getRequest(url)
    return BeautifulSoup(r.text, parser)
