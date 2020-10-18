import numpy as np
import matplotlib as plt
from google_play_scraper import app


def main():
    arr = np.array([[1,2,4], [3,4,5]])
    print(arr)
    arr1 = arr.transpose()
    print(arr1)
    result = app(
        'org.duosoft.books20century',
        lang='ru', # defaults to 'en'
        country='ru' # defaults to 'us'
    )
    print(result)


if __name__ == '__main__':
    main()