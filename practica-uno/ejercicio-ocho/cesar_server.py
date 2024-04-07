from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

mensajes = [
       {
            "id": 1,
            "content": "Este es un mensaje de ejemplo",
            "encrypted_content": "Hvwh hv xqphvih gh hvshyrh"
        }
]

class MensajeService:
    @staticmethod
    @staticmethod
    def add_mensaje(data):
        nuevo_id = len(mensajes) + 1
        data["id"] = nuevo_id
        if "encrypted_content" not in data:
            data["encrypted_content"] = MensajeService.encrypt_message(data["content"])
        mensajes.append(data)
        return mensajes

    @staticmethod
    def find_mensaje(id):
        return next(
            (mensaje for mensaje in mensajes if mensaje["id"] == id),
            None,
        )

    @staticmethod
    def update_mensaje(id, data):
        mensaje = MensajeService.find_mensaje(id)
        if mensaje:
            mensaje.update(data)
            return mensaje
        else:
            return None

    @staticmethod
    def delete_mensaje(id):
        mensaje = MensajeService.find_mensaje(id)
        if mensaje:
            mensajes.remove(mensaje)
            return {"mensaje": "Mensaje eliminado correctamente"}
        else:
            return {"error": "Mensaje no encontrado"}

    @staticmethod
    def get_all_mensajes():
        return mensajes

    @staticmethod
    def encrypt_message(message):
        encrypted_message = ""
        for char in message:
            if 'a' <= char <= 'z':
                encrypted_char = chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                encrypted_char = chr(((ord(char) - ord('A') + 3) % 26) + ord('A'))
            else:
                encrypted_char = char
            encrypted_message += encrypted_char
        return encrypted_message

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/mensajes":
            data = self.read_data()
            nuevo_mensaje = {
                "content": data.get("content")
            }
            mensajes = MensajeService.add_mensaje(nuevo_mensaje)
            HTTPResponseHandler.handle_response(self, 201, mensajes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no encontrada"}
            )


    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/mensajes":
            all_mensajes = MensajeService.get_all_mensajes()
            HTTPResponseHandler.handle_response(self, 200, all_mensajes)
        elif parsed_path.path.startswith("/mensajes/"):
            mensaje_id = int(parsed_path.path.split("/")[-1])
            mensaje = MensajeService.find_mensaje(mensaje_id)
            if mensaje:
                HTTPResponseHandler.handle_response(self, 200, mensaje)
            else:
                HTTPResponseHandler.handle_response(self, 404, {"Error": "Mensaje no encontrado"})
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no encontrada"})


    def do_PUT(self):
        if self.path.startswith("/mensajes/"):
            mensaje_id = int(self.path.split("/")[-1])
            data = self.read_data()
            mensaje_actualizado = MensajeService.update_mensaje(mensaje_id, data)
            if mensaje_actualizado:
                nuevo_contenido = data.get("content")
                if nuevo_contenido:
                    nuevo_contenido_encriptado = MensajeService.encrypt_message(nuevo_contenido)
                    mensaje_actualizado["content"] = nuevo_contenido
                    mensaje_actualizado["encrypted_content"] = nuevo_contenido_encriptado
                    # Actualiza el mensaje en la lista de mensajes
                    mensajes[mensaje_id - 1].update(mensaje_actualizado)
                HTTPResponseHandler.handle_response(self, 200, mensaje_actualizado)
            else:
                HTTPResponseHandler.handle_response(self, 404, {"Error": "Mensaje no encontrado"})
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no encontrada"}
            )


    def do_DELETE(self):
        if self.path.startswith("/mensajes/"):
            mensaje_id = int(self.path.split("/")[-1])
            resultado = MensajeService.delete_mensaje(mensaje_id)
            HTTPResponseHandler.handle_response(self, 200, resultado)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no encontrada"}
            )

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

