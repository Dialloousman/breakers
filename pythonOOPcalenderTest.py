class Routine:
    def __init__(self, person):
        self.person = person

    def morning(self):
        print('good morning' + ' ' + self.person)
    
    def afternoon (self):
        print('Hey {}, are you hungry yet?'.format(self.person))

    def evening (self):
        print('{}, its time for bed!'.format(self.person))

# inhertiance example
class Schedule(Routine):
    def greeting():
        pass