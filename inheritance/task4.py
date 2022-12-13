class TeamIterator:
    
    def __init__(self, team):
        juns = [f"('{x}', 'junior')" for x in team._juniorMembers]
        sens = [f"('{x}', 'senior')" for x in team._juniorMembers]
        self.team =  juns + sens
        self.index = -1

    def __next__(self):
        self.index += 1
        
        if self.index < len(self.team):          
            return self.team[self.index]
        else:
            raise StopIteration


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __len__(self):
        return len(self._juniorMembers + self._seniorMembers)

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()


# *** Итерируемся по команде в цикле for ***
# ('Ivan', 'junior')
# ('Mary', 'junior')
# ('Nikita', 'junior')
# ('Rita', 'senior')
# ('Roma', 'senior')
# ('Ramil', 'senior')
# *** Итерируемся по команде в цикле while ***
# ('Ivan', 'junior')
# ('Mary', 'junior')
# ('Nikita', 'junior')
# ('Rita', 'senior')
# ('Roma', 'senior')
# ('Ramil', 'senior')