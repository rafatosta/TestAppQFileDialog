import os

os.system('flatpak-builder build TestAppQFileDialog.yaml --force-clean --ccache --install --user')

os.system('flatpak run com.rtosta.TestAppQFileDialog')
