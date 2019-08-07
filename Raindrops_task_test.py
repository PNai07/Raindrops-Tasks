from Raindrops_task_main import Raindrops
# These are the testcases which have been created to test the program.
import pytest

def test1():
        assert Raindrops(1) =="1"

def test2(self):
        assert Raindrops(3) =="Pling"

def test3(self):
        assert Raindrops(5) =="Plang"

def test4(self):
        assert Raindrops(7) =="Plong"

def test5(self):
        assert Raindrops(6) =="Pling"

def test6(self):
        assert Raindrops(8) =="8"

def test7(self):
        assert Raindrops(9) =="Pling"

def test8(self):
        assert Raindrops(10), "Plang"

def test9(self):
        assert Raindrops(14), "Plong"

def test10(self):
        assert Raindrops(15) == "PlingPlang"

def test11(self):
        assert Raindrops(21) == "PlingPlong"

def test12(self):
        assert Raindrops(25) == "Plang"

def test13(self):
        assert Raindrops(27) == "Pling"

def test14(self):
        assert Raindrops(35) =="PlangPlong"

def test15(self):
        assert Raindrops(49) == "Plong"

def test16(self):
        assert Raindrops(52) =="52"

def test17(self):
        assert Raindrops(105) == "PlingPlangPlong"

def test18(self):
        assert Raindrops(1121) == "1121"

def test19 (self):
        assert Raindrops('a') =="Error, you may want to input an integer!"