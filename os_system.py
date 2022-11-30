import os

URL="tcu-sdlab/shigi_research"
DIR="shigi_research"
FILE="aaa.txt"
#SEARTのjsonのプロジェクト名の部分
#json_load['items'][i]['name']

#git cloneコマンドを使用
os.system('git clone https://github.com/%s.git'%URL)

#ここに処理を記述

os.system('chdir')

#ディレクトリの移動用コマンド
#os.chdir('..')

#cloneしたプロジェクトを削除
os.system('rmdir /s /q %s'%URL)

#ファイルの削除
#os.system('del /s /q %s.json'%FILE)
