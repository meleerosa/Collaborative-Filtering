import operator

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class Model:
    def __init__(self, df):
        self._df = df
        self._item_similarity = cosine_similarity(self._df.T)
        self._user_similarity = cosine_similarity(self._df)
        self._user_sim_df = pd.DataFrame(self._user_similarity, index = self._df.index, columns = self._df.index)
        self._item_sim_df = pd.DataFrame(self._item_similarity, index = self._df.columns, columns = self._df.columns)

    def item_based_recommend(self, region, num = 5):
        if region in self._df.columns:
            return self._item_sim_df[region].sort_values(ascending = False)[1:num+1].to_dict()
        else:
            return 'No data'

    # 안가본곳 중에서만 추천
    def user_based_recommend_1(self, user):
        sim_users = self._user_sim_df.sort_values(by = user, ascending = False).index[1:11]
        best = []
        most_common = {}

        for i in sim_users:
            best.append(self._df.loc[i,:][(self._df.loc[user,:]) == 0].sort_values(ascending=False).index[:5].to_list())

        for i in range(len(best)):
            for j in best[i]:
                if j in most_common:
                    most_common[j] += 1
                else:
                    most_common[j] = 1
        sorted_list = sorted(most_common.items(), key = operator.itemgetter(1), reverse= True)
        return sorted_list[:5]

    # 전체에서 추천
    def user_based_recommend_2(self, user):
        sim_users = self._user_sim_df.sort_values(by = user, ascending = False).index[1:11]
        best = []
        most_common = {}

        for i in sim_users:
            best.append(self._df.loc[i,:].sort_values(ascending=False).index[:5].to_list())

        for i in range(len(best)):
            for j in best[i]:
                if j in most_common:
                    most_common[j] += 1
                else:
                    most_common[j] = 1
        sorted_list = sorted(most_common.items(), key = operator.itemgetter(1), reverse= True)
        return sorted_list[:5]