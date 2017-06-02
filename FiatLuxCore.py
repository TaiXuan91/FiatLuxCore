import ascii_engine as ag
import scene 

gamemode='normal' # normal,script,god...
d,t=ag.display_prepare('Fallout is a series of post-apocalyptic retrofuturistic role-playing video games. It was created by Interplay Entertainment. Although the series is set during the 22nd and 23rd centuries, its \natompunk retrofuturistic setting and artwork are influenced by the post-war culture of 1950s America, and its combination of hope for the promises of tec\nhnology, and lurking fear of nuclear annihilation. A forerunner for Fallout is Wasteland, a 1988 video game of which the Fallout series is regarded to be a spiritual successor. Although the game worlds are different, the background story, inhabitants, locations, and characters draw many parallelsThe first two titles in the series, Fallout and Fallout 2, were developed by Black Isle Studios. Micro Fort and 14 Degrees Easts 2001 Fallout Tactics: Brotherhood of Steel is a tactical role-playing game. In 2004, Interplay closed Black Isle Studios,[1] and continued to produce an action game with role-playing elements for the PlayStation 2 and Xbox, Fallout: Brotherhood of Steel without Black Isle Studios. A third entry in the main series, Fallout 3, was released in 2008 by Bethesda Softworks. It was followed by Fallout: New Vegas in 2010, developed by Obsidian Entertainment. Fallout 4 was announced on June 3, 2015, and was released on November 10, 2015.Bethesda Softworks owns the rights to produce Fallout games.[2] Soon after acquiring the rights to the intellectual property (IP), Bethesda licensed the rights to make a massively multiplayer online role-playing game (MMORPG) version of Fallout to Interplay. The MMORPG got as far as beta stage under Interplay,[3] but a lengthy legal dispute between Bethesda Softworks and Interplay halted the development of the game and led to its eventual cancellation, as Bethesda claimed in court that Interplay had not met the terms and conditions of the licensing contract. The case was decided in favor of Bethesda.[4]')
x=ag.display(d)
if x!=None:
    compile(x,filename='command',mode='eval')
    gamemode=eval(x)
d,t=ag.display_prepare(t)
ag.display(d)
#s=ag.Screen()
#print(s.display())

#s.description[10]='hello world'+ag.space44[11:44]
#s.display()

#s.clean('description')
#s.display()

#s.clean('status')
#s.display()

#s.clean('scene')
#s.display()
#a=scene.Scene(3,7)
#print(a.space2d)

#b=scene.Scene(0,0)
#for x in b.space2d:
#    print(x)