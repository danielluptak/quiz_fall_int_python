class CategoryOption:

    def __init__(self):
        self.category = ''
        self.api = ''
        self.make = ''
        self.api1 = 'https://opentdb.com/api.php?amount=10&category=9&type=multiple'
        self.api2 = 'https://opentdb.com/api.php?amount=10&category=10&type=multiple'
        self.api3 = 'https://opentdb.com/api.php?amount=10&category=15&type=multiple'
        self.api4 = 'https://opentdb.com/api.php?amount=10&category=23&type=multiple'
        self.api5 = 'https://opentdb.com/api.php?amount=10&category=24&type=multiple'
        self.api6 = 'https://opentdb.com/api.php?amount=10&category=22&type=multiple'
        self.api_to_pass = ''

    def get_category(self):
        print("Please choose one of these categories: \n"
              "1: General Knowledge\n"
              "2: Entertainment: Books\n"
              "3: Entertainment: Video Games\n"
              "4: History\n"
              "5: Politics\n"
              "6: Geography")
        choice = input()
        self.category = choice
        print('You chose category number: ' + self.category)
        if choice == '1':
            self.api_to_pass = self.api1
        elif choice == '2':
            self.api_to_pass = self.api2
        elif choice == '3':
            self.api_to_pass = self.api3
        elif choice == '4':
            self.api_to_pass = self.api4
        elif choice == '5':
            self.api_to_pass = self.api5
        elif choice == '6':
            self.api_to_pass = self.api6


if __name__ == '__main__':
    cat = CategoryOption()
    cat.get_category()



