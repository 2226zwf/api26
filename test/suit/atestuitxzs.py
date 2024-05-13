import unittest
from test.case.user.test_xzs_reg import MyTestCase as regtest
from xzs.testcase.test_xzs_login import MyTestCase as logintest
from lib.HTMLTestRunner import HTMLTestRunner

class MyTestCase(unittest.TestCase):
    def test_suit(self):
        #创建一个测试套件
        suit = unittest.TestSuite()
        #添加单个用例
        suit.addTest(regtest("test_reg_ok"))
        #添加多个的测试用例
        suit.addTests([logintest("test_login_ok"),logintest("test_login_err1")])
        unittest.TextTestRunner(verbosity=2).run(suit)
    def test_makesuit(self):
        #makesuit 单个用例
        suit1 = unittest.makeSuite(regtest,"test_reg_ok")
        #会将整个测试方法都添加到suit2中
        suit2 = unittest.makeSuite(logintest)
        #将两个测试集 suit1 suit2集合成一个 suit5
        suit5 = unittest.TestSuite([suit1,suit2])
        #生成文本格式的测试报告
        with open("../../练习/result.txt", "w")as f:
            unittest.TextTestRunner(verbosity=2,stream=f).run(suit5)

    def test_loader(self):
        #loader 加载该测试类所有用例并生产测试集
        suit3 = unittest.TestLoader().loadTestsFromTestCase(logintest)
        #生成html格式的测试报告
        # t = time.strftime('%Y_%m_%d_%H_%M_%S')
        with open('../../report/report.html', 'wb')as f:
            HTMLTestRunner(
                stream=f,
                title='xzs登录',
                description='xzs登录例集',
                verbosity=2
            ).run(suit3)

    # def test_discover(self):
    #     suit4 = unittest.TestLoader().discover("./")
    #     unittest.TextTestRunner(verbosity=2).run(suit4)

if __name__ == '__main__':
    unittest.main()
