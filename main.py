#TASK 1
print('1)Create a new file\n2)Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3\nEnter 0 to quit')

def create():
  with open ('Subject.txt','w') as file:
    new_subject=input('Введите новый предмет')
    file.write(new_subject+'\n')
  return 'Успешно создано'

def show():
  with open ('Subject.txt','r') as file:
    lines=file.read()
  return f'В файле находится: {lines}'

def add():
  with open ('Subject.txt','r') as file:
    lines=file.read()
  with open ('Subject.txt','w') as file:
    new_subject=input()
    lines+=new_subject+'\n'
    file.write(lines)
  return f'{lines}\nУспешно добавлено'

while True:
  variants=[0,1,2,3]
  user=int(input())
  if user not in variants:
    print('Make a selection 1, 2 or 3')
  elif user==1:
    print(create())
  elif user==2:
    print(show())
  elif user==3:
    print(add())
  elif user==0:
    print('Bye!')
    break

#TASK 2
seti  = [{"interface": "Ethernet0", "ip": "1.1.1.1", "status": "up"},
{"interface": "Ethernet1", "ip": "2.2.2.2", "status": "down"},
{"interface": "Serial0", "ip": "3.3.3.3", "status": "up"},
{"interface": "Serial1", "ip": "4.4.4.4", "status": "up"}]
print(len(seti))
print (f"Название: {seti[1]['interface']}, IP: {seti[1]['ip']}, Статус: {seti[1]['status']}")

#TASK 3
def addition():
  from random import randint
  a=randint(5,20)
  b=randint(5,20)
  print(f'{a} + {b} = ')
  user=int(input('Ваш ответ: '))
  return f'правильный ответ - {a+b}, ваш ответ - {user}, {correct(a+b,user)}'
addition()
def correct(i,j):
  if i==j:
    return 'correct'
  else:
    return 'incorrect'

def subtraction():
  from random import randint
  a=randint(1,25)
  b=randint(25,50)
  print(f'{b} - {a} = ')
  user=int(input('Ваш ответ: '))
  return f'правильный ответ - {b-a}, ваш ответ - {user}, {correct(b-a,user)}'
subtraction()