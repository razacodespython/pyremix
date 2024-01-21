# @version ^0.3.9

userCount: public(uint256)  # Counter for the number of users added
# Example of a fixed-size array
fixedNums: uint256[5]
dynamic_array: DynArray[uint256, 3]
dynamic_array_string: DynArray[String[100], 10]
#count: public(uint256)

@external
def addcount():
    self.userCount += 1

@external
def add_fixed_numberlist(_index:uint256, _value:uint256):
    self.fixedNums[_index] = _value
    #self.count +=1

@view
@external
def get_fixed_number(_index:uint256) -> uint256:
    return self.fixedNums[_index]

@view
@external
def getlengthdynamicarray() -> uint256:
    return len(self.dynamic_array)

#explain why this throws an error
#the len() function is not directly applicable as it would be in Python. The len() function in Vyper is primarily used for dynamic arrays, strings, and bytes types.
#In this case, since fixedNums is declared as uint256[5], its length is always 5. You can return this value directly without using the len() function.
# @view
# @external
# def getlengthfixedarray() -> uint256:
#     return len(self.fixedNums)

@external
def add_dynamic_array(_value:uint256):
    self.dynamic_array.append(_value)

@external
def remove_dynamic_array():
    self.dynamic_array.pop()

@view
@external
def get_dynamic_index(_index:uint256) -> uint256:
    return self.dynamic_array[_index]

@external
def add_string(_message:String[100]):
    self.dynamic_array_string.append(_message)

@view
@external
def get_message(_index:uint256) -> String[100]:
    return self.dynamic_array_string[_index]