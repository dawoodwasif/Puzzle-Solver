
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm


def get_piece(a, size=128, cuts=2):

    """
       extracts each piece of the puzzle and returns
    """

    cut_len = size // cuts

    if cuts == 3:
        a = np.array([a[:, 0:cut_len, :], a[:, cut_len:cut_len * 2, :], a[:, cut_len * 2:cut_len * 3, :]])
        a = np.concatenate(
            (a[:, 0:cut_len, :, :], a[:, cut_len:cut_len * 2, :, :], a[:, cut_len * 2:cut_len * 3, :, :]))
    if cuts == 2:
        a = np.array([a[:, 0:cut_len, :], a[:, cut_len:, :]])
        a = np.concatenate((a[:, 0:cut_len, :, :], a[:, cut_len:, :, :]))

    return a

def load_data(df, cuts=2):

    """
        loads and returns data
    """

    # data = pd.read_csv(base_path + '{}.csv'.format(path))
    # path = base_path + path + '/'

    x = []
    y = []
    total = len(df)
    for i in tqdm(range(total)):

        im = Image.open(df.iloc[i]['path'])
        im = np.array(im).astype('float16')
        im = im / 255 - 0.5
        x.append(get_piece(im))

        label = df.iloc[i]['label']
        label = [int(i) for i in list(label)]
        y.append(label)

    return (np.array(x), np.expand_dims(np.array(y), axis=-1))