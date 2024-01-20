# @version ^0.3.9

userCount: public(uint256)  # Counter for the number of users added
@external
def addcount():
    self.userCount += 1