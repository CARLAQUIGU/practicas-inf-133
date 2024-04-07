import requests

url = "http://localhost:8000/"

# POST para agregar un nuevo mensaje por la ruta /mensajes
ruta_post = url + "mensajes"
nuevo_mensaje = {
    "id": 2,
    "content": "Hola Carla",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_mensaje)
print(post_response.text)

# GET para obtener todos los mensajes por la ruta /mensajes
print("\nLISTA DE MENSAJES")
ruta_get = url + "mensajes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET para obtener mensaje por ID por la ruta /mensajes/{id}

print("\nMENSAJE POR ID")
mensaje_id = 1
ruta_get_id = url + f"mensajes/{mensaje_id}"  # Aquí se incluye el ID del mensaje en la URL
get_response_id = requests.request(method="GET", url=ruta_get_id)
print(get_response_id.text)
# PUT para actualizar la información de un mensaje por su ID por la ruta /mensajes/{id}
print("\nACTUALIZANDO MENSAJE")
mensaje_id = 1
ruta_put = url + f"mensajes/{mensaje_id}"
datos_actualizados = {
    "content": "Hola carla"
}
put_response = requests.request(method="PUT", url=ruta_put, json=datos_actualizados)
print(put_response.text)

# DELETE para eliminar un mensaje por su ID por la ruta /mensajes/{id}
print("\nELIMINAR MENSAJE")
mensaje_id = 2
ruta_delete = url + f"mensajes/{mensaje_id}"
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)

# GET para obtener todos los mensajes después de eliminar uno por la ruta /mensajes
print("\nLISTA DE MENSAJES DESPUÉS DE ELIMINAR")
get_response_after_delete = requests.request(method="GET", url=ruta_get)
print(get_response_after_delete.text)
