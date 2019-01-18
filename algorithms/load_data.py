import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_iris(std=False):
    df = pd.read_csv(
        filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
        header=None, 
        sep=',')

    df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    df.dropna(how="all", inplace=True) # drops the empty line at file-end

    X = df.ix[:,0:4].values
    y = df.ix[:,4].values

    if std:
        X = StandardScaler().fit_transform(X)

    return X, y