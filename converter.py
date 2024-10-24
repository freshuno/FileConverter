import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import os
from PIL import Image


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konwerter Multimediów")
        self.root.geometry("700x300")

        # Etykieta i przycisk do wczytywania pliku
        self.label = tk.Label(root, text="Wybierz plik do konwersji:")
        self.label.pack(pady=10)

        self.select_file_btn = tk.Button(root, text="Wybierz plik", command=self.load_file)
        self.select_file_btn.pack(pady=5)

        # Etykieta do wyświetlania wybranego pliku
        self.file_label = tk.Label(root, text="Nie wybrano pliku")
        self.file_label.pack(pady=5)

        # Wybór formatu docelowego
        self.format_label = tk.Label(root, text="Wybierz format docelowy:")
        self.format_label.pack(pady=10)

        self.format_options = ["jpg", "png", "mp4", "mp3", "wav"]
        self.selected_format = tk.StringVar(root)
        self.selected_format.set(self.format_options[0])  # Domyślnie jpg

        self.format_menu = tk.OptionMenu(root, self.selected_format, *self.format_options)
        self.format_menu.pack(pady=5)

        # Przycisk do konwersji
        self.convert_btn = tk.Button(root, text="Konwertuj", command=self.convert_file)
        self.convert_btn.pack(pady=20)

        # Ścieżka do wybranego pliku
        self.file_path = None

    def load_file(self):
        """Funkcja ładuje plik wybrany przez użytkownika"""
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))

    def convert_file(self):
        """Funkcja konwertuje plik do wybranego formatu"""
        if not self.file_path:
            messagebox.showerror("Błąd", "Nie wybrano pliku do konwersji!")
            return

        # Pobierz wybrany format
        output_format = self.selected_format.get()
        output_file = os.path.splitext(self.file_path)[0] + f".{output_format}"

        print(f"Rozpoczynam konwersję: {self.file_path} do {output_file}")

        try:
            if output_format in ["jpg", "png"]:
                self.convert_image(output_file, output_format)
            elif output_format in ["mp3", "wav"]:
                self.convert_audio(output_file, output_format)
            elif output_format in ["mp4"]:
                self.convert_video(output_file, output_format)
            messagebox.showinfo("Sukces", f"Plik został przekonwertowany do {output_format}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się przekonwertować pliku: {str(e)}")

    def convert_image(self, output_file, format):
        """Konwersja pliku obrazu"""
        try:
            print(f"Konwertowanie obrazu do formatu: {format}")
            img = Image.open(self.file_path)
            print("Obraz został załadowany.")
            if format == "jpg":
                img = img.convert("RGB")  # Usunięcie przezroczystości
                print("Obraz przekonwertowany do RGB.")
            img.save(output_file, "JPEG")  # Użyj "JPEG"
            print(f"Obraz zapisany jako: {output_file}")
        except Exception as e:
            print(f"Błąd podczas konwersji obrazu: {str(e)}")
            raise

    def convert_audio(self, output_file, format):
        """Konwersja pliku audio"""
        print(f"Konwertowanie audio do formatu: {format}")
        stream = ffmpeg.input(self.file_path)
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream)
        print(f"Audio zapisane jako: {output_file}")

    def convert_video(self, output_file, format):
        """Konwersja pliku wideo"""
        print(f"Konwertowanie wideo do formatu: {format}")
        stream = ffmpeg.input(self.file_path)
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream)
        print(f"Wideo zapisane jako: {output_file}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
