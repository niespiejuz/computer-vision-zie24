Źródło wykorzystanych obrazów: [Melanoma dataset](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images)

Podczas demonstracji kodu na zajęciach użyty został Python 3.10.

Skrypty wykonują podział wszystkich plików w folderze na zbiory: treningowy, walidacyjny, testowy. 
Używając powyższego linku, można po pobraniu odpowiednio ręcznie złączyć zawartość gotowych folderów 
`train` i  `test` lub przekazać ścieżkę np. wyłącznie do folderu `train`. Ważne, by wewnątrz przekazanego
folderu znajdowały się dwa podfoldery: `benign` oraz `malignant`.

Po sklonowaniu repozytorium należy podać ścieżkę do przygotowanego jak opisane powyżej zbioru (`dataset_dir`), 
utworzyć [środowisko wirtualne](https://docs.python.org/3/library/venv.html) (`venv`), 
a następnie je aktywować i zainstalować potrzebne zależności: ```pip install -r requirements.txt```.

Następny krok to uruchomienie skryptów, porównanie - i eksperymenty z parametrami sieci, ich wielkością, 
zbiorami, przetwarzaniem wstępnym oraz wszystkim innym, co ciekawi :)

Powodzenia!