from termcolor import colored
from loader import loadfile
x= ''
y= ''
o='0'
p='0'
z='0'
a=0
k=''
n=0
qmap={}
catpoints =[100,200,300,400,500]
def art():
  print(colored('    _____ ________   ___   _______    _     _______    ______   ____  ____  ','blue'))
  print(colored('   |_   _|_   __  |.\'   `.|_   __ \\  / \\    |_   __ \\  |_   _ `.|_  _||_  _| ','yellow'))
  print(colored('     | |   | |_ \\_/  .-.  \\ | |__) |/ _ \\     | |__) |   | | `. \\ \\ \\  / /   ','blue'))
  print(colored(' _   | |   |  _| _| |   | | |  ___// ___ \\    |  __ /    | |  | |  \\ \\/ /    ','yellow'))
  print(colored('| |__\' |  _| |__/ \\  `-\'  /_| |_ _/ /   \\ \\_ _| |  \\ \\_ _| |_.\' /  _|  |_    ','blue'))
  print(colored('`.____.\' |________|`.___.\'|_____|____| |____|____| |___|______.\'  |______|   ','yellow'))
  print(colored('  _  _          _ _   _       ___                ___    _ _ _   _           ','blue'))
  print(colored(' | || |___ __ _| | |_| |_    / __|__ _ _ _ ___  | __|__| (_) |_(_)___ _ _   ','yellow'))
  print(colored(' | __ / -_) _` | |  _| \' \\  | (__/ _` | \'_/ -_) | _|/ _` | |  _| / _ \\ \' \\  ','blue'))
  print(colored(' |_||_\\___\\__,_|_|\\__|_||_|  \\___\\__,_|_| \\___| |___\\__,_|_|\\__|_\\___/_||_| ','yellow'))

def points(q):
  if q.selected == True:
    return colored('XXX', 'red')
  else:
    return colored(q.points, 'green')
def grid2():
  global qmap
  qlist = list(qmap.values())
  
  print(colored(' ============= =================== =============== =================== ============= ', 'blue'))
  print(colored('| Wild Card(1)| Diet/Conditions(2)| Food Groups(3)| Nutrient Groups(4)| Symptoms(5) |', 'green'))
  print(colored('|=============|===================|===============|===================|=============|', 'blue'))
  num = 0
  for i in range(0,5): 
    print('|      '+ points(qlist[num])+'    |        '+points(qlist[num+5])+'        |     '+points(qlist[num+10])+'       |       '+points(qlist[num+15])+'         |     '+points(qlist[num+20])+'     |')
    print(colored(' ============= =================== =============== =================== ============= ', 'blue'))
    num = num+1


def displayscore():
  global x
  global y
  global o
  global p
  print(colored('======================================================', 'yellow' ))
  print(colored('|                    SCORE SUMMARY                   |', 'yellow' ))
  print(colored('======================================================', 'yellow' ))
  print(colored('|                     '+ x+' : '+o+ '                   |', 'yellow' ))
  print(colored('|                     '+ y+' : '+p+ '                   |', 'yellow' ))
  print(colored('======================================================', 'yellow' ))
def pickchoice(name):
  global z
  global a  
  global qmap
  inputs(name)
  qu = qmap[z+'_'+a]
  while(qu.selected):
    print(colored('This question has already been selected, please choose again.', 'red'))
    inputs(name)
    qu = qmap[z+'_'+a]

  return qu  
def inputs(name):
  global z
  global a
  z=input(name+', pick a category (1,2,3,4 or 5): ')
  while (int(z) < 1 or int(z) > 5):
    print(colored('Invalid category chosen. Please enter again.', 'red'))
    z=input(name+', pick a category (1,2,3,4 or 5): ')

  a=str(input(name+', pick a points value(100,200,300,400,500): '))
  while(int(a) not in catpoints):
    print(colored('Invalid points chosen. Please enter again.', 'red'))
    a=str(input(name+', pick a dollar value(100,200,300,400,500): '))
 
def playersturn2(name,score):
  global z
  global a
  global qmap
  qu = pickchoice(name)
  print(qu.question.strip())
  for option in qu.options:
    print(option)
  b=input()
  if b.lower() == qu.answer:
    print(colored('\U0001F44d Correct!\U0001f600', 'green'))
    score=str(int(score)+int(a))
    qu.selected = True
    grid2()
  else:
    print(colored('\U0001F44e Incorrect. \U0001f61e' + ' The correct answer is ' + qu.answer ,'red'))
    score=str(int(score)-int(a))
    qu.selected = True
    grid2()
  return (score)

art()
qmap = loadfile()
grid2()
x= str(input('What is Player 1s name?: '))
y= str(input('What is Player 2s name?: '))
m=int(input('How many rounds would you like to play?: '))
o='0'
p='0'
displayscore()
for i in range(0,m):
  o=playersturn2(x,o)
  displayscore()
  p=playersturn2(y,p)
  displayscore()
if int(o)>int(p):
  print(colored("Congratulations "+ x + "!! \U0001f3c6 You are the winner of JEOPARDY Health Care Edition.", 'cyan'))
elif int(o)<int(p):
  print(colored("Congratulations "+ y + "!! \U0001f3c6 You are the winner of JEOPARDY Health Care Edition.", 'cyan'))
else:
  print(colored("There is no winner. Both players tied!", 'yellow'))
a= input('Press any key to exit the game')