from zeep import Client

client = Client('http://localhost:8000')
suma = client.service.Suma(n="5",m="5")
resta = client.service.Resta(n="5",m="5")
multi = client.service.Multiplicacion(n="5",m="5")
division = client.service.Division(n="10",m="5")
print("El resultado de la suma es : ", suma)
print("El resultado de la resta es : ", resta)
print("El resultado de la multiplicacion es : ", multi)
print("El resultado de la division es : ", division)