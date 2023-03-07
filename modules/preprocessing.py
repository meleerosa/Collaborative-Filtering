import warnings

import numpy as np

warnings.filterwarnings(action='ignore')

import pandas as pd
import scipy as sp
from pandas.io.json import json_normalize
from sklearn.metrics.pairwise import cosine_similarity


class Preprocess:
    def __init__(self, data):
        self._data = data
        self._df = pd.DataFrame()

    def make_dataset(self):
        for i in range(len(self._data)):
            self._region_df = json_normalize(self._data[i]['travelFavorite_set'])
            self._region_df['user_id'] = [self._data[i]['user_id']]*len(self._region_df)
            self._df = pd.concat([self._df, self._region_df], axis = 0)
            self._pivot_df = self._df.pivot_table(index = 'user_id', columns = 'region', values = 'score')
            self._base_norm = self._pivot_df.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
            self._base_norm.fillna(0, inplace=True)
            self.base_sparse = sp.sparse.csr_matrix(self._base_norm.values)
        
        return self._base_norm
