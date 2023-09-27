# Polymorphism means the ability to take different forms

class Europe:
    def capital_city(self):
        print('Switzerland is the headquarters of Europe')

    def language(self):
        print('English & German are spoken in Switzerland')


class Spain(Europe):
    def capital_city(self):
        print('Madrid is the capital of Spain')

    def language(self):
        print('Spanish is spoken in spain')


european = Europe()
european.capital_city()
european.language()

spanish = Spain()
spanish.capital_city()
spanish.language()
