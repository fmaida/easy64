import os


class Image():

    def __init__(self, filename=None):
        self.file = None
        self.name = None
        self.mode = None
        self.joyport = None
        self.video_format = None
        self.accurate_disk = ""
        self.read_only = ""
        self.set_mode_c64()
        self.set_mode_pal()
        self.set_joyport_2()
        self.set_accurate_disk(False)
        self.set_readonly(False)
        if filename:
            self.load(filename)

    def load(self, filename):
        self.file = filename
        if os.path.exists(self.file):
            temp = os.path.basename(self.file)
            self.name = os.path.splitext(temp)[0] 
        else:
            raise FileNotFoundError(self.file)
    
    def set_accurate_disk(self, enable=True):
        if enable:
            self.accurate_disk = "accuratedisk"
        else:
            self.accurate_disk = ""
    
    def set_readonly(self, enable=False):
        if enable:
            self.read_only = "readonly"
        else:
            self.read_only = ""
    
    def set_mode_c64(self):
        self.mode = "64"

    def set_mode_vic20(self):
        self.mode = "vic"
    
    def set_mode_pal(self):
        self.video_format = "pal"
    
    def set_mode_ntsc(self):
        self.video_format = "ntsc"

    def set_joyport_1(self):
        self.joyport = 1
    
    def set_joyport_2(self):
        self.joyport = 2

    def save_cjm(self):
        status = ""
        status += self.mode + ","
        status += self.video_format + ","
        status += self.accurate_disk + "," if self.accurate_disk != "" else ""
        status += self.read_only + "," if self.read_only != "" else ""
        breakpoint()
        if status[-1] == ",":
            status = status[0:-1]
        temp =  "X:" + status + "\r\n"
        temp += "J:1"
        if self.joyport == 1:
            temp += "*"
        temp += ":JU,JD,JL,JR,JF,JF,RS,SP,SP,RS,F1,F7,RS" + "\r\n"
        temp += "J:2"
        if self.joyport == 2:
            temp += "*"
        temp += ":JU,JD,JL,JR,JF,JF,RS,SP,SP,RS,F1,F7,RS" + "\r\n"
        my_path = os.path.dirname(self.file)
        my_path = os.path.join(my_path, self.name + ".cjm")
        f = open(my_path, "w")
        f.write(temp)
        f.close()
        return my_path