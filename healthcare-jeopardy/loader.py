class questions:
  answer = ''
  options = []
  question = ''
  points = 0
  category_name = ''
  category_id = 0
  selected = False 
      

def loadfile():
  question_map = {}
  f= open("JP.txt","r")   
  line = f.readline()
  while line:
    words = line.split('#')
    if len(words)==6:
      q = questions()
      q.category_id = words[0]
      q.category_name = words[1]
      q.points = words[2]
      q.question = words[3]
      q.options = words[4].split('|')
      q.answer = words[5].strip()
      question_map[q.category_id+'_'+ q.points]= q
    line = f.readline()
  f.close()
  return question_map
