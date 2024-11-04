import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import os
import shutil
from PIL import Image

# Ustaw ścieżkę do ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-7.1-full_build\bin"  # Upewnij się, że to jest właściwa ścieżka

MAX_FILE_SIZE_MB = 200  # Maksymalny rozmiar pliku w MB

# Słowniki formatów dostępnych dla każdego typu pliku
IMAGE_FORMATS = ["jpg", "png", "gif"]
AUDIO_FORMATS = ["mp3", "wav", "flac"]
VIDEO_FORMATS = ["mp4", "mov"]

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

        # Menu wyboru formatu (dynamicznie aktualizowane)
        self.selected_format = tk.StringVar(root)
        self.format_menu = tk.OptionMenu(root, self.selected_format, "")
        self.format_menu.pack(pady=5)

        # Przycisk do konwersji
        self.convert_btn = tk.Button(root, text="Konwertuj", command=self.convert_file)
        self.convert_btn.pack(pady=20)

        # Przycisk do pobrania pliku, początkowo wyłączony
        self.download_btn = tk.Button(root, text="Pobierz", command=self.download_file, state="disabled")
        self.download_btn.pack(pady=10)

        # Ścieżka do wybranego pliku
        self.file_path = None
        # Ścieżka do przekonwertowanego pliku
        self.output_file = None

    def load_file(self):
        """Funkcja ładuje plik wybrany przez użytkownika i sprawdza jego rozmiar oraz typ"""
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            file_size_mb = os.path.getsize(self.file_path) / (1024 * 1024)  # Rozmiar w MB
            if file_size_mb > MAX_FILE_SIZE_MB:
                messagebox.showerror("Błąd", f"Plik przekracza maksymalny rozmiar {MAX_FILE_SIZE_MB} MB!")
                self.file_path = None  # Wyczyszczenie ścieżki, aby uniknąć konwersji dużego pliku
                self.file_label.config(text="Nie wybrano pliku")
                self.update_format_options([])  # Wyczyść opcje formatów
            else:
                self.file_label.config(text=os.path.basename(self.file_path))
                self.update_format_options(self.get_available_formats(self.file_path))
                self.download_btn.config(state="disabled")  # Wyłącz przycisk "Pobierz" do czasu konwersji

    def get_available_formats(self, file_path):
        """Zwraca dostępne formaty docelowe w zależności od typu pliku"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower().replace(".", "")  # Przetworzenie rozszerzenia

        if ext in IMAGE_FORMATS:
            return [fmt for fmt in IMAGE_FORMATS if fmt != ext]
        elif ext in AUDIO_FORMATS:
            return [fmt for fmt in AUDIO_FORMATS if fmt != ext]
        elif ext in VIDEO_FORMATS:
            return [fmt for fmt in VIDEO_FORMATS if fmt != ext]
        else:
            messagebox.showerror("Błąd", "Nieobsługiwany typ pliku.")
            return []

    def update_format_options(self, formats):
        """Aktualizuje dostępne opcje formatów docelowych w menu wyboru formatu"""
        self.format_menu["menu"].delete(0, "end")
        for fmt in formats:
            self.format_menu["menu"].add_command(label=fmt, command=tk._setit(self.selected_format, fmt))
        if formats:
            self.selected_format.set(formats[0])  # Ustaw pierwszy format jako domyślny
        else:
            self.selected_format.set("")  # Wyczyść wybór formatu

    def convert_file(self):
        """Funkcja konwertuje plik do wybranego formatu"""
        if not self.file_path:
            messagebox.showerror("Błąd", "Nie wybrano pliku do konwersji!")
            return

        output_format = self.selected_format.get()
        self.output_file = os.path.splitext(self.file_path)[0] + f".{output_format}"

        try:
            if output_format in IMAGE_FORMATS:
                self.convert_image(self.output_file, output_format)
            elif output_format in AUDIO_FORMATS:
                self.convert_audio(self.output_file, output_format)
            elif output_format in VIDEO_FORMATS:
                self.convert_video(self.output_file, output_format)
            messagebox.showinfo("Sukces", f"Plik został przekonwertowany do {output_format}")
            self.download_btn.config(state="normal")  # Włącz przycisk "Pobierz" po zakończeniu konwersji
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się przekonwertować pliku: {str(e)}")

    def convert_image(self, output_file, format):
        """Konwersja pliku obrazu"""
        try:
            img = Image.open(self.file_path)
            if format == "jpg":
                img = img.convert("RGB")  # Usunięcie przezroczystości dla JPEG
                img.save(output_file, "JPEG")
            else:
                img.save(output_file, format.upper())  # png, gif, itp.
        except Exception as e:
            raise

    def convert_audio(self, output_file, format):
        """Konwersja pliku audio"""
        try:
            stream = ffmpeg.input(self.file_path)
            stream = ffmpeg.output(stream, output_file, format=format)
            ffmpeg.run(stream)
        except ffmpeg.Error as e:
            raise

    def convert_video(self, output_file, format):
        """Konwersja pliku wideo"""
        try:
            stream = ffmpeg.input(self.file_path)
            stream = ffmpeg.output(stream, output_file, format=format)
            ffmpeg.run(stream)
        except ffmpeg.Error as e:
            raise

    def download_file(self):
        """Funkcja umożliwia zapisanie przekonwertowanego pliku w wybranej lokalizacji"""
        if not self.output_file:
            messagebox.showerror("Błąd", "Brak przekonwertowanego pliku do pobrania.")
            return

        download_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(self.output_file)[1],
                                                     filetypes=[("Pliki", f"*{os.path.splitext(self.output_file)[1]}")])
        if download_path:
            shutil.copy(self.output_file, download_path)
            messagebox.showinfo("Sukces", f"Plik został pobrany jako: {download_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
