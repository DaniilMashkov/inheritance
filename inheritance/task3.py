class MyList(list):


    def __init__(self, lst):
        print('Работает init')
        self.lst = lst

    def __getitem__(self, item):
        print ('Работает getitem')
        return self.lst[item]
    
    def __setitem__(self, key, value):
        print ('Работает setitem')
        self.lst[key] = value

    def __str__(self):
        print('Работает str')
        return f'{self.lst}'

    def __len__(self):
        print('Работает len')
        return len(self.lst)


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))