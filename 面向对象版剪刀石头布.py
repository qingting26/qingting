import random


class Computer:
    def __init__(self):
        self.fist = None

    def action(self):
        self.fist = random.randint(0, 3)


class Person:
    def __init__(self):
        self.fist = None

    def action(self):
        self.fist = int(input('请你出拳'))


class Judge:
    def judge(self, person: Person, com: Computer):
        if person.fist == com.fist:
            print('平局')
        elif person.fist - com.fist == 1 and person.fist > com.fist or person.fist - com.fist == -2:
            print('人类胜利')
        else:
            print('电脑胜利')
if __name__=='__main__':
    p=Person()
    c=Computer()
    j=Judge()
    while True:
        p.action()
        c.action()
        j.judge(p,c)

