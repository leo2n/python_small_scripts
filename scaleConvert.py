"""
这个类的主要目的是, 转换数字的进制, 并将它们显示出来
"""

class ScaleConvert:
    """
    
    """
    def __init__(self, num):
        self.num = num
        pass
    
    def convert(self):
        if self.num[:2].lower() == "0x":
            self.hexShow(self.num)
        elif self.num[:2].lower() == "0o":
            self.octShow(self.num)
        elif self.num[:2].lower() == "0b":
            self.binShow(self.num)
        else:
            print("无需转换")
    
    def hexShow(self, num):
        hexNum = num[2:]
        print("{}的十进制是:{}".format(num, int(hexNum, base=16)))
        print("{}的八进制是:{}".format(num, oct(int(hexNum, base=16))))
        print("{}的二进制是:{}".format(num, bin(int(hexNum, base=16))))
    
    def octShow(self, num):
        octNum = num[2:]
        print("{}的十六进制是:{}".format(num, hex(int(octNum, base=8))))
        print("{}的十进制是:{}".format(num, int(octNum, base=8)))
        print("{}的二进制是:{}".format(num, bin(int(octNum, base=8))))

    def binShow(self, num):
        binNum = num[2:]
        print("{}的十六进制是:{}".format(num, hex(int(binNum, base=2))))
        print("{}的十进制是:{}".format(num, int(binNum, base=2)))
        print("{}的八进制是:{}".format(num, oct(int(binNum, base=2))))

if __name__ == "__main__":
    try:
        while True:
            x = input("请输入要转换的数字:")
            s = ScaleConvert(x)
            if x == "break":
                break
            s.convert()
    except:
        print("意外情况发生, 程序退出!")
