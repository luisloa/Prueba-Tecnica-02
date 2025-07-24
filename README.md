# Prueba-Tecnica-02
# Sección 2:

Esta aplicación permite al usuario interactuar con una lista que contiene los primeros 100 números naturales, y eliminar uno de ellos a través de la interfaz de la terminal. Posteriormente, la aplicación calcula automáticamente cuál fue el número eliminado y envía esta información en formato JSON a un servidor local (localhost) mediante una solicitud HTTP.

# Tecnologías implementadas

- Python
- fastAPI
- Uvicorn
- Git
- Github
- vevn

# Requerimientos (requirements.txt)

- annotated-types==0.7.0
- anyio==4.9.0
- click==8.2.1
- fastapi==0.116.1
- h11==0.16.0
- idna==3.10
- pydantic==2.11.7
- pydantic_core==2.33.2
- sniffio==1.3.1
- starlette==0.47.2
- typing-inspection==0.4.1
- typing_extensions==4.14.1
- uvicorn==0.35.0

# Recomendaciones de Instalacion
# Requsitos

- Python 3.10 o superior https://www.python.org/downloads/
- Git y Github

# Clonar Repositorio desde Github

# ****** INSTRUCCIONES DE USO ******
# Desde terminal

    1. git clone https://github.com/luisloa/Prueba-Tecnica-02.git
    2. cd Prueba-Tecnica-02
    3. source prueba_tec-env/bin/activate
    3. uvicorn main:app --reload
    4. Abrir servidor http://127.0.0.1:8000
    5. Ingresar numero a eliminar

# Proceso

La aplicación se ejecuta al iniciar el servidor local con Uvicorn. Durante su funcionamiento, se activan los scripts principales: conjunto_numeros.py y main.py.

# Scripts

# conjunto_numeros.py
Contiene la lógica de manipulación de una lista con los primeros 100 números naturales.

Funciones:

- Generación de la lista: Crea una lista con los números del 1 al 100.

- Extracción de número: A través del método de clase extract(), elimina el número que el usuario ingresa por terminal.

- Resultado de extracción: Devuelve la lista actualizada sin el número eliminado.

- Cálculo del número eliminado: Mediante el método calcular_numero_extraido(), se compara la lista original con la modificada para detectar qué número fue eliminado. Una vez identificado, el proceso se detiene.

- Resultado final: Retorna el número eliminado.

# main.py
Define el servidor y la API con FastAPI.

Funcionalidades:

- Inicialización del servidor: Crea una aplicación web utilizando FastAPI.

- Asignación de ruta: Define un endpoint para interactuar con el servidor local.

- Solicitud de numero: Solicita al usuario un número por consola. 

- Validación de entrada: Verifica que el número ingresado por el usuario:
    - Sea un número entero.

    - Se encuentre en el rango de 1 a 100.

- Ejecución del proceso:

    - Si el número es válido, se llama al método extract() para eliminarlo de la lista.

    - Luego se ejecuta calcular_numero_extraido() para identificar cuál fue el número extraído.

    - Finalmente, el resultado se envía al servidor mediante una solicitud HTTP en formato JSON.
    
# Estructura proyecto
../prueba_tecnica_02/
├── conjunto_numeros.py
├── main.py
├── prueba_tec-env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   └── pyvenv.cfg
├── __pycache__
│   ├── conjunto_numeros.cpython-311.pyc
│   └── main.cpython-311.pyc
├── README.md
└── requirements.txt


