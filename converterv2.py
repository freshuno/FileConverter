import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import os
import shutil
from PIL import Image
import subprocess

# Set path to ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"  # Ensure this is the correct path

MAX_FILE_SIZE_MB = 200  # Maximum file size in MB

# Supported formats for each file type
IMAGE_FORMATS = ["jpg", "png", "gif"]
AUDIO_FORMATS = ["mp3", "wav", "flac"]
VIDEO_FORMATS = ["mp4", "mov"]

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Converter")
        self.root.geometry("700x300")

        # Label and button for file selection
        self.label = tk.Label(root, text="Select a file to convert:")
        self.label.pack(pady=10)

        self.select_file_btn = tk.Button(root, text="Select File", command=self.load_file)
        self.select_file_btn.pack(pady=5)

        # Label to display the selected file
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=5)

        # Label for selecting the output format
        self.format_label = tk.Label(root, text="Choose output format:")
        self.format_label.pack(pady=10)

        # Format selection menu (dynamically updated)
        self.selected_format = tk.StringVar(root)
        self.format_menu = tk.OptionMenu(root, self.selected_format, "")
        self.format_menu.pack(pady=5)

        # Button to start conversion
        self.convert_btn = tk.Button(root, text="Convert", command=self.convert_file)
        self.convert_btn.pack(pady=20)

        # Button to download converted file, initially disabled
        self.download_btn = tk.Button(root, text="Download", command=self.download_file, state="disabled")
        self.download_btn.pack(pady=10)

        # Path to the selected file
        self.file_path = None
        # Path to the converted file
        self.output_file = None

    def load_file(self):
        """Loads the file selected by the user and checks its size and type."""
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            file_size_mb = os.path.getsize(self.file_path) / (1024 * 1024)  # Size in MB
            if file_size_mb > MAX_FILE_SIZE_MB:
                messagebox.showerror("Error", f"File exceeds maximum size of {MAX_FILE_SIZE_MB} MB!")
                self.file_path = None
                self.file_label.config(text="No file selected")
                self.update_format_options([])  # Clear format options
            else:
                self.file_label.config(text=os.path.basename(self.file_path))
                self.update_format_options(self.get_available_formats(self.file_path))
                self.download_btn.config(state="disabled")  # Disable download until conversion

    def get_available_formats(self, file_path):
        """Returns available target formats depending on the file type."""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower().replace(".", "")

        if ext in IMAGE_FORMATS:
            return [fmt for fmt in IMAGE_FORMATS if fmt != ext]
        elif ext in AUDIO_FORMATS:
            return [fmt for fmt in AUDIO_FORMATS if fmt != ext]
        elif ext in VIDEO_FORMATS:
            return [fmt for fmt in VIDEO_FORMATS if fmt != ext]
        else:
            messagebox.showerror("Error", "Unsupported file type.")
            return []

    def update_format_options(self, formats):
        """Updates available target format options in the format selection menu."""
        self.format_menu["menu"].delete(0, "end")
        for fmt in formats:
            self.format_menu["menu"].add_command(label=fmt, command=tk._setit(self.selected_format, fmt))
        if formats:
            self.selected_format.set(formats[0])  # Set the first format as default
        else:
            self.selected_format.set("")  # Clear format selection

    def convert_file(self):
        """Converts the file to the selected format."""
        if not self.file_path:
            messagebox.showerror("Error", "No file selected for conversion!")
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
            messagebox.showinfo("Success", f"File converted to {output_format}")
            self.download_btn.config(state="normal")  # Enable download button after conversion
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert file: {str(e)}")

    def convert_image(self, output_file, format):
        """Converts image file."""
        try:
            img = Image.open(self.file_path)
            if format == "jpg":
                img = img.convert("RGB")  # Remove transparency for JPEG
                img.save(output_file, "JPEG")
            else:
                img.save(output_file, format.upper())  # e.g., PNG, GIF
        except Exception as e:
            raise

    def convert_audio(self, output_file, format):
        """Converts audio file using ffmpeg."""
        try:
            command = ["ffmpeg", "-i", self.file_path, output_file]
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise

    def convert_video(self, output_file, format):
        """Converts video file using ffmpeg."""
        try:
            command = ["ffmpeg", "-i", self.file_path, output_file]
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise

    def download_file(self):
        """Saves the converted file to a specified location."""
        if not self.output_file:
            messagebox.showerror("Error", "No converted file to download.")
            return

        download_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(self.output_file)[1],
                                                     filetypes=[("Files", f"*{os.path.splitext(self.output_file)[1]}")])
        if download_path:
            shutil.copy(self.output_file, download_path)
            messagebox.showinfo("Success", f"File downloaded as: {download_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
