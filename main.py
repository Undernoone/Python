print(20020729)
print("helloworld")
print('helloworld')
#单引号和双引号都可以，但是推荐使用双引号
name = 'coder729'
#在Python中不需要使用关键字string关键字去声明数据类型
print(name)
print('我的名字是'+name)
#加号是字符串连接符，可以连接多个字符串，也可以连接变量和字符串
print(name,"在学习Python")
print(name,"在学习Python",sep="")
#逗号默认是空格，可以使用sep参数指定分隔符，sep参数默认为空格
# print括号内最后默认会加上一个换行符，如果不想换行，可以用end参数指定结束符
print(end="修改换行符")
print('test')