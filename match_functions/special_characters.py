
class Specials: 
    characters = dict([
        ('$', '#36;'),     
        ('[', '#91;'),
        (']', '#93;'),
        (' ', '#32;'),
        ('"','#34;')
        ])

    def __init__(self):
        self = self

    def cleanse_special_characters(self,test_string):
        # specials = Specials()
    #    def replace_specials(test_string):
        parsed_string = test_string
        for char in self.characters:
            parsed_string = parsed_string.replace(char,'')
        return  parsed_string

    def utf8_special_characters(self,test_string):
        # specials = Specials()
    #    def replace_specials(test_string):
        parsed_string = ''
        for char in test_string:
            parsed_string += self.characters.get(char,char)
        return  parsed_string

#    return replace_specials(test_string) if len([char for char in test_string if char in Specials().characters]) > 0 else return test_string
