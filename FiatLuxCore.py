import ascii_engine as ag

s=ag.Screen()
print(s.display())

s.description[10]='hello world'+ag.space44[11:44]
s.display()

s.clean('description')
s.display()

s.clean('status')
s.display()

s.clean('scene')
s.display()