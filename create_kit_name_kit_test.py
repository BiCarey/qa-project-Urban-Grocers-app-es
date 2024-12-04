import configuration
import data
import sender_stand_request
from data import kit_body


# esta función cambia los valores en el cuerpo de la solicitud, especificamente en el parámetro "name"
def get_kit_body (name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body


# Función de prueba positiva
#Función para los test: 1,2,5,6 y 7
def positive_assert(kit_body):  # en instrucciones es positive_assert(kit_body)
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    #kit_body =  get_kit_body(kit_body)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    #assert kit_response.json()["authToken"] != ""



# Función de prueba negativa para Prueba 3 y Prueba 8
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_code_400_no_name(kit_body):
    #Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_client_kit(kit_body)

    #Comprueba si larespuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#Función de prueba negativa para Prueba 4
def negative_assert_code_400(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(kit_body)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 1. Creación de un nuevo kit
# El kit_body contiene 1 caracter
def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert(data.kit_body_1)

# Prueba 2. Creación de un nuevo kit
# El kit_body contiene 511 caracter
def test_create_kit_511_letter_in_kit_body_get_success_response():
    positive_assert(data.kit_body_2)


#Prueba 3. Error porque el valor de name esta vacío
def test_create_kit_no_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(data.kit_body_3)
    # Comprueba la respuesta
    negative_assert_code_400_no_name(kit_body)



#Prueba 4. Error
# El parámetro "name" contiene 512 caracteres
def test_create_kit_name_512_letters_get_error_response():
    negative_assert_code_400(data.kit_body_4)


#prueba 5. Se permiten cracteres especiales en el name
def test_create_kit_name_special_symbol_get_success_response():
    positive_assert(data.kit_body_5)


# Prueba 6. se espera un 201.
# El parámetro "name" contiene palabras con espacios
def test_create_kit_has_space_en_name_get_succes_response():
    positive_assert(data.kit_body_6)


#Prueba 7. Se espera un 201
#se permiten numeros en name
def test_create_kit_has_numbers_in_name_get_error_response():
    positive_assert(data.kit_body_7)


#Prueba 8. Se espera un 400. El parametro "name" no se pasa en la solicitud
def test_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_code_400_no_name(kit_body)



#Prueb 9. se espera un 400. El parámetro "name" es un número
def tests_create_kit_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_kit_body(data.kit_body_9)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400





