# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Czym jest repo

Rozwiązania list laboratoryjnych z przedmiotu „Analiza i przetwarzanie obrazów i wideo” (computer vision). Każda lista to osobny katalog `lab-NN/`:

- `LabN_zadanie.ipynb`: notebook od prowadzącego z treścią zadań. Komórki prowadzącego (treść zadania, wczytanie obrazów) zostają nietknięte; rozwiązania trafiają do komórek pod markdownem „Rozwiązanie:”, dalej jako kolejne komórki.
- `LabN_teoria/`: wstęp teoretyczny (PDF) i notebook demo od prowadzącego; tylko do czytania.
- Obrazy wejściowe (`*.bmp`, `*.png`) leżą obok notebooka, bo notebook wczytuje je ścieżką względną (`cv2.imread('Monety_szare.bmp', ...)`). Jeśli lista korzysta z obrazów z innej listy, kopiuje się je do jej katalogu. Materiały od prowadzącego (obrazy, notebooki) bywają w `~/Downloads/Materiały do laboratoriów-*/`.

`main.py` i `README.md` to puste szablony z `uv init`; nie są używane.

## Środowisko i komendy

Python 3.12, zależności w `pyproject.toml` / `uv.lock` (opencv-python, scikit-image, matplotlib, torch/torchvision, jupyter), środowisko w `.venv`.

```bash
uv sync                                    # instalacja zależności
.venv/bin/jupyter nbconvert --to notebook --execute --inplace \
    --ExecutePreprocessor.timeout=1200 lab-02/Lab2_zadanie.ipynb   # wykonanie całego notebooka (z katalogu notebooka liczą się ścieżki obrazów)
```

Nie ma testów ani lintera. Weryfikacja = notebook wykonuje się od początku do końca bez błędów, a wykresy pokazują to, co opisują wnioski.

## Konwencje rozwiązań

- Wszystko po polsku: komentarze, tytuły wykresów, markdown z opisami i wnioskami.
- Styl kodu zwięzły, jak w `lab-01/Lab1_zadanie.ipynb`: małe helpery (`count_objects`, `iou`, `show_grid` itp.) definiowane raz na górze notebooka i reużywane, sweepy parametrów jako wykresy liniowe lub heatmapy, porównania jako siatki `plt.subplots`.
- Zadania są eksperymentalne: chodzi o badanie wpływu parametrów metody i porównanie wyników, nie o jedno rozwiązanie. Tam, gdzie to możliwe, wynik ocenia się liczbowo względem wzorca (np. maska z czystego obrazu, ręcznie zaznaczony wielokąt), a nie tylko na oko.
- Przy badaniu parametru pokazuje się też wartości skrajnie małe i skrajnie duże obok optimum, żeby było widać kontrast.
- Tylko wizualizacje niezbędne do odpowiedzi na pytania z zadania; bez pobocznych porównań.
- Pod każdym zadaniem komórka „**Wnioski (zad. N)**” z odpowiedziami na pytania z treści, oparta na liczbach widocznych na wykresach. Po zmianie eksperymentów wnioski trzeba zaktualizować.
- `plt.rcParams['figure.dpi'] = 72` w komórce z helperami, żeby notebook z wynikami nie puchł (PNG są zapisywane w `.ipynb`).
