class User:

    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


    # pass

user_1 = User(user_id="001", username="Kayvan")
user_2 = User(user_id="002", username="Hanh")
# user_2.id = "002"
# user_2.username = "Hanh"

# user_1.id = "001"
# user_1.username = "Kayvan"

user_1.follow(user=user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


print(user_1.username, user_1.followers)

help(print)

# print(user_1.id, user_1.username)