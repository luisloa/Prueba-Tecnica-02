class ConjuntoNumeros:
    __NUMEROS = list(range(1, 101))

    @classmethod
    def extract(cls, numero):
        if numero in cls.__NUMEROS:
            cls.__NUMEROS.remove(numero)
        return cls.__NUMEROS
    
    @classmethod
    def calcular_num_extraido(cls):
        for index, num in enumerate(cls.__NUMEROS):
            index += 1
            if index != num:
                print(f'Numero:  --> faltante')
                return index
            else:
                print(f'Numero: {num}')
                continue

if __name__ == '__main__':
    ConjuntoNumeros.extract(10)
    print(ConjuntoNumeros.calcular_num_extraido())
