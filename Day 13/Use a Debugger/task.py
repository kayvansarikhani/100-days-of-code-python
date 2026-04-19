# import random
# import maths
#
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         # print(new_item)
#         # print("\n")
#         new_item += random.randint(1, 3)
#         # print(new_item)
#         # print("\n")
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
def is_leap(year):
    if year % 4 == 0:
        print(year % 4)
        if year % 100 == 0:
            print(year % 100)
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap(2000)