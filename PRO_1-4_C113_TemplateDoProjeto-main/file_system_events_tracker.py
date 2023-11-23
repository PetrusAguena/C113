import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:\Users\petru\Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado")
    def on_deleted(self, event):
        print(f"Opa, Alguém excluiu {event.src_path}")    
    def on_modified(self, event):
        print(f"Eita, Alguém modificou {event.src_path}")
    def on_moved(self, event):
        print(f"Epa, Alguém moveu {event.src_path}")
    



# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt

while True:
    time.sleep(2)
    print("executando...")






