# Macros
## Setting
display_color=True
screen_width=80-1 #the last one for '\n'
screen_height=25-1 #the last one for input command

## Colors. Colorful by default.
### ANSI escape codes
esc='\x1b['
### Foreground colors
F_black=esc+'30m'
F_red=esc+'31m'
F_green=esc+'32m'
F_yellow=esc+'33m'
F_blue=esc+'34m'
F_magenta=esc+'35m'
F_cyan=esc+'36m'
F_white=esc+'37m'
### Background colors
B_black=esc+'40m'
B_red=esc+'41m'
B_green=esc+'42m'
B_yellow=esc+'43m'
B_blue=esc+'44m'
B_magenta=esc+'45m'
B_cyan=esc+'46m'
B_white=esc+'47m'

def open_color():
    ### ANSI escape codes
    esc='\x1b['
    ### Foreground colors
    F_black=esc+'30m'
    F_red=esc+'31m'
    F_green=esc+'32m'
    F_yellow=esc+'33m'
    F_blue=esc+'34m'
    F_magenta=esc+'35m'
    F_cyan=esc+'36m'
    F_white=esc+'37m'
    ### Background colors
    B_black=esc+'40m'
    B_red=esc+'41m'
    B_green=esc+'42m'
    B_yellow=esc+'43m'
    B_blue=esc+'44m'
    B_magenta=esc+'45m'
    B_cyan=esc+'46m'
    B_white=esc+'47m'

def close_color():
    ### ANSI escape codes
    esc=''
    ### Foreground colors
    F_black=esc+''
    F_red=esc+''
    F_green=esc+''
    F_yellow=esc+''
    F_blue=esc+''
    F_magenta=esc+''
    F_cyan=esc+''
    F_white=esc+''
    ### Background colors
    B_black=esc+''
    B_red=esc+''
    B_green=esc+''
    B_yellow=esc+''
    B_blue=esc+''
    B_magenta=esc+''
    B_cyan=esc+''
    B_white=esc+''

def return_space(n): #return a string of n sapces
    s=''
    for i in range(n):
        s+=' '
    return s

def display_prepare(text): #return the data to display.text is a string.
    data=list()
    for i in range(screen_height):
        if i==0:
            s=''
            for j in range(screen_width):
                s+='-'
            data.append(s)
        elif i<screen_height-1:
            s=''
            s+='|'
            for j in range(screen_width-2): # -2 for two '|' each side of screen
                if len(text)<=j:
                    l= screen_width-1-len(s)
                    s+=return_space(l)
                    text=''
                    break
                ch=text[j]
                if ch!='\r' and ch!='\n':
                    s+=ch
                else:
                    text=text[j+1:]
                    break
            else:
                text=text[j+1:]
            if len(s)<screen_width-1:
                l= screen_width-1-len(s)
                s+=return_space(l)
            s+='|'
            data.append(s)
        else:
            s=''
            for j in range(screen_width):
                s+='-'
            data.append(s)

    return data,text # also return the text that is not yet displayed


def display(data,hint='Your Command:'): #display data and return a cmd string
    for s in data:
        print(s)
    return input(hint)




#class Screen_old: #The result of the rendering

#    def __init__(self):
        #Two ASCII letters form a pixel.A 25*80 terminal has 25*(80/2) pixels. 
#        self.description=list() # 22*22 pixels
#        for i in range(22):
#            self.description.append(F_black+B_white+space44)
#       self.description[10]=F_black+B_white+'Inilitializing...                           '
#      self.description[11]=F_black+B_white+'This is a description                       '

#        self.buffer_des=list() # A buffer for description.
#        self.buffer.append(self.description)
        
#        self.scene=list() # 16*16 pixels
#        for i in range(16):
#            self.scene.append(F_white+B_blue+space32)
#        self.scene[7]=F_white+B_blue+'This is a scene                 '
#        
#        self.status=list() # 5*16 pixels
#        for i in range(5):
#            self.status.append(F_red+B_white+space32)
#        self.status[2]=F_red+B_white+'This is a status bar            '

#    def display(self):
#        frame_color=F_black+B_white
#        line=frame_color+'|'
#        print(frame_color+'===============================================================================')
#        for i in range(16):
#            print(line+self.description[i]+line+self.scene[i]+line)
#        print(line+self.description[16]+line+'================================'+line)
#        for i in range(17,22):
#            print(line+self.description[i]+line+self.status[i-17]+line)
#        print(frame_color+'===============================================================================')
#        return input()

#    def clean(self,block): #clean description, scene or status bar.
#        if block=='description':
#            for i in range(22):
#                self.description[i]=F_black+B_white+space44
#        elif block=='scene':
#            for i in range(16):
#                self.scene[i]=F_black+B_white+space32
#        elif block=='status':
#            for i in range(5):
#                self.status[i]=F_black+B_white+space32
#        else:
#            return False
#        return True

#    def update(self,block,data): # update description,scene or status with data.
#        if block=='description':
#            self.description=data
#        elif block=='scene':
#            self.scene=data
#        elif block=='status':
#            self.status=data
#        else:
#            return False
#        return True

#    def render_text(s): # render string s,and display.
#        sx=s.splitlines()
#        page={}
#        while len(page)<=22:
            
