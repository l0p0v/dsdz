users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # isso funciona porque users[i] é o usuário cujo id é 'i'
    users[i]["friends"].append(users[j]["name"])  # adiciona 'i' como um amigo de 'j'
    users[j]["friends"].append(users[i]["name"])  # adiciona 'j' como um amigo de 'i'

total_connections = sum([len(user["friends"]) for user in users])
num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], len(user["friends"])) for user in users]
# cada par é um (user_id, num_friends)
num_friends_by_id = sorted(num_friends_by_id, key=lambda it: it[1], reverse=True)

print(num_friends_by_id[:5])
print(num_friends_by_id[5:])
