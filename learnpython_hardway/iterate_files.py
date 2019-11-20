users = [{ 'admin': True, 'active': False, 'name': 'Kevin' }, 
         {'admin': False, 'active': False, 'name': 'Mark'}, 
         {'admin': False, 'active': True, 'name': 'Juju'},
        ]
x = 1

for user in users:
    prefix = ""
    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix = "(ADMIN) "
    elif user['active']:
        prefix = "ACTIVE - "
    print(f"Number {x}: {prefix} {user['name']}")
    x += 1
