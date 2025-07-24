from fastapi import FastAPI
from conjunto_numeros import ConjuntoNumeros

app = FastAPI()

@app.get("/")
def validacion():
    try:
        valor = int(input('Ingresa por consola un numero entero <1-100>, para eliminar de la lista: '))
        if 1 <= valor <= 100:
            ConjuntoNumeros.extract(valor)
            num_extraido = ConjuntoNumeros.calcular_num_extraido()
            return {'numero_extraido': num_extraido}
        else:
            print('Solo se permiten numeros enteros <1-100>')

    except Exception as e:
        print(f'Error: {e}, recuerda solo se permiten numeros enteros <1-100>')

if __name__ == '__main__':
    print(validacion())