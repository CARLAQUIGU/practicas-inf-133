import requests

url = "http://localhost:8000/"

# POST para agregar un nuevo animal por la ruta /animales
ruta_post = url + "animales"
nuevo_animal = {
    "id": 2,
    "nombre": "Leon",
    "especie": "Panthera leo",
    "genero": "Macho",
    "edad": "5",
    "peso": "180",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

# GET para obtener todos los animales por la ruta /animales
print("\nLISTA DE ANIMALES")
ruta_get = url + "animales"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET para obtener animales por especie por la ruta /animales?especie={especie}
print("\nANIMALES POR ESPECIE")
especie = "Panthera leo"
ruta_get_especie = url + f"animales?especie={especie}"
get_response_especie = requests.request(method="GET", url=ruta_get_especie)
print(get_response_especie.text)

# GET para obtener animales por género por la ruta /animales?genero={genero}
print("\nANIMALES POR GÉNERO")
genero = "Hembra"
ruta_get_genero = url + f"animales?genero={genero}"
get_response_genero = requests.request(method="GET", url=ruta_get_genero)
print(get_response_genero.text)

print("\nACTUALIZANDO ANIMAL")
# PUT para actualizar la información de un animal por su ID por la ruta /animales/{id}
animal_id = 2
ruta_put = url + f"animales/{animal_id}"
datos_actualizados = {
    "nombre": "Leon actualizado",
    "especie": "Panthera leo",
    "genero": "Macho",
    "edad": "5",
    "peso": "180",
}
put_response = requests.request(method="PUT", url=ruta_put, json=datos_actualizados)
print(put_response.text)

print("\nELIMINAR ANIMAL")
# DELETE para eliminar un animal por su ID por la ruta /animales/{id}
animal_id = 1
ruta_delete = url + f"animales/{animal_id}"
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)

# GET para obtener todos los animales después de eliminar uno por la ruta /animales
print("\nLISTA DE ANIMALES DESPUÉS DE ELIMINAR")
get_response_after_delete = requests.request(method="GET", url=ruta_get)
print(get_response_after_delete.text)
