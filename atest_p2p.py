import unittest,requests


class MyTestCase(unittest.TestCase):
    url ="http://192.168.55.55:8080/p2p_management/addProduct"

    def test_goods_ok(self):
        if check_product("66"):
            del_product("66")
            data = {"proNum":"66","proName":"66","proLimit":"66","annualized":"66"}
            r = requests.post(url=self.url, json=data)
            self.assertNotIn('失败',r)

    def test_goods_err(self):
        if not check_product('66'):
            add_product('66','66',66,66)
        data = {"proNum":"","proName":"66","proLimit":"66","annualized":"66"}
        r = requests.post(url=self.url, json=data)
        self.assertIn('400',r.text)




if __name__ == '__main__':
    unittest.main()
