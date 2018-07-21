# 实现用户输入用户名和密码，当用户名为seven且密码为123时，登陆成功，否则登陆失败
# 最多允许输入3次
count = 0
while count <3:
    name = input('name:').strip()
    pw = input('passward:').strip()
    if name=='seven' and pw=='123':
        print('登陆成功')
    else:
        print('登陆失败')
        count+=1

# 分别书写数字5，10，32，7的二进制，八进制和十六进制
print('5、10、32、7的二进制分别为：', bin(5), bin(10), bin(32), bin(7))
print('5、10、32、7的八进制分别为：', oct(5), oct(10), oct(32), oct(7))
print('5、10、32、7的十六进制分别为：', hex(5), hex(10), hex(32), hex(7))

name = 'aleX'

# 移除name变量对应值两边的空格，并输入移除后的内容
print(name.strip())

# 判断name是否对应‘al'开头，并输出结果,是否是以’x'为结尾，并输出结果
print(name.startswith('al'))
print(name.endswith('x'))

# 将name变量中‘l'替换成’p'
print(name.replace('l', 'p'))

# 将name变量对应的值以‘l'分割，并输出结果
print(name.split('l'))

# 将name中对应的值变为大写
print(name.upper())
print(name.lower())

# 输出name中对应的第二个字符
print(name[1])

# 输出name中对应的前三个字符
print(name[: 3])

# 输出name中对应的后两个字符
print(name[-2:])

# 输出name中’e'所在的索引位置
print(name.index('e'))

# 循环name每个元素
for i in name:
    print(i)

# 利用下划线将列表中的每一个元素拼接
li = ['alex', 'eric', 'rain']
print('_'.join(li))

# 在l列表中追加元素
l = ['alex', 'eric', 'rain']
l.append('seven')
print(l)

# 在列表的第一个位置插入“Tony”
li.insert(0, 'Tony')
print(li)

# 修改列表li的第二个元素为‘kelly'
li[1] = 'kelly'
print(li)

# 删除列表中的元素’eric‘
# 利用索引删除，用pop
li.pop(1)
print(li)
# 利用关键字删除，用remove
li.remove('rain')
print(li)

#删除列表中2-4个元素
li = ['alex', 'eric', 'rain', 'kelly']
del li[1:]
print(li)

# 使用enumrate输出列表元素和序号（序号从100开始）
li = ['alex', 'eric', 'rain', 'kelly']
for k, v in enumerate(li, 100):
    print(k, v)

# 元组：计算元组的长度
tu = ('alex', 'eric', 'rain')
print(len(tu))

# 获取元组的第二个元素
print(tu[1])

# 使用for,len,range输出元组的索引
for i in range(len(tu)):
    print(tu.index(tu[i]))
    print(tu[i])

# 利用enumrate输出元组元素和序号(从10开始）
# for k in enumerate(tu, 10):
#     print(k)
for k, v in enumerate(tu, 10):
    print(k, v)

# 元组不可以修改变量，也不可以添加元素

# 字典：输出字典中所有的值
dic = {'k1': 'v1', 'k2': 'v2', 'k3': [1, 2, 3]}
for i in dic:
    # print(i)
    print(i, dic[i])

# 在字典dic中添加一对键值对：'k4': 'v4'
dic['k4'] = 'v4'
print(dic)

# 修改字典中’k1'对应值为‘alex’
dic['k1'] = 'alex'
print(dic)

# 在k3值上插入18
dic['k3'].append(18)
print(dic)

# 在k3值的第一个位置上插入44
dic['k3'].insert(0, 44)
print(dic)

# 转换
# 将字符串s变成列表
s = "alex"
print(list(s))

# 将s变为元组
print(tuple(s))

# 将列表变成元组
li = ['alex', 'rich']
print(tuple(li))

# 将元组变成列表
tu = ('alex', 'rain')
print(list(tu))

# 转码
n = '老男孩'

# 将字符串转换成utf-8编码的字节，并输出
a = n.encode('utf-8')
print(a)

# 将字节转换成utf-8编码的字节
b = a.decode('utf-8')
print(b)

# 将字符串转换成gbk编码的字节，并输出
c = n.encode('gbk')
print(c)

# 将字节转换成gbk编码的字节，并输出
d = c.decode('gbk')
print(d)