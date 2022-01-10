guest_list = ['гермиона грейнджерс', 'северус снег', 'профессор дамблдор']
# print(guest_list)

# invitation_hermiona = f"{guest_list[0].title()}, я приглашаю тебя на званый ужин"
# print(invitation_hermiona)

# invitation_severus = f"{guest_list[1].title()}, я приглашаю вас на званый ужин"
# print(invitation_severus)

# invitation_albus = f"{guest_list[2].title()}, я приглашаю вас на званый ужин"
# print(invitation_albus)

invitation_del = guest_list.pop(0)
# print(f"{invitation_del.title()} не сможет прийти на званый ужин")

# print(guest_list)

# print(f"{guest_list[0].title()}, я приглашаю тебя на званый ужин")

guest_list.insert(0, 'гарри поттер')
print(guest_list)

guest_list.insert(0, 'рон уизли')
print(guest_list)

guest_list.insert(2, 'профессор макгонагл')
print(guest_list)

guest_list.append('волан де-морт')
print(guest_list)

invitation_ron = f"{guest_list[0].title()}, я приглашаю тебя на званый ужин"
invitation_harry = f"{guest_list[1].title()}, я приглашаю тебя на званый ужин"
invitation_minerva = f"{guest_list[2].title()}, я приглашаю вас на званый ужин"
invitation_severus = f"{guest_list[3].title()}, я приглашаю вас на званый ужин"
invitation_albus = f"{guest_list[4].title()}, я приглашаю вас на званый ужин"
invitation_voldemort = f"{guest_list[5].title()}, я приглашаю тебя на званый ужин"

print(invitation_ron)
print(invitation_harry)
print(invitation_minerva)
print(invitation_severus)
print(invitation_albus)
print(invitation_voldemort)