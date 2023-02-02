phonebook = {}
def process_add():
    surname = input('Введите фамилию\n')
    number = list(str(i) for i in input('Введите номера через пробел\n').split(' '))
    org = list(str(i) for i in input('Введите организации через пробелы\n').split(' '))
    add(name, number, surname, org)

def add(name, number, surname, org):
    phonebook[name] = {
        'surname': surname,
        'numbers': number,
        'organisations': org
    }

def rename(phonebook, newname, oldname):
    if oldname not in phonebook.keys():
        print('error')
    else:
        phonebook[newname] = phonebook[oldname]
        del phonebook[oldname]

def newdate(phonebook):
    name = input('Введите имя контакта\n')
    print(
        'Если хотите поменять фамилию - нажмите 1;\nЕсли хотите поменять номера - нажмите 2;\nЕсли хотите поменять организации - нажмите 3;\n')
    a = int(input())
    if a == 1:
        new_surname = input('Введите новую фамилию\n')
        phonebook[name]['surname'] = new_surname
    if a == 2:
        new_number = list(str(i) for i in input('Введите номера через пробел\n').split(' '))
        phonebook[name]['numbers'] = new_number
    if a == 3:
        new_org = list(str(i) for i in input('Введите организации через пробел\n').split(' '))
        phonebook[name]['organisations'] = new_org

def add_number_or_org(phonebook):
    name = input('Введите имя контакта\n')
    print('Если хотите добавить номер - нажмите 1;\nЕсли хотите добавить организацию - нажмите 2;\n')
    a = int(input())
    if a == 1:
        phonebook[name]['numbers'].append(str(input('Введите номер, который хотите добавить\n')))
    if a == 2:
        phonebook[name]['organisations'].append(str(input('Введите организацию, которую хотите добавить\n')))

def delete_contact(phonebook, oldname):
    if oldname not in phonebook.keys():
        print('error')
    else:
        del phonebook[oldname]

while True:
    print("""    Если хотите создать новый контакт - нажмите 1;
    Если хотите просмотреть текущую телефонную книгу - нажмите 2;
    Eсли хотите поменять данные контакта - нажмите 3;
    Если хотите изменить имя контакта - нажмите 4;
    Если хотите добавить номер или организацию - нажмите 5;
    Если хотите удалить контакт - нажмите 6;
    Если хотите завершить программу - нажмите 7;\n""")
    a = input()
    if a == '1':
        name = input('Введите имя контакта\n')
        process_add()
    if a == '2':
        print(phonebook)
    elif a == '3':
        newdate(phonebook)
    elif a == '4':
        oldname = input('Введите имя контакта, который хотите изменить\n')
        newname = input('Введите новое имя контакта\n')
        rename(phonebook, newname, oldname)
    elif a == '5':
        add_number_or_org(phonebook)
    elif a == '6':
        oldname = input('Введите имя контакта, который хотите удалить\n')
        delete_contact(phonebook, oldname)
    elif a == '7':
        break
    else:
        print("""           Х@₽ня полная
  !!!ERROR!!!!!!ERROR!!!!!!ERROR!!!
        Введите номер от 1 до 7""")