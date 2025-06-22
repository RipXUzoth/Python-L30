class RomanConverter:
    def __init__(self, number):
        self.number = number
        self.roman_numeral = ""
    def convert_to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
        num = self.number
        roman = ""
        for i in range(len(val)):
            count = int(num / val[i])
            roman += syms[i] * count
            num -= val[i] * count
        self.roman_numeral = roman
        return roman
    def display(self):
        print(f"integer: {self.number} --> Roman Numeral: {self.roman_numeral}")
number = int(input("Enter an integer to convert to roman numeral: "))
converter = RomanConverter(number)
roman = converter.convert_to_roman()
converter.display()