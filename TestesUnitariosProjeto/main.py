
from src.service.service_user import ServiceUser

service = ServiceUser()
user_1 = service.add_user("Cleonice", "Analista de Teste")
user_4 = service.add_user("Cleonice", "Analista de Teste")
user_2 = service.add_user("Diego", "Desenvolvedor")

# print(service.remove_user("Cleonice"))
print(user_1)
print(user_4)
print(user_2)


# print(user_1)
# print(service.update_user("Cleonice"))
for user in service.store.bd:
    print(f"{user.name} {user.job}")