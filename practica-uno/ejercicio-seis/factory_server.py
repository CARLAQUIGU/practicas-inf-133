from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

# Base de datos simulada de animales
animales = {}


class Animal:
    def __init__(self, nombre, especie, genero, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso


class Mamifero(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "mamífero"


class Ave(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "ave"


class Reptil(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "reptil"


class Anfibio(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "anfibio"


class Pez(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        self.tipo = "pez"


class AnimalFactory:
    @staticmethod
    def create_animal(tipo, nombre, especie, genero, edad, peso):
        if tipo == "mamífero":
            return Mamifero(nombre, especie, genero, edad, peso)
        elif tipo == "ave":
            return Ave(nombre, especie, genero, edad, peso)
        elif tipo == "reptil":
            return Reptil(nombre, especie, genero, edad, peso)
        elif tipo == "anfibio":
            return Anfibio(nombre, especie, genero, edad, peso)
        elif tipo == "pez":
            return Pez(nombre, especie, genero, edad, peso)
        else:
            raise ValueError("Tipo de animal no válido")


class AnimalService:
    def __init__(self):
        self.factory = AnimalFactory()

    def add_animal(self, data):
        id = len(animales) + 1
        tipo = data.get("tipo")
        nombre = data.get("nombre")
        especie = data.get("especie")
        genero = data.get("genero")
        edad = data.get("edad")
        peso = data.get("peso")

        animal = self.factory.create_animal(tipo, nombre, especie, genero, edad, peso)
        animales[id] = animal.__dict__
        return animal.__dict__

    def find_animal(self, id):
        return animales.get(id)

    def filter_animals_by_name(self, nombre):
        return [animal for animal in animales.values() if animal["nombre"] == nombre]

    def filter_animals_by_species(self, especie):
        return [animal for animal in animales.values() if animal["especie"].lower() == especie.lower()]

    def filter_animals_by_gender(self, genero):
        return [animal for animal in animales.values() if animal["genero"].lower() == genero.lower()]

    def update_animal(self, id, data):
        if id in animales:
            animales[id].update(data)
            return animales[id]
        else:
            return None

    def delete_animal(self, id):
        if id in animales:
            del animales[id]
            return {"message": "Animal eliminado correctamente"}
        else:
            return None


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class AnimalRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.animal_service = AnimalService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/animales":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.animal_service.add_animal(data)
            HTTPDataHandler.handle_response(self, 201, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path == "/animales":
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                animales_filtrados = self.animal_service.filter_animals_by_name(nombre)
                if animales_filtrados:
                    HTTPDataHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPDataHandler.handle_response(self, 204, [])
            elif "especie" in query_params:
                especie = query_params["especie"][0]
                animales_filtrados = self.animal_service.filter_animals_by_species(especie)
                if animales_filtrados:
                    HTTPDataHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPDataHandler.handle_response(self, 204, [])
            elif "genero" in query_params:
                genero = query_params["genero"][0]
                animales_filtrados = self.animal_service.filter_animals_by_gender(genero)
                if animales_filtrados:
                    HTTPDataHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPDataHandler.handle_response(self, 204, [])
            else:
                animales_list = list(animales.values())
                HTTPDataHandler.handle_response(self, 200, animales_list)
        elif parsed_path.path.startswith("/animales/"):
            animal_id = int(parsed_path.path.split("/")[-1])
            animal = self.animal_service.find_animal(animal_id)
            if animal:
                HTTPDataHandler.handle_response(self, 200, animal)
            else:
                HTTPDataHandler.handle_response(self, 404, {"message": "Animal no encontrado"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith("/animales/"):
            try:
                animal_id = int(parsed_path.path.split("/")[-1])  # Extraer el ID del animal de la URL
                data = HTTPDataHandler.handle_reader(self)
                animal_actualizado = self.animal_service.update_animal(animal_id, data)
                if animal_actualizado:
                    HTTPDataHandler.handle_response(self, 200, animal_actualizado)
                else:
                    HTTPDataHandler.handle_response(
                        self, 404, {"message": "Animal no encontrado"}
                    )
            except ValueError:
                HTTPDataHandler.handle_response(
                    self, 400, {"message": "ID de animal no válido"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith("/animales/"):
            animal_id = int(parsed_path.path.split("/")[-1])
            resultado = self.animal_service.delete_animal(animal_id)
            if resultado:
                HTTPDataHandler.handle_response(self, 200, resultado)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Animal no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, AnimalRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
