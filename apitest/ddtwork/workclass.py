# from ddt import ddt,data,unpack,feed_data
# import unittest
#
#
# test_data=[{"username":"Admin","password":1234},{"username":"root","password":"mima"}]
# @ddt #装饰测试类
# class TestMath(unittest.TestCase):
#
#     @data(*test_data)  #装饰测试用例，拿到几个数据，执行几条用例
#     @unpack   #拿到的数据根据逗号区分  #s使用字典时，参数名和key必须对应
#     def test_prin(self,username,password):
#         print("item",username)
#
#     # def test_add(self):
#     #     a=10
#     #     b=20
#     #     print(a+b)
#
# if __name__ == '__main__':
#     unittest.main()


s='hello'
print(s.find('et'))
s.replace('el','ll')

print(s)