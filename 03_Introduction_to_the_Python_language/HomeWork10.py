"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""

import pandas as pd
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

# Первый вариант
data["robot"] = (data["whoAmI"] == "robot").astype(int)
data["human"] = (data["whoAmI"] == "human").astype(int)

# Второй вариант
# data.loc[data["whoAmI"] == "robot", "robot"] = 1
# data.loc[data["whoAmI"] == "human", "human"] = 1
# data.fillna(0, inplace=True)

print(data.head(10))
