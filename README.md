> **Dokumentacja inżynierii wymagań**
>
> **Raport zawiera przykładowe elementy wykonanej dokumentacji
> inżynierii wymagań.**
>
> **Członkowie zespołu:**

-   *Macierz kompetencji zespołu.*

+:-------------------+:--------------:+:--------------:+:------------:+
| > **Kompetencje**  | > **Filip      | > **Wojciech   | > **Jakub    |
|                    | > Kubala**     | > Barnaś**     | > Wiatr**    |
+--------------------+----------------+----------------+--------------+
| > Programowanie    | > Posiada      | > Posiada      | > Posiada    |
| > Java             |                |                |              |
+--------------------+----------------+----------------+--------------+
| > Programowanie    | > Posiada      | > Posiada      | > Posiada    |
| > C/C++            | > (podstawy)   | > (podstawy)   | > (podstawy) |
+--------------------+----------------+----------------+--------------+
| > Znajomość UML    | > Pos          | > Posiada      | > Posiada    |
|                    | iada(podstawy) |                |              |
+--------------------+----------------+----------------+--------------+
| > Tworzenie        | > Po           | > Posiada      | > Posiada    |
| > interfejsu       | siada(podstawy |                |              |
| > użytkownika      |                |                |              |
+--------------------+----------------+----------------+--------------+
| > Programowanie    | > Posiada      | > Posiada      | > Posiada    |
| > Python           | > (podstawy)   |                |              |
+--------------------+----------------+----------------+--------------+
| > Testowanie       | > Nie posiada  | > Nie posiada  | > Nie        |
| > oprogramowania   |                |                | > posiada    |
+--------------------+----------------+----------------+--------------+

-   *W tabeli poniżej umieść zestaw pytań, które zostały sformułowane w
    celu uszczegółowienia zadanego projektu. Zanotuj odpowiedzi, które
    pojawiły się w trakcie dyskusji.*

+:--------------------+:----------------------------+:-----------------+
| > **Pytanie**       | > **Odpowiedź**             | > **Uwagi**      |
+---------------------+-----------------------------+------------------+
| **Jaka dopuszczalna | 20%                         |                  |
| utrata jakości?**   |                             |                  |
+---------------------+-----------------------------+------------------+
| > **Czy powinien    | > Nie.                      |                  |
| > być robiony       |                             |                  |
| > backup pliku?**   |                             |                  |
+---------------------+-----------------------------+------------------+
| > **Jakie formaty   | > IMG: JPEG, PNG, GIF,\     |                  |
| > mają być          | > AUDIO: MP3, WAV, FLAC,    |                  |
| > obłsugiwane?**    | > VIDEO: MP4,MOV            |                  |
+---------------------+-----------------------------+------------------+
| > **Czy nowy plik   | > Nowy plik jako kopia.     |                  |
| > ma zastępować     |                             |                  |
| > stary czy być     |                             |                  |
| > jego kopią?**     |                             |                  |
+---------------------+-----------------------------+------------------+
| > **Jak dokładnie   | > \<zdjęcie\>               |                  |
| > ma wyglądać       |                             |                  |
| > interfejs?**      |                             |                  |
+---------------------+-----------------------------+------------------+
| > **Jaki maksymalny | > 200 MB                    |                  |
| > rozmiar pliku?**  |                             |                  |
+---------------------+-----------------------------+------------------+
| > **Jaki maksymalny | > 5 min                     |                  |
| > dopuszczalny czas |                             |                  |
| > przetwarzania     |                             |                  |
| > pliku?**          |                             |                  |
+---------------------+-----------------------------+------------------+

> *Czy wszystkie wymagania klienta są możliwe do spełnienia? TAK*

-   *Ustalony format danych wejściowych.*

+:----------------------+:---------------------+:----------------------+
| > **IMG**             | > **AUDIO**          | > **VIDEO**           |
+-----------------------+----------------------+-----------------------+
| > **JPEG,**           | > **MP3,**           | > **MP4,**            |
| >                     | >                    | >                     |
| > **PNG,**            | > **WAV,**           | > **MOV**             |
| >                     | >                    |                       |
| > **GIF**             | > **FLAC**           |                       |
+-----------------------+----------------------+-----------------------+

-   *Modelowanego systemu za pomocą tabeli*

+:------------+:-------------------------------------------------------+
| >           | > *Konwerter*                                          |
| ***Aktor*** |                                                        |
+-------------+--------------------------------------------------------+
| >           | > *Celem działania aplikacji jest konwersja plików na  |
|  ***Opis*** | > podany przez użytkownika format.*                    |
+-------------+--------------------------------------------------------+
| >           | > *Plik przesłany przez użytkownika.*                  |
|  ***Dane*** |                                                        |
+-------------+--------------------------------------------------------+
| > ***W      | > *Użytkownik przesyła plik i wybiera format na jaki   |
| yzwalacz*** | > chce go zamienić.*                                   |
+-------------+--------------------------------------------------------+
| > ***O      | > *Plik w formacie wybranym przez użytkownika.*        |
| dpowiedź*** |                                                        |
+-------------+--------------------------------------------------------+
| >           | > *Plik nie może przekroczyć 200 MB.*                  |
| ***Uwagi*** |                                                        |
+-------------+--------------------------------------------------------+

-   *Przedstawienie modelowanego systemu za pomocą diagramów UML*

> *Rys. 1 Diagram przypadków użycia*
>
> *Rys. 2 Diagram przepływu danych*

-   *Diagram sekwencyjny UML*

<!-- -->

-   *Projekt architektury opracowywanego systemu*

> *Każdy z trzech dużych prostokątów reprezentuje poszczególne
> komponenty systemu. Zadaniem systemu jest najpierw przyjąć plik do
> konwersji, aby następnie przetworzyć . Na końcu system udostępia plik
> do pobrania w docelowym formacie. Pierwszym kluczowym i krytycznym
> elementem systemu jest sprawdzenie poprawności przesłanego do niego
> pliku w celu zapewnienia bezbłędnego działania programu. Drugim ważnym
> komponentem systemu są algorytmy odpowiedzialne za konwertowanie
> pliku.. Wszystko to stanowi podstawę do wygenerowania pliku docelowego
> w formacie podanym przez użytkownika.*

-   *Sugerowany język implementacji: Python*

> *Uzasadnienie:*
>
> *Python to idealny wybór, ponieważ pozwala tworzyć aplikacje szybciej
> i taniej . Jest również niezawodny, co oznacza lepszą jakość i
> łatwiejsze utrzymanie aplikacji w przyszłości.*
