# FLASKSHING
Flaskshing es una aplicación de phishing (simulada) diseñada en Python utilizando Flask. Su propósito es simular una página de inicio de sesión para diferentes plataformas y captura las credenciales ingresadas por los usuarios.

## Caracteristicas
* Simulación de páginas de inicio de sesión.
* Captura y almacenamiento de credenciales ingresadas en un archivo.
* Visualización de credenciales capturadas desde el archivo.
* Interfaz de línea de comandos para seleccionar opciones.

## Requisitos
* Python 3.x
* Flask
* Terminal

## Instalación
1. Clonar repositorio
````
git clone https://github.com/AlexArce2000/flaskshing.git
````
2. Instalar dependencias
````
pip install -r requirements.txt
````
3. Ejecutar el sistema
````
python flaskshing.py
````
Accede al servidor en: http://127.0.0.1:5000

Para exponer tu aplicación Flask en un entorno que no sea localhost, puedes usar herramientas como ngrok, serveo o localtunnel. La elección de la herramienta depende de tus preferencias y necesidades específicas yo utlizo `cloudflared`.

### Instalar Cloudflared
#### Actualizar el sistema
````
sudo apt update
sudo apt upgrade
````
#### Descargar el binario de cloudflared
```
mkdir -p ~/bin
cd ~/bin
```
#### Descarga la última versión de cloudflared:
```
curl -LO https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
```

#### Hacer al archivo ejecutable

```
chmod +x cloudflared-linux-amd64
```

#### Mover el binario a un directorio en el PATH
```
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
```
#### Verificar la instalación
```
cloudflared --version
```
#### Modo de uso 
```
cloudflared tunnel --url http://localhost:3000
```