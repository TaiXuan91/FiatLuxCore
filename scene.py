# Macros
## Directions
north=+1
south=-1
east=+1
west=-1


class Scene:
    def __init__(self,ns,ew): # ew:east-west length,ns:north-south length
        if ns<=0 or ew <=0: # ns and ew should be bigger than 0.
            ns=16
            ew=16
        self.space2d=list()
        for i in range(ns):
            self.space2d.append(list())
            for j in range(ew):
                self.space2d[i].append(None)
