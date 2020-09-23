from least import least_class
class run:

    def testcase(self):

        s=least_class(4)

        s.put("flipkart")
        assert s.get("flipkart")!=None, "testcase1 failed"
        print("testcase1 passed successfully")

        s.put("nykaa")
        assert s.get("nykaa")!= None, "testcase1 failed"
        print("testcase1 passed successfully")

        s.put("amazon")
        assert s.get("amazon")!= None, "testcase1 failed"
        print("testcase1 passed successfully")

        s.put("flipkart")
        assert s.get("flipkart")!= None, "testcase1 failed"
        print("testcase1 passed successfully")

        s.put("shopclues")
        assert s.get("shopclues")!= None, "testcase1 failed"
        print("testcase1 passed successfully")

        print("All test cases passes successfully")

        least = s.get_cache()
        for i in least:
            print(i)

s=run()
s.testcase()
