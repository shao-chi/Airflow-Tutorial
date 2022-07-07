import numpy as np

from utils.utils import getSoup, getRequest


def saveCatGif():
    url = getRandomCatGif()
    saveGifFromUrl(url, 'cat.gif')


def getRandomCatGif():
    url = "https://tenor.com/search/cat-memes-gifs"
    soup = getSoup(url)
    figureBlocks = soup.select("figure.GifListItem")
    randomIndex = np.random.choice(np.arange(len(figureBlocks)))
    figure = figureBlocks[randomIndex]
    return figure.find('img')['src']


def saveGifFromUrl(url, savePath):
    with open(savePath, 'wb') as f:
        f.write(getRequest(url).content)
