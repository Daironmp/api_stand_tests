import configuration
import requests

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# 👇 AQUÍ VA
response = get_users_table()

# 👇 Y ESTO DESPUÉS
print(response.status_code)
