import math
from Erlang import Algorytm

class Model:
    """
    Model for ErlangB algorithm

    traffic         = the traffic in Erlangs
    lines           =  the number of servers(lines) in a trunk group
    blocking_rate   = Probability of blocking
    sources         = the number of points generating the traffic
    """

    def __init__(self, traffic=None, lines=None, blocking_rate=None, sources=None):
        self._block = 0.1
        self._users = None
        self.lines = lines
        self.blocking_rate = blocking_rate
        self.traffic = traffic
        self.sources = sources

    def calculate_traffic_per_hour(self, calls, duration, seconds=True):
        """ Calculate the total traffic volume of one hour.
        :param calls: amount of calls made in hour
        :param duration: average duration time in seconds or minutes
        :param seconds: If duration in seconds set True, if in minutes set as False
        :return: Erlang traffic representation
        """
        unit = 3600 if seconds else 60
        self.traffic = calls * duration / unit

    def calculate_traffic_per_user(self, user, block):
        self.traffic = user * block

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self.traffic = value * self.block if value else False
        self._users = value

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self.traffic = value * self.users if value else False
        self._block = value

    def validate_data(self):
        tab = [self.traffic, self.lines, self.blocking_rate]
        for val in tab:
            if val is None:
                raise ValueError("This field can't be empty")

    def calculate_erlang(self):
        """
        Erlang algorithm

        :return: traffic / lines / blocking_rate
         dependence which value is equal False
        """
        self.validate_data()
        return Algorytm(self).sprawdzanie()

if __name__ == '__main__':
    model = Model()
    model.traffic = 3.4
    model.lines = 10
    model.sources = 500
    model.blocking_rate = False
    print(model.calculate_erlang())
