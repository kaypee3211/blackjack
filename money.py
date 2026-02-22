class money:

    def __init__(self, all, debt):
        self.all = all
        self.debt = 0
    def addDebt(self,debtValue):
        self.all += debtValue
        self.debt += debtValue
    def payOffDebt(self,debtValue):
        self.debt -= debtValue
        self.all -= debtValue
