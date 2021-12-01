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
