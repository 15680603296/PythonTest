import unittest

class MyTest_A(unittest.TestCase):
    """测试A"""
    #setUP和tearDown在每个用例执行时都会调用
    def setUp(self):
        print("test.初始化")
    #注意：测试用例必须以test开头，否则unittest不认为是测试用例
    def test_a(self):
        """测试a"""
        print("我是测试用例a!")
    def test_b(self):
        """测试b"""
        print("""我是测试用例b!""")
    def tearDown(self):
        print("test.清理")

if __name__ == '__main__':
    unittest.main()



