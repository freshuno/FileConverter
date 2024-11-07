Żeby odpalić aplikacje należy wpisać w terminalu:

- pip install pillow
  
- pip install ffmpeg
  
Ponadto należy pobrać z tej strony plik o nazwie ffmpeg-master-latest-win64-gpl.zip
https://github.com/BtbN/FFmpeg-Builds/releases
![image](https://github.com/user-attachments/assets/665c460f-4b90-4afe-b88a-b2b7266bd15f)

Po pobraniu należy stworzyć folder ffmpeg na dysku C

![image](https://github.com/user-attachments/assets/817b9cce-c267-457a-bfdd-0f45b745f629)
Rozpakować w tym folderze pobrany wcześniej przez nas plik ffmpeg-master-latest-win64-gpl.zip
![image](https://github.com/user-attachments/assets/f6db0380-2aa9-4fbf-8906-816df3dc5ee8)
Kopiujemy ścieżke do pliku bin 
![image](https://github.com/user-attachments/assets/285e376d-b3ee-45e4-bb23-0b7e6dc76479)
C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin
Otwieramy zmienne środowiskowe
![image](https://github.com/user-attachments/assets/43efda13-0636-42c3-99fd-fcae4803f778)
Klikamy zmienne środowiskowe 
![image](https://github.com/user-attachments/assets/75eb6590-07d1-4030-bcd5-31494ecb7c01)
Edytujemy PATH
![image](https://github.com/user-attachments/assets/ce75f44b-cfa9-403f-8cbe-3accf37994fa)
Klikamy NEW i dodajemy naszą ścieżkę C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin
![image](https://github.com/user-attachments/assets/e01b9908-8710-4a4e-8dff-db3186822b1f)
Klikamy OK OK 







# Dokumentacja inżynierii wymagań

Raport zawiera przykładowe elementy wykonanej dokumentacji inżynierii wymagań.

Członkowie zespołu:

•	Macierz kompetencji zespołu.

![image](https://github.com/user-attachments/assets/75052f30-53a8-4870-ae2b-2dea4e9b5de7)


•	W tabeli poniżej umieść zestaw pytań, które zostały sformułowane w celu uszczegółowienia zadanego projektu. Zanotuj odpowiedzi, które pojawiły się w trakcie dyskusji.

![image](https://github.com/user-attachments/assets/94779cb8-2801-46ce-9e3d-17c72d13542f)


•	Ustalony format danych wejściowych.

![image](https://github.com/user-attachments/assets/53bbe107-e8ca-4b3f-8e21-6c2424574632)


•	Modelowanego systemu za pomocą tabeli

![image](https://github.com/user-attachments/assets/61d1d5c0-eadb-4f16-a9ca-2d04bf25bb4f)


•	Przedstawienie modelowanego systemu za pomocą diagramów UML

![image](https://github.com/user-attachments/assets/a171e549-169a-4876-916d-e8a68ff58afd)



Rys. 1 Diagram przypadków użycia
 
![image](https://github.com/user-attachments/assets/eed93643-0166-4987-a721-e3bf696432b8)


Rys. 2 Diagram przepływu danych

•	Diagram sekwencyjny UML
 
![image](https://github.com/user-attachments/assets/fe84840e-6983-44cb-8da2-1fa448104841)


•	Projekt architektury opracowywanego systemu

 ![image](https://github.com/user-attachments/assets/6bf074d8-e9bb-489d-9233-c5214420241f)



Każdy z trzech dużych prostokątów reprezentuje poszczególne komponenty systemu. Zadaniem systemu jest najpierw przyjąć plik do konwersji, aby następnie przetworzyć . Na końcu system udostępia plik do pobrania w docelowym formacie. Pierwszym kluczowym i krytycznym elementem systemu jest sprawdzenie poprawności przesłanego do niego pliku w celu zapewnienia bezbłędnego działania programu. Drugim ważnym komponentem systemu są algorytmy odpowiedzialne za konwertowanie pliku.. Wszystko to stanowi podstawę do wygenerowania pliku docelowego w formacie podanym przez użytkownika.



•	Sugerowany język implementacji: Python
Uzasadnienie:
Python to idealny wybór, ponieważ pozwala tworzyć aplikacje szybciej i taniej . Jest również niezawodny, co oznacza lepszą jakość i łatwiejsze utrzymanie aplikacji w przyszłości.


