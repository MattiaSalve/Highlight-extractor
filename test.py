import pandas as pd

df = pd.DataFrame({"Ciao": [1], "Come": [2]})
serie = pd.DataFrame({"Ciao": [3], "Come": [4]})
df = pd.concat([df, serie], ignore_index=True)
print(df)
