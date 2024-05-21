```bash
# add flathub remote
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# installing required packages
flatpak install --user --assumeyes flathub org.kde.Platform//6.7 org.kde.Sdk//6.7 com.riverbankcomputing.PyQt.BaseApp//6.7 
```

Local dependencies
- python >= 3.9
- flatpak-builder

Download the application
```bash
git clone https://github.com/rafatosta/TestAppQFileDialog.git
cd TestAppQFileDialog
```

Run in flatpak

```
python run_flatpak.py
```

run local
```
python -m TestAppQFileDialog
```