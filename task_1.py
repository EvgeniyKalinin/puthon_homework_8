def write_number():
    with open('numbers.txt', 'r') as numb:
        n = numb.read()
        print(n)

def find_contact():
    search = input('Введите параметр поиска -->   ')
    search = search.lower()
    count = 0
    with open('numbers.txt', 'r') as numb:
        for line in numb:
            list_1 = line
            list_1 = list_1.lower().split()
            
            for i in range(len(list_1)):
                if search == list_1[i]:
                    print(line)
                    count = 1
        if count == 0:
            print('\nКонтакт не найден')
         
def add_contact():
    new_list = []
    add_c = input('Введите Фамилию  -->   ')
    add_c = add_c.capitalize()
    new_list.append(add_c)
    new_list.append(' ')
    
    add_c = input('Введите Имя  -->   ')
    add_c = add_c.capitalize()
    new_list.append(add_c)
    new_list.append(' ')
    
    add_c = input('Введите Отчество  -->   ')
    add_c = add_c.capitalize()
    new_list.append(add_c)
    new_list.append(' -- ')
    
    add_c = input('Введите Номер телефона в формате < +7(999)111-22-33>  -->   ')
    add_c = add_c.capitalize()
    new_list.append(add_c)
    
    n = "".join(new_list)
    
    complite = int(input(f'\n\n {n}\n\n Данные введены верно? (если да введите <1>)\n -->   '))
    
    if complite == 1:
        with open('numbers.txt', 'a') as numb:
            numb.write(f'{n}\n')
        print(f"\n\n<Контакт {n} успешно добавлен>\n\n")
    else:
        print(f'Сохранение данных отменено')

def remove_contact():
    search = input('Введите параметр поиска -->   ')
    search = search.lower()
    count = 0
    list_change_remove = '$'
    with open('numbers.txt', 'r') as numb:
        for line in numb:
            list_1 = line
            list_1 = list_1.lower().split()
            
            for i in range(len(list_1)):
                if search == list_1[i]:
                    j = int(input(f'\nУдалить этот контакт<1> или продолжить поиск <0>?\n {line}\n -->   '))
                    if j == 1:
                        j_1 = int(input(f'\nТочно удалить контакт<1>\n -->'))
                        if j_1 == 1:
                            list_remove = line
                            count = 1
                            print('Контакт удален.')
                            break
                    count = 1
        if count == 0:
            print('\nКонтакт не найден')  
    with open('numbers.txt', 'r') as numb:
        
        list_1 = numb.readlines()
        for i in range(len(list_1)):
            if list_remove in list_1[i]:
                list_1.remove(list_1[i])
                break
    
    with open('numbers.txt', 'w') as numb_1:
        for line_1 in list_1:
            numb_1.write(f'{line_1}')

def change_contact():
    
    search = input('Введите параметр поиска -->   ')
    search = search.lower()
    count = 0
    count_save = 0
    fatal_count = 0
    list_change_remove = '$'
    with open('numbers.txt', 'r') as numb:
            for line in numb:
                list_1 = line
                list_1 = list_1.lower().split()
            
                for i in range(len(list_1)):
                    if search == list_1[i]:
                        j = int(input(f'\nИзменить этот контакт<1> или продолжить поиск <0>?\n {line}\n -->   '))
                        if j == 1:
                            list_change_remove = line
                            count = 1
                            break                            
                        
            if count == 0:
                print('\nКонтакт не найден')
                fatal_count = 1
                
                
    if fatal_count == 0:
        with open('numbers.txt', 'r') as numb:
           
            list_1 = numb.readlines()
            for i in range(len(list_1)- 1):
                if list_change_remove in list_1[i]:
                    list_1.remove(list_1[i])
                    
            new_list = []
            add_c = input('Введите Фамилию  -->   ')
            add_c = add_c.capitalize()
            new_list.append(add_c)
            new_list.append(' ')
    
            add_c = input('Введите Имя  -->   ')
            add_c = add_c.capitalize()
            new_list.append(add_c)
            new_list.append(' ')

            add_c = input('Введите Отчество  -->   ')
            add_c = add_c.capitalize()
            new_list.append(add_c)
            new_list.append(' -- ')
    
            add_c = input('Введите Номер телефона в формате < +7(999)111-22-33>  -->   ')
            add_c = add_c.capitalize()
            new_list.append(add_c)

            n = "".join(new_list)
    
            complite = int(input(f'\n\n {n}\n\n Данные введены верно? (если да введите <1>)\n -->   '))
              
            if complite == 1:
                    with open('numbers.txt', 'a') as numb:
                        numb.write(f'{n}\n')
                    print(f"\n\n<Контакт {n} успешно изменен>\n\n")
            else:
                print(f'Сохранение данных отменено')
                count_save = 1    
    
    if count_save == 0 and fatal_count == 0:
        with open('numbers.txt', 'w') as numb_1:
            for line_1 in list_1:
                numb_1.write(f'{line_1}')    
    
    
                 
  
        
      

while True:
    print('\nВыберите дейтвие:\n 1 -- Вывод телефонного справочника\n 2 -- Поиск по справочнику\n 3 -- Добавление контакта \n '
          '4 -- Удалить контакт\n 5 -- Изменить контакт\n 6 -- выход\n')
    wt = int(input())
    print()
    if wt == 1:
        write_number()
    elif wt == 2:
        find_contact()
    elif wt == 3:
        add_contact()
    elif wt == 4:
        remove_contact()
    elif wt == 5:
        change_contact()
    elif wt == 6:
        break
    
        
    
    