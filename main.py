import ffmpeg, os, sys, shutil
from tkinter import filedialog
import customtkinter
from pathlib import Path

class Error(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("System")

        self.label = customtkinter.CTkLabel(self, text="Es darf kein Feld leer sein!")
        self.label.pack(padx=20, pady=20)

class Success(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("System")

        self.label = customtkinter.CTkLabel(self, text="Die Konvertierung wurde gestartet")
        self.label.pack(padx=20, pady=20)

class Finished(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("System")

        self.label = customtkinter.CTkLabel(self, text="Die Konvertierung wurde erfolgreich beendet!")
        self.label.pack(padx=20, pady=20)

class App (customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Converter")
        self.geometry("500x400")
        self.resizable(True, True)
        
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.convertto = customtkinter.CTkEntry(self.main_frame, placeholder_text="Gebe das Format ein, zu welchem conventiert werden soll")
        self.convertto.pack(padx=10, pady=10, fill='x', expand=True)

        self.new_file_name = customtkinter.CTkEntry(self.main_frame, placeholder_text="Gebe den Namen ein, wie die neue Datei heißen soll")
        self.new_file_name.pack(padx=10, pady=10, fill='x', expand=True)

        self.convert = customtkinter.CTkButton(self.main_frame, text="Convert", command=self.convert)
        self.convert.pack(padx=10, pady=10, fill='x', expand=True)
        
    
    def convert(self):
        '''Convert a file to a requested format'''
        fileextention = self.convertto.get().lower()
        new_file_name = self.new_file_name.get()
        
        if fileextention != "" and new_file_name != "":
            path = filedialog.askopenfilename(title="Choose file", initialdir=Path(sys.executable))
            (ffmpeg.input(f'{path}').output(f"{new_file_name}.{fileextention}").run())
        
        else:
            Error()

if __name__ == '__main__':
    app = App()
    app.mainloop()