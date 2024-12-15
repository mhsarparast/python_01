import re
class Account:
    def __init__(self, title, account_id,ammount):
        self.title = title
        self.account_id = account_id
        self.ammount = ammount
    def __repr__(self):
        return str(self.__dict__)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
    @property
    def account_id(self):
        return self._account_id
    @account_id.setter
    def account_id(self, value):
        if re.match(r'6104\d{12}', value):
            self._account_id = value
        else:
            raise ValueError('Account ID is not valid')
    @property
    def ammount(self):
        return self._ammount
    @ammount.setter
    def ammount(self, value):
        if value>=0:
            self._ammount = value
        else:
            raise ValueError('Amount cannot be negative')