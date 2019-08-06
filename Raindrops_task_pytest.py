from Raindrops_task_main import Raindrops

class RaindropsTest_pytest():
    def test1(self):
        self.assertEqual(Raindrops(1),"1")

    def test2(self):
        self.assertEqual(Raindrops(2),"Pling")

    def test3(self):
        self.assertEqual(Raindrops(3), "Plang")

    def test4(self):
        self.assertEqual(Raindrops(4), "Plong")

    def test5(self):
        self.assertEqual(Raindrops(5), "Pling")

    def test6(self):
        self.assertEqual(Raindrops(6), "Pling")

    def test7(self):
        self.assertEqual(Raindrops(7), "Plang")

    def test8(self):
        self.assertEqual(Raindrops(10), "Plong")

    def test9(self):
        self.assertEqual(Raindrops(14), "PlingPlang")

    def test10(self):
        self.assertEqual(Raindrops(15), "PlingPlong")

    def test11(self):
        self.assertEqual(Raindrops(17), "Plang")

    def test12(self):
        self.assertEqual(Raindrops(20), "PlangPlong")

    def test13(self):
        self.assertEqual(Raindrops(30), "Plong")

    def test14(self):
        self.assertEqual(Raindrops(34), "34")