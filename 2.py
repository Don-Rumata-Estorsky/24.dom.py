"""
Напишите скрипт, который будет создавать виртуальное окружение и устанавливать 
туда библиотеку python-docx.
"""
import os
import subprocess

def create_venv(venv):
  

    if not os.path.exists(venv):
        print("создаём вертуальное окружение")
        subprocess.run(["python", "-m", "venv", "venv" ])
    else:
        print("виртуальное окружение уже созданно.")


def create_docx(docx):
    if not os.path.exists(docx):
        print("добавляем python-docx в вертуал. окруж.")
        subprocess.run(["pip", "install", "python-docx",  ])
    else:
        print("библиотека python-docx уже добавлена.")



if __name__ == "__main__":
    create_venv()  
    create_docx()