"""
Decoding function.

This Python code will decode a one-hot vector of wickelfeatures back into a
verb after the neural network training.
"""
import pandas as pd
import numpy as np
import decoding_function as dec
from Files import nodes
wickelfeatures_list = nodes.nds


def decoding(vector):
    """
    Receive a vector that represents the prediction of
    wickelfeatures of a verb.

    :vector type: list
    :r type: str (?)
    """
    def createdf(vector):
        """
        Create a dataframe of wickelfeatures and prediction values.

        :vector type: list
        :r type: dataframe (pandas)
        """
        new = np.asarray(vector)
        df = pd.DataFrame()
        df['wickelfeatures'] = wickelfeatures_list
        df['values'] = new
        return df

    def sixteenbest(df):
        """
        Select sixteen best wickelfeatures.

        :df type: df (pandas)
        :r type: df (pandas)
        """
        x = df.sort_values(by = ['values'], axis = 0, ascending = False, inplace = False, kind='quicksort', na_position = 'last')
        r = x.head(16)
        return r.sort_index(axis=0)

    def find_compatible(df1, df2):
        """
        Find Compatible.

        returns a new df with compatible wickelfeatures

        :df1 type: df
        :df2 type: df
        :r type: df
        """
        df3 = pd.DataFrame()
        df2['aux'] = ''
        for index, row in df2.iterrows():
            df2.iloc[index, df2.columns.get_loc('aux')] = row['wickelfeatures'][0] + row['wickelfeatures'][1]
        for index, row in df1.iterrows():
            last_two = row[0][-2]+row[0][-1]
            df3 = df3.append(df2[df2['aux'].isin([last_two])])
        return df3.sort_index(axis=0)
    dfx = createdf(vector)
    begin = sixteenbest(dfx[361:])
    end = sixteenbest(dfx[261:361])
    dbeg = ''
    dend = ''
    for i in range(0, 3):
        dbeg = dbeg + dec.competion(begin['wickelfeatures'], i)
    for i in range(0, 3):
        dend = dend + dec.competion(end['wickelfeatures'], i)
    decoded = dbeg
    while True:
        new_df = find_compatible(begin, dfx)
        prox = list(sixteenbest(new_df)['wickelfeatures'])
        phoneme = dec.competion(prox, 2)
        print(phoneme)
        decoded = decoded + phoneme
        print(decoded)
        begin = sixteenbest(new_df)
        print(dend)
        if decoded[-2] == dend[0] and decoded[-1] == dend[1]:
            break
        if decoded[-1] == '#':
            break

    return decoded