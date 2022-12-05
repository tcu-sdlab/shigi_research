import json,os

#Linux用

#jsonファイルを解析し,必要な情報のリストを返す関数
def make_list(repo_json):
    json_open = open(repo_json, 'r',encoding="utf_8")
    json_load = json.load(json_open)

    name_list = []
    for i in range(0,len(json_load['items'])):
        name_list.append(json_load['items'][i]['name'])

    json_open.close()
    return name_list

#リストからリファクタリング検知を行い,必要なリファクタリングのリストのみを抽出
def categorize_ref(name_list):

    target = '/'

    for i in range(0,len(name_list)):
        filename = name_list[i].replace('/', '__')
        print(filename)
        idx = name_list[i].find(target)
        reponame = name_list[i][idx+1:]

        #リファクタリング検知
        os.system('git clone https://github.com/%s.git'%name_list[i])

        os.system('./RefactoringMiner -a %s -json result/%s.json'% (reponame, filename))

        os.system('rm -R %s'%reponame)
    return 0

#main関数
repo_json='results.json'
name_list=make_list(repo_json)
categorize_ref(name_list)
