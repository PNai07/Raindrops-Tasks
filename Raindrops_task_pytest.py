from Raindrops_task_main import Raindrops

class RaindropsTest_pytest():
    def test1(self):
        self.assertEqual(Raindrops(1),"1")

    def test2(self):
        self.assertEqual(Raindrops(3),"Pling")

    def test3(self):
        self.assertEqual(Raindrops(5), "Plang")

    def test4(self):
        self.assertEqual(Raindrops(7), "Plong")

    def test5(self):
        self.assertEqual(Raindrops(6), "Pling")

    def test6(self):
        self.assertEqual(Raindrops(8), "8")

    def test7(self):
        self.assertEqual(Raindrops(9), "Pling")

    def test8(self):
        self.assertEqual(Raindrops(10), "Plang")

    def test9(self):
        self.assertEqual(Raindrops(14), "Plong")

    def test10(self):
        self.assertEqual(Raindrops(15), "PlingPlang")

    def test11(self):
        self.assertEqual(Raindrops(21), "PlingPlong")

    def test12(self):
        self.assertEqual(Raindrops(25), "Plang")

    def test13(self):
        self.assertEqual(Raindrops(27), "Pling")

    def test14(self):
        self.assertEqual(Raindrops(35), "PlangPlong")

    def test15(self):
        self.assertEqual(Raindrops(49), "Plong")

    def test16(self):
        self.assertEqual(Raindrops(52), "52")

    def test17(self):
        self.assertEqual(Raindrops(105), "PlingPlangPlong")

    def test18(self):
        self.assertEqual(Raindrops(1121), "1121")