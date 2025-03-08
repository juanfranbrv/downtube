"""
Archivo principal del proyecto downtube.
Este archivo se encarga de descargar un video de YouTube

Usa la librería pytubefix para descargar videos de YouTube.
Para instalar pytubefix, ejecuta el siguiente comando:
pip install pytubefix

Para instalar la librería rich, ejecuta el siguiente comando:
pip install rich

Para instalar la librería pyfiglet, ejecuta el siguiente comando:
pip install pyfiglet

Para visualiza los tipos de letra de Figlet, puedes visitar el siguiente enlace:
https://www.askapache.com/online-tools/figlet-ascii/

"""
import os
from rich import print as rprint

from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

import pyfiglet 

def pulsa_tecla():
    input("\n\nPulsa una tecla para continuar...")

while True:
    os.system("cls")

    texto_formateado = pyfiglet.figlet_format("DownTube", font="slant")
    rprint(f"[bold magenta]{texto_formateado}[/bold magenta]")
    rprint(f"[bold magenta]DESCARGADOR DE VIDEOS DE YOUTUBE[/bold magenta]")
    rprint(f"[bold magenta]Creado con 💗 por @juanfrabrv[/bold magenta]")
    rprint(f"\n")
    rprint(f"1 : Descargar vídeo")
    rprint(f"2 : Descargar audio")
    rprint(f"3 : Descargar lista de reproducción completa")
    rprint(f"0 : Salir\n")
    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        break
    elif opcion == "1":
        url = input("Introduce la URL del vídeo: ")
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        rprint(f"Descargando... {yt.title}")

        ys.download()
        rprint("[bold green]\nDescarga completada[/bold green]")
        pulsa_tecla()
    elif opcion == "2":
        url = input("Introduce la URL del vídeo ▶ audio: ")
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        rprint(f"Descargando... {yt.title}")

        ys.download()
        rprint("[bold green]\nDescarga completada[/bold green]")
        pulsa_tecla()
        
    elif opcion == "3":
        url = input("Introduce la URL del vídeo: ")
        lista_reproduccion = Playlist(url)

        rprint(f"Descargando lista de reproducción... {lista_reproduccion.title}")
        rprint(f"Descargando {len(lista_reproduccion.videos)} vídeos")
        for video in lista_reproduccion.videos:
            rprint(f"Descargando... {video.title}")
            ys = video.streams.get_highest_resolution()
            ys.download()

        rprint("[bold green]\nDescarga completada[/bold green]")
        pulsa_tecla()

