Źródło wykorzystanych obrazów: [Chess Pieces Dataset](https://www.kaggle.com/datasets/ninadaithal/chess-pieces-dataset)

Podczas demonstracji kodu na zajęciach użyty został Python 3.10.

W przykładzie `main.py` zbiór rozpakowano w folderze `./datasets` - należy zmodyfikować odpowiednio ścieżkę, jeżeli znajduje się w innym miejscu.

W przykładzie wywołania funkcji `detect_yolo` znajduje się ścieżka do jednego obrazka z podfolderu `test`. Zachęcam do próby także na innych obrazach.

Ponadto, w `detect_yolo` znajduje się ścieżka do konkretnego checkpointa modelu - ścieżkę tę można modyfikować w ramach trenowania kolejnych modeli. Domyślnie pliki .pt znajdować się będą w `./runs/detect/train[numer_treningu]` - w tym podfolderze znajdować się będą także informacje o przebiegu treningu (z dużą liczbą wykresów ;)).

Po sklonowaniu repozytorium należy utworzyć [środowisko wirtualne](https://docs.python.org/3/library/venv.html) (`venv`), 
a następnie je aktywować i zainstalować potrzebne zależności: 
```
pip install -r requirements.txt
```

Uwaga: powyższe kroki pozwalają zainstalować bibliotekę `torch` bez wspaecia dla CUDA. W przypadku chęci użycia GPU do obliczeń, należy dodatkowo uruchomić (np. dla wersji CUDA 11.8):
```
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```
W przypadku pojawienia się po instalacji komunikatu: _WARNING: Failed to remove contents in a temporary directory [tu_ścieżka]'.
  You can safely remove it manually._ - wówczas przed uruchomieniem kodu należy wskazany plik usunąć.


Zachęcam do eksperymentów, powodzenia!
