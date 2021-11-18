# pdfregnrextractor

## Installation

Install Python:

### Linux

Debian
```bash
sudo apt-get install python3.7
```
Red Hat
```bash
sudo yum install python37
```
Suse
```bash
sudo zypper install python3-3.7
```

verify

```bash
python3 --version
```
#### Install Pip

load install script
```bash
curl -O https://bootstrap.pypa.io/get-pip.py
```
execute it
```bash
python3 get-pip.py --user
```
verify

```bash
pip --version
```
### Windows

Offizielle Python Installation herunterladen: [https://www.python.org/downloads/](https://www.python.org/downloads/) 

CMD öffnen und auf erfolgreiche Installation prüfen

```bash
python --version
```
```bash
pip --version
```


## Abhängigkeiten installieren und Skript ausführen 

Alle zu extrahierenden PDF-Dateien in den Ordner 'pdfs' des Projekts legen.
Via CMD in das Projekt navigieren



e.g.

```bash
cd ~/pdfregnrextractor
```

Abhängigkeiten installieren

```bash
pip install fitz
pip install -U PyMuPDF
```

Skript starten:

```bash
python main.py
```

Die Datei registrierungsnummern.csv wird überschrieben und beinhaltet eine Liste aller erfolgreich extrahierten Registrierungsnummern. 


## Issues / TODO's / Hinweise

### Logs: 
Die genutzte Bibliothek fitz basiert auf mupdf. Mupdf scheint Font-files e.g. arial.ttf nicht zu unterstützen, wodurch folgender Fehler/Hinweis ausgeschrieben wird:
```bash
mupdf: FT_New_Memory_Face(Arial): unknown file format
```
Für die Zwecke des Projekts spielt dies jedoch keine Rolle.

## Weitere Interessante Bibliotheken

### pdfminer
Basiert lediglich auf Python, anders als das genutzte PyMuPdf, welches auf MuPDF basiert.
PDFMiner scheint sehr mächtig zu sein. In der Handhabung ist es jedoch etwas komplizierter, als PyMuPdf und scheint etwas langsamer zu sein.

### PyPDF2

Weniger mächtig, als pdfminer und MuPDF. Zudem weniger zuverlässig, bei der Textextraktion und fehleranfälliger.


