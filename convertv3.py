import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import threading
from PIL import Image
import subprocess
import shutil
import time

MAX_FILE_SIZE_MB = 201
QUALITY = 80

# Obsługiwane formaty
IMAGE_FORMATS = ["jpg", "png", "gif"]
AUDIO_FORMATS = ["mp3", "wav", "flac"]
VIDEO_FORMATS = ["mp4", "mov"]

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Converter")
        self.root.geometry("700x400")

        self.label = tk.Label(root, text="Wybierz plik do konwersji:")
        self.label.pack(pady=10)
        self.select_file_btn = tk.Button(root, text="Wybierz plik", command=self.load_file)
        self.select_file_btn.pack(pady=5)
        self.file_label = tk.Label(root, text="Nie wybrano pliku")
        self.file_label.pack(pady=5)

        self.format_label = tk.Label(root, text="Wybierz format wyjściowy:")
        self.format_label.pack(pady=10)
        self.selected_format = tk.StringVar(root)
        self.format_menu = tk.OptionMenu(root, self.selected_format, "")
        self.format_menu.pack(pady=5)

        self.convert_btn = tk.Button(root, text="Konwertuj", command=self.start_conversion)
        self.convert_btn.pack(pady=20)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.download_btn = tk.Button(root, text="Pobierz", command=self.download_file, state="disabled")
        self.download_btn.pack(pady=10)

        self.file_path = None
        self.output_file = None

    def load_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            file_size_mb = os.path.getsize(self.file_path) / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                messagebox.showerror("Błąd", f"Plik przekracza maksymalny rozmiar {MAX_FILE_SIZE_MB} MB!")
                self.file_path = None
                self.file_label.config(text="Nie wybrano pliku")
                self.update_format_options([])
            else:
                self.file_label.config(text=os.path.basename(self.file_path))
                self.update_format_options(self.get_available_formats(self.file_path))
                self.download_btn.config(state="disabled")

    def get_available_formats(self, file_path):
        _, ext = os.path.splitext(file_path)
        ext = ext.lower().replace(".", "")
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
        self.format_menu["menu"].delete(0, "end")
        for fmt in formats:
            self.format_menu["menu"].add_command(label=fmt, command=tk._setit(self.selected_format, fmt))
        if formats:
            self.selected_format.set(formats[0])
        else:
            self.selected_format.set("")

    def start_conversion(self):
        if not self.file_path:
            messagebox.showerror("Błąd", "Nie wybrano pliku do konwersji!")
            return

        # Uruchamiamy konwersję w nowym wątku
        self.progress_bar["value"] = 0
        self.convert_btn.config(state="disabled")  # Wyłącz przycisk konwersji
        threading.Thread(target=self.convert_file).start()

    def convert_file(self):
        output_format = self.selected_format.get()
        self.output_file = os.path.splitext(self.file_path)[0] + f".{output_format}"

        try:
            if output_format in IMAGE_FORMATS:
                self.convert_image(self.output_file, output_format)
            elif output_format in AUDIO_FORMATS:
                self.convert_audio(self.output_file, output_format)
            elif output_format in VIDEO_FORMATS:
                self.convert_video(self.output_file, output_format)

            # Aktualizacja paska postępu w trakcie konwersji
            for i in range(1, 101):  # Symulacja postępu w 100 krokach
                self.progress_bar["value"] = i
                time.sleep(0.05)  # Symulacja krótkiego opóźnienia przetwarzania

            messagebox.showinfo("Sukces", f"Plik został przekonwertowany na {output_format}")
            self.download_btn.config(state="normal")  # Włącz przycisk pobierania
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się przekonwertować pliku: {str(e)}")
        finally:
            self.progress_bar.stop()  # Zatrzymaj pasek postępu
            self.convert_btn.config(state="normal")  # Włącz ponownie przycisk konwersji

    def convert_image(self, output_file, format):
        img = Image.open(self.file_path)
        if format == "jpg":
            img = img.convert("RGB")
            img.save(output_file, "JPEG", quality=QUALITY)
        else:
            img.save(output_file, format.upper())

    def convert_audio(self, output_file, format):
        # Ustaw wyższy bitrate dla lepszej jakości
        command = ["ffmpeg", "-i", self.file_path, "-b:a", "256k", output_file]
        subprocess.run(command, check=True)

    def convert_video(self, output_file, format):
        # Ustaw niższy CRF dla wyższej jakości
        command = ["ffmpeg", "-i", self.file_path, "-crf", "18", output_file]
        subprocess.run(command, check=True)

    def download_file(self):
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
