#Macros
##space sequences
space44='                                            '
space32='                                '
##ANSI escape codes
esc='\x1b['
##Foreground colors
F_black=esc+'30m'
F_red=esc+'31m'
F_green=esc+'32m'
F_yellow=esc+'33m'
F_blue=esc+'34m'
F_magenta=esc+'35m'
F_cyan=esc+'36m'
F_white=esc+'37m'
##Background colors
B_black=esc+'40m'
B_red=esc+'41m'
B_green=esc+'42m'
B_yellow=esc+'43m'
B_blue=esc+'44m'
B_magenta=esc+'45m'
B_cyan=esc+'46m'
B_white=esc+'47m'

class Screen: #The result of the rendering

    def __init__(self):
        #Two ASCII letters form a pixel.A 25*80 terminal has 25*(80/2) pixels. 
        self.description=list() # 22*22 pixels
        for i in range(22):
            self.description.append(F_black+B_white+space44)
        self.description[10]='\x1b[30;47mInilitializing...                           '
        self.description[11]='\x1b[30;47mThis is a description                       '
        
        self.scene=list() # 16*16 pixels
        for i in range(16):
            self.scene.append(F_white+B_blue+space32)
        self.scene[7]='\x1b[37;44mThis is a scene                 '
        
        self.status=list() # 5*16 pixels
        for i in range(5):
            self.status.append(F_red+B_white+space32)
        self.status[2]='\x1b[31;47mThis is a status bar            '

    def display(self):
        frame_color='\x1b[30;47m'
        line=frame_color+'|'
        print(frame_color+'===============================================================================')
        for i in range(16):
            print(line+self.description[i]+line+self.scene[i]+line)
        print(line+self.description[16]+line+'================================'+line)
        for i in range(17,22):
            print(line+self.description[i]+line+self.status[i-17]+line)
        print(frame_color+'===============================================================================')
        return input('Your command:')

    def clean(self,block): #clean description, scene or status bar.
        if block=='description':
            for i in range(22):
                self.description[i]=F_black+B_white+space44
        elif block=='scene':
            for i in range(16):
                self.scene[i]=F_black+B_white+space32
        elif block=='status':
            for i in range(5):
                self.status[i]=F_black+B_white+space32
        else:
            return False
        return True

    def render(self,block,data): #render description,scene or status.
        if block=='description':
            self.description=data
        elif block=='scene':
            self.scene=data
        elif block=='status':
            self.status=data
        else:
            return False
        return True