#@version ^0.3.9

balances: public(HashMap[String[100], uint256])

@external
def adduser(_user:String[100]):
    self.balances[_user] = 0

@view
@external
def getuser(_user:String[100]) -> uint256:
    return self.balances[_user]

@external
def set_balance(_user:String[100], _amount:uint256):
    self.balances[_user] = _amount