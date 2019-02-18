from colorama import init,Fore
import ctypes

class ColorPrint(object):
    def __init__(self):
        self.STD_OUTPUT_HANDLE= -11
        self.FOREGROUND_RED = 0x04
        self.FOREGROUND_BLUE = 0x01 # 蓝
        self.FOREGROUND_GREEN = 0x02
        self.FOREGROUND_INTENSITY = 0x08
        self.std_out_handle = ctypes.windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE)

    def set_cmd_color(self, color):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(self.std_out_handle, color)  
        return bool

    def Reset(self):
        self.set_cmd_color(self.FOREGROUND_RED|self.FOREGROUND_GREEN|self.FOREGROUND_BLUE)

    def RedPrint(self,text):
        self.set_cmd_color(self.FOREGROUND_RED|self.FOREGROUND_INTENSITY)
        print(text)
        self.Reset()
RedPrint = ColorPrint().RedPrint