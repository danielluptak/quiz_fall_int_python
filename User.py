from DBConnection import DBConnection


class User:
    def __init__(self):
        self.id = None
        self.username = ''
        self.is_valid = False

    def get_username(self):
        # ask user for the username
        # keep username in class var
        print("Give username: ")
        name = input()
        self.username = name

    def check_username(self):
        db = DBConnection()
        user = db.check_user(self.username)
        if user is not None:
            self.id = user[0]
            self.is_valid = True
        else:
            self.id = None
            self.is_valid = False

    def __str__(self):
        return "User: " + self.username + " " + str(self.is_valid)


if __name__ == '__main__':
    user = User()
    user.get_username()
    user.check_username()
    print(user)