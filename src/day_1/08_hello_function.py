
def user_hello(user):
    print(f'Привет {user}')

users = ['John', 'David', 'Kate', 'Alex']

for user in users:
    user_hello(user)
    # print(f'Привет {user}')

new_user = 'Arthur'

users.append(new_user)
user_hello(new_user)

# print(f'Hi, {users[-1]}')
