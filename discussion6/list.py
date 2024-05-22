my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]
my_list.insert(1, 'a')  # [1, 'a', 2, 3, 4]
my_list.extend([5, 6])  # [1, 'a', 2, 3, 4, 5, 6]


# my_list = [1, 2, 3]
# my_list[0] = 'one'  # ['one', 2, 3]
# print(my_list)

# my_list = ['one', 2, 3, 2]
# my_list.pop(1)  # Removes 2: ['one', 3, 2]
# my_list.remove(2)  # Removes first 2: ['one', 3]
# del my_list[0]  # ['3']
# my_list.clear()  # []
# print(my_list)

# my_dict = {'name': 'John', 'age': 25}
# my_dict['age'] = 26  # Update
# my_dict['city'] = 'New York'  # Insert

# print(my_dict['name'])  # John
# print(my_dict['age'])  # 26

# my_dict = {'name': 'John', 'age': 26, 'city': 'New York'}
# age = my_dict.pop('age')  # Removes age: {'name': 'John', 'city': 'New York'}
# del my_dict['city']  # {'name': 'John'}
# my_dict.clear()  # {}
# print(my_dict)

# colors = ['red', 'green', 'blue']
# colors.append('yellow')
# print(colors)  # ['red', 'green', 'blue', 'yellow']
# colors.pop(1)  # Removes 'green'
# print(colors)  # ['red', 'blue', 'yellow']

# user = {'username': 'jdoe', 'email': 'jdoe@example.com'}
# user['name'] = 'John Doe'  # Insert/Update
# print(user)  # {'username': 'jdoe', 'email': 'jdoe@example.com', 'name': 'John Doe'}
# user.pop('email')
# print(user)  # {'username': 'jdoe', 'name': 'John Doe'}


