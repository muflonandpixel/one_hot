#начальный код
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
#решение
def my_get_dummies(df,str):
    type_of_column = set(df[str])
    for i in type_of_column:
        df.loc[df[str] == i, i] = 1
        df.loc[df[str] != i, i] = 0
    return df[list(type_of_column)]
print(data)
print(my_get_dummies(data, 'whoAmI'))