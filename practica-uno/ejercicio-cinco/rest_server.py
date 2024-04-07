from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

animales = [
    {
        "id": 1,
        "nombre": "Jirafa",
        "especie": "Giraffa camelopardalis",
        "genero": "Hembra",
        "edad": "5",
        "peso": "180",
    },
]

class AnimalService:
    @staticmethod
    def add_animal(data):
        id = data.get("id")
        animal_existente = AnimalService.find_animal(id)
        if animal_existente:
            return {"error": "Ya existe un animal con el mismo ID."}
        else:
            animales.append(data)
            return animales

    @staticmethod
    def find_animal(id):
        return next(
            (animal for animal in animales if animal["id"] == id),
            None,
        )

    @staticmethod
    def filter_animals_by_name(nombre):
        return [
            animal for animal in animales if animal["nombre"] == nombre
        ]

    @staticmethod
    def filter_animals_by_species(especie):
        return [
            animal for animal in animales if animal["especie"].lower() == especie.lower()
        ]

    @staticmethod
    def filter_animals_by_gender(genero):
        return [
            animal for animal in animales if animal["genero"].lower() == genero.lower()
        ]

    @staticmethod
    def update_animal(id, data):
        animal = AnimalService.find_animal(id)
        if animal:
            animal.update(data)
            return animal
        else:
            return None

    @staticmethod
    def delete_animal(id):
        animal = AnimalService.find_animal(id)
        if animal:
            animales.remove(animal)
            return {"message": "Animal eliminado correctamente"}
        else:
            return {"error": "Animal no encontrado"}

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/animales":
            data = self.read_data()
            animales = AnimalService.add_animal(data)
            HTTPResponseHandler.handle_response(self, 201, animales)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path == "/animales":
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                animales_filtrados = AnimalService.filter_animals_by_name(nombre)
                if animales_filtrados:
                    HTTPResponseHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            elif "especie" in query_params:
                especie = query_params["especie"][0]
                animales_filtrados = AnimalService.filter_animals_by_species(especie)
                if animales_filtrados:
                    HTTPResponseHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            elif "genero" in query_params:
                genero = query_params["genero"][0]
                animales_filtrados = AnimalService.filter_animals_by_gender(genero)
                if animales_filtrados:
                    HTTPResponseHandler.handle_response(self, 200, animales_filtrados)
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 200, animales)
        elif parsed_path.path.startswith("/animales/"):
            animal_id = int(parsed_path.path.split("/")[-1])
            animal = AnimalService.find_animal(animal_id)
            if animal:
                HTTPResponseHandler.handle_response(self, 200, [animal])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            data = self.read_data()
            animal_actualizado = AnimalService.update_animal(animal_id, data)
            if animal_actualizado:
                HTTPResponseHandler.handle_response(self, 200, animal_actualizado)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error": "Animal no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith("/animales/"):
            animal_id = int(parsed_path.path.split("/")[-1])
            resultado = AnimalService.delete_animal(animal_id)
            HTTPResponseHandler.handle_response(self, 200, resultado)
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()
