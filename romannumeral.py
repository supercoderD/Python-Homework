class RomanConverter:
    def __init__(self, number):
        self.number = number
        self.romanmap = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        
        
    def roman(self):
        result = ""
        numtoconvert = self.number

        for value, symbol in self.romanmap:
            while numtoconvert >= value:
                result += symbol
                numtoconvert -= value 
        return result

mynumber = RomanConverter(1994)
print(f"{mynumber.number} in Roman numerals is: {mynumber.roman()}")

number2 = RomanConverter(45)
print(f"{number2.number} in Roman numerals is: {number2.roman()}")