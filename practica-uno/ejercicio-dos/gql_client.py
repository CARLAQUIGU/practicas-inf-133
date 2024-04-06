import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL para listar todas las plantas
query_lista_plantas = """
{
    plantas {
        id
        nombre_comun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para listar todas las plantas
response = requests.post(url, json={'query': query_lista_plantas})
print("\nLISTA DE PLANTAS:")
print(response.text)

# Definir la consulta GraphQL para buscar plantas por especie
query_plantas_por_especie = """
{
    plantasPorEspecie(especie: "Rosa spp.") {
        id
        nombre_comun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para buscar plantas por especie
response = requests.post(url, json={'query': query_plantas_por_especie})
print("\nPLANTAS POR ESPECIE (Rosa spp.):")
print(response.text)

# Definir la consulta GraphQL para buscar plantas que tienen frutos
query_plantas_con_frutos = """
{
    plantasConFrutos {
        id
        nombre_comun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL buscar plantas que tienen frutos
response = requests.post(url, json={'query': query_plantas_con_frutos})
print("\nPLANTAS CON FRUTOS:")
print(response.text)

# Definir la consulta GraphQL para crear una nueva planta
query_crear_planta = """
mutation {
    crearPlanta(
        nombreComun: "Girasol",
        especie: "Helianthus annuus",
        edad: 3,
        altura: 50.0,
        frutos: true
    ) {
        planta {
            id
            nombre_comun
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para crear una nueva planta
response = requests.post(url, json={'query': query_crear_planta})
print("\nCREAR NUEVA PLANTA (Girasol):")
print(response.text)

# Definir la consulta GraphQL para actualizar la información de una planta
query_actualizar_planta = """
mutation {
    actualizarPlanta(
        id: 3,
        nombreComun: "Girasol Gigante",
        especie: "Helianthus annuus",
        edad: 5,
        altura: 200.0,
        frutos: true
    ) {
        planta {
            id
            nombre_comun
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para actualizar la información de una planta
response = requests.post(url, json={'query': query_actualizar_planta})
print("\nACTUALIZAR PLANTA (Girasol Gigante):")
print(response.text)

# Definir la consulta GraphQL para eliminar una planta
query_eliminar_planta = """
mutation {
    eliminarPlanta(id: 1) {
        planta {
            id
            nombre_comun
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para eliminar una planta
response = requests.post(url, json={'query': query_eliminar_planta})
print("\nELIMINAR PLANTA (ID: 1):")
print(response.text)
# Definir la consulta GraphQL para listar todas las plantas
query_lista_plantas = """
{
    plantas {
        id
        nombre_comun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para listar todas las plantas
response = requests.post(url, json={'query': query_lista_plantas})
print("\nLISTA DE PLANTAS:")
print(response.text)