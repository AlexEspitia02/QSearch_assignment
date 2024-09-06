import random
users = {
    'user1': 'password1',
    'user2': 'password2'
}

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
