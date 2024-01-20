# @version ^0.3.9

# A contract to store and retrieve users' favorite numbers based on their usernames

# Variables
favoriteNumbers: public(HashMap[Bytes[50], uint256])  # Mapping of usernames to their favorite numbers
userNames: public(HashMap[uint256, Bytes[50]])  # Mapping of index to usernames
userCount: public(uint256)  # Counter for the number of users added

@external
def addLALAUser(_username: Bytes[50], _favoriteNumber: uint256):
    """
    Add a user with their username and favorite number.
    """
    self.favoriteNumbers[_username] = _favoriteNumber
    self.userNames[self.userCount] = _username
    self.userCount += 1

@view
@external
def getFavoriteNumber(_username: Bytes[50]) -> uint256:
    """
    Retrieve a user's favorite number by their username.
    """
    return self.favoriteNumbers[_username]

@view
@external
def getUserNameAtIndex(_index: uint256) -> Bytes[50]:
    """
    Get a user's username by index in the userNames array.
    """
    return self.userNames[_index]
