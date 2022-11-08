import random
import sys
class СA:
    def __init__(self, X, Y, prosent):
        self.__X = X
        self.__Y = Y
        self.__prosent = prosent
        field = [[0] * X for i in range(Y)]
        self.__field = field

    @property
    def field(self):
        return self.__field

    @property
    def X(self):
        return self.__X
    @X.setter
    def X(self, val):
        if val < 0:
            print('Ошибка')
        else:
            self.__X = val

    @property
    def Y(self):
        return self.__Y
    @Y.setter
    def Y(self, val):
        if val < 0:
            print('Ошибка')
        else:
            self.__Y = val

    @property
    def prosent(self):
        return self.__prosent
    @prosent.setter
    def prosent(self, val):
        if val < 0 or val > 100:
            print('Ошибка')
        else:
            self.__prosent = val

    def apdate(self,сa):
        for i in range(0, self.__X):
            for j in range(0, self.__Y):
                if random.randint(1,100) <= self.__prosent:
                    self.__field[j][i] = 1
        display(self.__field)

        while True:
            move = input('Введите любую клавишу, чтобы продолжить или (-) чтобы закончить: ')
            self.__buffer = [[0] * self.__X for i in range(self.__Y)]
            сa.neighbours()
            display(self.__buffer)
            self.__field = self.__buffer
            if move =='-':
                break

    def neighbours(self):
        for i in range(0, self.__X):
            for j in range(0, self.__Y):
                s=0
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if (n==i and m==j) or n==-1 or m==-1 or n==self.__X or m==self.__Y:
                            continue
                        elif self.__field[m][n] == 1:
                            s+=1

                if self.__field[j][i] == 1:
                    if s == 2 or s == 3:
                        self.__buffer[j][i] = 1
                    else:
                        self.__buffer[j][i] = 0
                elif self.__field[j][i] == 0:
                    if s == 3:
                        self.__buffer[j][i] = 1
                    else:
                        self.__buffer[j][i] = 0

class DLA(СA):
    def __init__(self,X,Y,prosent):
        super().__init__(X,Y,prosent)

    def apdate(self,сa):
        self.__field = self.field
        self.__X = self.X
        self.__Y = self.Y
        self.__prosent = self.prosent
        self.__field[(self.__Y//2)][self.__X//2] = 1
        display(self.__field)
        number_cells = 1
        while number_cells / (self.__X * self.__Y) * 100 < self.__prosent:
            number_cells = 0
            for i in range(0, self.__X):
                for j in range(0, self.__Y):
                    if self.__field[j][i] == 1:
                        number_cells += 1
            while True:
                X1 = random.randint(0, self.__X - 1)
                Y1 = random.randint(0, self.__Y - 1)
                if self.__field[Y1][X1] == 0:
                    self.__field[Y1][X1] = '*'
                    display(self.__field)
                    break
            while self.__field[Y1][X1] != 1:
                self.__field[Y1][X1] = 0
                сa.neighbours(Y1, X1)

                if self.__field[Y1][X1] != 1:
                    k = random.randint(0, 3)
                    if k == 0:
                        Y1 -= 1
                    elif k == 1:
                        X1 -= 1
                    elif k == 2:
                        Y1 += 1
                    elif k == 3:
                        X1 += 1
                    if X1 == -1 or Y1 == -1 or X1 == self.__X or Y1 == self.__Y:
                        display(self.__field)
                        break
                    else:

                        self.__field[Y1][X1] = '*'

                display(self.__field)

    def neighbours(self,Y1,X1):
        for n in range(X1 - 1,X1 + 2):
            for m in range(Y1 - 1, Y1 + 2):
                if n == -1 or m == -1 or n == self.__X or m == self.__Y or (n!= X1 and m != Y1):
                    continue
                elif self.__field[m][n] == 1:
                    self.__field[Y1][X1] = 1
                    break

def display(field):
        for i in range(0, len(field)):
            for j in range(0, len(field[i])):
                print(field[i][j], end=' ')
            print()
        print()

def main():
#    сa1 = СA(5, 5, 50)
 #   сa1.apdate(сa1)
   dla1 = DLA(5,5,50)
   dla1.apdate(dla1)

main()
