#使用には pandas,matplotlib,seabornのインストールが必須.全てpipで可能
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#図の設定
plt.style.use('default')
sns.set()
sns.set_style('whitegrid')
sns.set_palette('Blues')

#図に使用する配列(例)
list1 = [["data1", 21]]
colums=["kind","value"]

#list1とcolumsでデータフレーム df を作成
df = pd.DataFrame(data=list1,columns=colums)

#追加する配列
list2 = ["data1",11]

#list2とcolumsでデータフレーム df2 を作成
df2 = pd.DataFrame(data=[list2],columns=colums)

#df に df2 を挿入
df=df.append(df2, ignore_index = True)

print(df)

#x軸にkind,y軸にvalueを指定して表示
sns.violinplot(x=df["kind"], y=df["value"])
plt.show()
