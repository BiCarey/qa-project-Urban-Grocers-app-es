import configuration
import requests
import data


#Funcion para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
Autoken = response.json()['authToken']

headers_2 = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {Autoken}'
}


#Funcion para crear un nuevo Kit personal de producto
def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,# inserta la dirección URL completa
                         json=kit_body,  # inserta el cuerpo de solicitud
                         headers=headers_2) # inserta los encabezados, incluyendo la Autorization


response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())




