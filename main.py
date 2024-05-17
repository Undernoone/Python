# print(20020729)
# print("helloworld")
# print('helloworld')
# #单引号和双引号都可以，但是推荐使用双引号
# name = 'coder729'
# #在Python中不需要使用关键字string关键字去声明数据类型
# print(name)
# print('我的名字是'+name)
# #加号是字符串连接符，可以连接多个字符串，也可以连接变量和字符串
# print(name,"在学习Python")
# print(name,"在学习Python",sep="")
# #逗号默认是空格，可以使用sep参数指定分隔符，sep参数默认为空格
# # print括号内最后默认会加上一个换行符，如果不想换行，可以用end参数指定结束符
# print(end="修改换行符")
# print('test')
# print(len(name))
# print(type(name))
# year = [2024,2025,2026]
# print(type(year))
# year = input("请输入年份：")
# print(type(year))
# month = int(input("请输入月份："))
# print(type(month))
# #input函数默认接收的为字符串数据类型，如果需要输入整数，可以先将字符串转换为整数
# if 2>1:
#     print("hello")
# else:
#     print("end")
# Python_list = [1,2,3,4,5]
# print(Python_list)
# print(Python_list[0])
# print(Python_list[1:3])
# print(Python_list[2:])
# Python对列表添加函数可以用append()方法，删除函数用pop()方法，修改函数用insert()方法，排序函数用sort()方法
# Python_list.append(6)
# print(Python_list)
# Python_list.pop(2)
# print(Python_list)
# remove()方法可以删除指定元素，但只能删除第一个匹配的元素
# Python_list.remove(4)
# print(Python_list)
# price=[100,200,300,400,500]
# max=max(price)
# min=min(price)
# sort_price=sorted(price)
# print(max)
# print(min)
# print(sort_price)
# user_information ={"name":"coder729","age":'20',"gender":"male"}
# print(user_information)
# search = input('请输入想要查询的数据:')
# if search in user_information:
#     print(user_information[search])
# else:
#     print("没有找到该数据")
# user_information = {('coder729',22):"20020729",
#                     ('coder728',21):'20020728',
#                     ('coder727',20):"20020727"}
# print(user_information)
# user_information[('coder729',19)] = "20020728"
# print(user_information)
# 想要添加元素到字典中，可以直接用字典名[键] = 值的方式添加，如果键不存在，则会自动添加，如果键存在，则会修改值
# list1 = [1,2,3,4,5]
# for i in list1:
#     if i > 3:
#         print(i)
#     else:
#         print("小于等于3")
# user_informatin = {"coder729":729,"coder728":728,"coder727":727}
# for user_id in user_informatin.items():
#     print(type(user_id))
# number = [1,2,3,4,5,6,7,8,9]
# for num in number:
#     # content = str(num) +'号号码'+"是"+str(num)
#     content = "{0}号号码是{0}".format(num)
#     print(content)
# format函数可以格式化字符串，{0}表示第一个参数，{1}表示第二个参数，以此类推
# def area(width,height):
#     area_number = width * height
#     return area_number
# print(area(5,6))
# print(area(100,9))
# def bmi(height,weight):
#     bmi_number = weight / (height ** 2)
#     return bmi_number
# print(bmi(1.71,60))
# import statistics
# print(statistics.median([1,2,3,4,5,6]))
# class Cat:
#     def __init__(self, cat_name,cat_age):
#         self.name = cat_name
#         self.age = cat_age
#     def speak(self):
#         print("喵喵喵")
#     def think(self,content):
#         print(f"小猫{self.name}在思考{content}")
# cat1 = Cat('white',1)
# cat1.think('今天吃什么鱼')
# class Student:
#     def __init__(self,name,student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = {"语文":80,"数学":90,"英语":85}
#     def set_grade(self,subject,grade):
#         if subject in self.grades:
#             self.grades[subject] = grade
# WANG = Student("王义","2010507103")
# CHEN = Student("陈晨","2010507104")
# WANG.set_grade("数学",95)
# print(WANG.grades)
# class Mammal:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#         self.eyes = 2
#     def breathe(self):
#         print(self.name+"正在呼吸")
#     def poop(self):
#         print(self.name+"正在大便")
# class Human(Mammal):
#     def read(self):
#         print(self.name+"正在阅读")
# class Dog(Mammal):
#     def sofa(self):
#         print(self.name+"正在抓沙发")
# Human1 = Human('coder729','male')
# print(Human1.name,Human1.sex,Human1.eyes)
# Human1.read()
# Dog1 = Dog('小狗','male')
# print(Dog1.sofa()
#print(Human1.read()) 会打印出 'coder729正在阅读'，但由于 read 方法没有返回任何值（即没有 return 语句），所以 print 也会打印出 None。
class Employee:
    def __init__(self,name):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"员工姓名：{self.name},工号是{self,id}")
class FulltimeEmployee(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    def calculate_salary(self):
        return self.salary
class ParttimeEmployee(Employee):
    def __init__(self,name,id,salary,workday):
        super().__init__(name,id)
        self.salary = salary
        self.workday = workday
    def calculate_salary(self):
        return self.salary * self.workday

coder729 = FulltimeEmployee("coder729",2010507103,5000)
coder728 = ParttimeEmployee("coder728",2010507104,3000,20)
print(coder729.calculate_salary())
print(coder728.calculate_salary())
