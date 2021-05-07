import configparser


cf=configparser.ConfigParser()

cf.read('case.ini',encoding='utf-8')

#数据读取
res=cf.get('MODE','mode')
print(res)
res=cf['MODE']['mode']
print(res)

"""
每个配置文件存在
section:片区名称
option:片区中某一具体的值的KEY
"""
print(cf.sections())  #读取配置文件的section 信息
print(cf.items('PYTHON')) #读取配置文件section中PYTHON的option信息


# if __name__ == '__main__':
#     data=[]
#     info={}
#     info["name"]="大王"
#     data.append(info)
#     print(data)
#     data=[]
#     info={}
#     info["name"]="小王子"
#     data.append(info)
#     print(data)