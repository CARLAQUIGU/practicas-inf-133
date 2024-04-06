import requests
# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# POST agrega un nuevo paciente por la ruta /pacientes
ruta_post = url + "pacientes"
nuevo_paciente = {
    "ci": 12559632,
    "nombre": "Maria",
    "apellido": "Lopez",
    "edad": "21",
    "genero": "Femenino",
    "diagnostico": "diabetes",
    "doctor": "Marcos Borras",
}   
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
print(post_response.text)
# POST agrega un nuevo paciente por la ruta /pacientes
ruta_post = url + "pacientes"
nuevo_paciente = {
    "ci": 12993232,
    "nombre": "Carla",
    "apellido": "Quispe",
    "edad": "21",
    "genero": "Femenino",
    "diagnostico": "asma",
    "doctor": "Marcelo Martinez",
}   
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
print(post_response.text)
# GET obtener a todos los pacientes por la ruta /pacientes 
print("\nLISTA DE PACIENTES")
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get) 
print(get_response.text)
#Get obtener a todos los pacientes por ci por la ruta /pacientes {ci}
print("\nPACIENTE POR CI")
ci = 3111078 
ruta_get_ci = url + f"pacientes/{ci}"
get_response_ci = requests.request(method="GET", url=ruta_get_ci)
print(get_response_ci.text)
# GET obtener pacientes por diagnóstico
print("\nPACIENTE POR DIAGNOSTICO")
diagnostico = "asma" 
ruta_get_diagnostico = url + f"pacientes?diagnostico={diagnostico}"
get_response_diagnostico = requests.request(method="GET", url=ruta_get_diagnostico)
print(get_response_diagnostico.text)
# GET obtener pacientes por doctor
print("\nPACIENTE POR DOCTOR")
doctor = "Marcos Borras"  
ruta_get_doctor = url + f"pacientes?doctor={doctor}"
get_response_doctor = requests.request(method="GET", url=ruta_get_doctor)
print(get_response_doctor.text)
print("\nACTUALIZANDO PACIENTES")
# PUT actualizar la información de un paciente por su CI
ci = 3111078
ruta_put = url + f"pacientes/{ci}"
datos_actualizados = {
    "nombre": "Gael",
    "apellido": "Garcia",
    "edad": "25",
    "genero": "Masculino",
    "diagnostico": "asma",
    "doctor": "Marcos Borras"
}
put_response = requests.request(method="PUT", url=ruta_put, json=datos_actualizados)
print(put_response.text)
print("\nELIMINAR PACIENTES")
# DELETE eliminar un paciente por su CI
ci = 3111078  # ID del paciente que deseas eliminar
ruta_delete = url + f"pacientes/{ci}"
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)
#otro
print("\nLISTA DE PACIENTES")
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get) 
print(get_response.text)