import json,unittest,requests
import ddt
from lib import read_excl
from lib.case_log import log_case_info
from  config.config import *

def read():
    r = read_excl.readexcel()
    l = r.excel_to_list(data_file,"test_user_login")
    t = []
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    return t

@ddt.ddt()
class MyTestCase(unittest.TestCase):
    @ddt.data(*read())
    def test_login(self,name):
        r = read_excl.readexcel()
        l = r.excel_to_list(data_file,"test_user_login")
        t = r.get_test_data(l,name)
        url = t.get("url")
        data = t.get("args")
        d = json.loads(data)
        exp = t.get("expect_res")
        req = requests.post(url,json=d)
        log_case_info(name,url,d,exp,req.text)
        self.assertIn(exp,req.text)

    # @classmethod
    # def setUpClass(cls):
    #     cls.r = read_excl.readexcel()
    #     cls.l = cls.r.excel_to_list("test_user_data.xlsx","test_user_login")
    # @ddt.data("login_ok","login_err1","login_err2","login_err3")
    # def test_login(self,name):
    #     t = self.r.get_test_data(self.l,name)
    #     url =t.get("url")
    #     args = t.get("args")
    #     exp = t.get("expect_res")
    #     d = json.loads(args)
    #     r = requests.post(url,json=d)
    #     self.assertIn(exp,r.text)

# def readexceldata(filename):
#     book = xlrd.open_workbook(filename)
#     sheet1 = book.sheet_by_index(1)
#     rows = sheet1.nrows
#     datalist = []
#     for i in range(1,rows):
#         datalist.append(sheet1.row_values(i))
#     return datalist
#
# @ddt.ddt()
# class MyTestCase(unittest.TestCase):
#     @ddt.data(*readexceldata("./test_user_data.xlsx"))
#     @ddt.unpack
#
#     def test_login(self,url,args,expect_res):
#         r = requests.post(url=url,json=json.loads(args))
#         self.assertIn(expect_res,r.text)



if __name__ == '__main__':
    unittest.main()
