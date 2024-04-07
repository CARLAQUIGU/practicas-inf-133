import requests
import json

url = "http://localhost:8000/animales"
headers = {"Content-Type": "application/json"}
print("\nAÑADIENDO ANIMALES")
# POST /animales
nuevo_animal = {
    "tipo": "mamífero",
    "nombre": "León",
    "especie": "Panthera leo",
    "genero": "macho",
    "edad": 5,
    "peso": 150
}
response = requests.post(url=url, json=nuevo_animal, headers=headers)
print(response.json())

new_animal_data = {
    "tipo": "ave",
    "nombre": "Águila",
    "especie": "Aquila chrysaetos",
    "genero": "hembra",
    "edad": 8,
    "peso": 6
}
response = requests.post(url=url, json=new_animal_data, headers=headers)
print(response.json())


# GET para obtener todos los animales por la ruta /animales
print("\nLISTA DE  ANIMALES")
response = requests.get(url=url)
print(response.json())


# GET para obtener todos los animales por especie por la ruta /animales?especie={especie}
print("\nANIMALES POR ESPECIE")
especie = "Panthera leo"
response = requests.get(f"{url}?especie={especie}")
print(response.json())


# GET para obtener todos los animales por genero por la ruta /animales?genero={genero}
print("\nANIMALES POR GENERO")
genero = "macho"
response = requests.get(f"{url}?genero={genero}")
print(response.json())


# # PUT para actualizar animales por la ruta /animales/{id}
print("\nACTUALIZAR ANIMAL")
animal_id = 1
update_animal = {
    "nombre": "León africano",
    "peso": 200
}
response = requests.put(f"{url}/{animal_id}", json=update_animal)
print("Animal actualizado:", response.json())


print("\nELIMINAR ANIMAL")
# # DELETE para eliminar animales por la ruta /animales/{id}
delete_animal = 1
response = requests.delete(f"{url}/{delete_animal}")
print("Animal eliminado:", response.json())

print("\nLISTA DE  ANIMALES")
response = requests.get(url=url)
print(response.json())
