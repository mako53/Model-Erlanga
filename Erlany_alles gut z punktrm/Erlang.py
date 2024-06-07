from math import factorial
from zasoby import precision, precision2

class Algorytm:

    def __init__(self, model):
        self.obj = model

    def get_obj_data(self):
        """
        Getting data from object
        :return: lines, traffic, blocking_rate
        """
        return self.obj.lines, self.obj.traffic, self.obj.blocking_rate

    def sprawdzanie(self):

        lines, traffic, block = self.get_obj_data()
        zmienne = [lines, traffic, block]
        '''
        if block is False:
            return self.calculate_erlang_p(traffic, lines)
        elif lines is False:
            return self.calculate_erlang_n(traffic, block)
        elif traffic is False:
            return self.calculate_erlang_a(lines, block)
        '''
        if zmienne[0] and zmienne[1] and not zmienne[2]:
            val1 = float(zmienne[0])
            val2 = int(zmienne[1])

            # sprawdzenie zakresów
            if (val1 <= 0 or val1 >= 200) or (val2 <= 1 or val2 >= 200):
                return 'wartość jest poza zakresem'
            else:
                return self.calculate_erlang_p(val2, val1)

        elif zmienne[0] and zmienne[2] and not zmienne[1]:
            val1 = float(zmienne[0])
            val3 = float(zmienne[2])

            # sprawdzenie zakresów
            if (val1 <= 0 or val1 >= 200) or (val3 <= 0 or val3 >= 1):
                return 'wartość jest poza zakresem'
            else:
                return self.calculate_erlang_a(val1, val3)

        elif zmienne[1] and zmienne[2] and not zmienne[0]:
            val2 = int(zmienne[1])
            val3 = float(zmienne[2])

            # sprawdzenie zakresów
            if (val2 <= 0 or val2 >= 200) or (val3 <= 0 or val3 >= 1):
                return 'wartość jest poza zakresem'
            else:
                return self.calculate_erlang_n(val2, val3)

    def calculate_erlang_p(self, traffic, lines):
        """
        Default erlang algorithm, calculate blocking rate
        :param traffic: the traffic in Erlangs
        :param lines: the number of lines
        :return: blocking rate
        """
        tab = [x for x in range(int(lines) + 1)]

        _sum = 0
        for idx, val in enumerate(tab):
            _sum += self.ann(idx, traffic)

        Pb = self.ann(int(lines), traffic) / _sum
        return round(precision2(Pb),3)

    def calculate_erlang_n(self, traffic, Pb):
        """
        calculate the number of lines in a trunk group
        :param traffic: the traffic in Erlangs
        :param Pb: blocking rate
        :return: number of lines
        """
        lines = 1
        p_search = Pb
        while float(p_search) >= Pb:
            lines += 1
            p_search = self.calculate_erlang_p(traffic, lines)

        #print(lines - 1)
        return lines

    def calculate_erlang_a(self, lines, Pb):
        """
        calculate traffic in erlangs
        :param lines: the number of lines
        :param Pb: blocking rate
        :return: traffic in erlangs
        """
        traffic = 0
        p_search = Pb
        while float(p_search) <= Pb:
            traffic += .1
            p_search = self.calculate_erlang_p(traffic, lines)
        #print(round(traffic, 2))
        return round(traffic, 3)


    def ann_small(self, n, a):
        """
        Default  a^n / n! algorithm for small numbers
        :param n: lines
        :param a: traffic
        :return: a^n / n!
        """
        exponent = a ** n
        b = factorial(n)
        return exponent/b

    def ann(self, n, a):
        """
        a^n / n! algorithm
        :param n: lines
        :param a: traffic
        :return: a^n / n!
        """
        result = 1
        for n in range(1, n + 1):
            result *= a / n

        return result
