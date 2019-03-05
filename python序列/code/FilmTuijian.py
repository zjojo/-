#encodig:utf-8
"""
电影评分及推荐
"""
from random import randrange

#历史电影打分数据
data = {"user" +str(i):{"film"+str(randrange(1, 15)): randrange(1, 6) for j in range(randrange(3, 10))}
        for i in range(10)}
#解释user 是字典推导式，生成从用户1到用户9，
#解释film：用户看过的电影也是字典推导式，在随机的3-10次数中，看到电影的名字是随机的从1,15中获取，对应的评分数据
# 也是随机从1,6中获取,即每一个用户可能看过的电影个数是不一致的,,且看过的电影名称是不一致的，评分也是随机的
#这里包含了三个随机：用户对应看过的电影个数随机；用户看过的电影名称随机，用户看过电影的评分随机

print(data)
#当前用户评分
user ={'film' +str(randrange(1,15)): randrange(1,6) for i in range(5)}
print(user)

#最相似的用户及其对电影打分情况
#两个用户共同打分的电影最多
#并且所有电影打分的差值的平方和最小
similarUser, films = min(data.items(), key=lambda item:(-len(item[1].keys()&user.keys()),
                         sum(((item[1].get(film) - user.get(film))**2
                              for film in user.keys()&item[1].keys()))))
#lambda函数语法：lambda parameters:express,这里lambda返回一个元组s，一个是用户共同打分的负数，一个是打分差值平方和
#min函数按照执行key的标准返回，因为data.sitems是返回键值对，所以key对应的是两个值，key按照平均分求最大值，value按照平方和求最小值
print("koown data".center(50, "="))
#center函数将打印的字居中显示，然后空白的地方用=代替

for item in data.items():
    print(len(item[1].keys()&user.keys()),
          sum(((item[1].get(film) - user.get(film))**2
                              for film in user.keys()&item[1].keys())),item,sep=':')
print('current data'.center(50, '='))
print(user)
print('most similar user and his filename'.center(50,'='))
print(similarUser, films,sep=':')
print('recommednfile film'.center(50),'=')
print(max(films.keys()-user.keys(), key=lambda film:films[film]))