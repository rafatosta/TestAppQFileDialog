from PyQt6 import QtWidgets
from PyQt6.QtWebEngineCore import QWebEngineDownloadRequest, QWebEngineSettings, QWebEnginePage, QWebEngineProfile
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QStandardPaths, QFileInfo, QUrl

from PyQt6.QtWebEngineWidgets import QWebEngineView

import os
import sys

__user_agent__ = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
__whatsapp_url__ = 'https://web.whatsapp.com/'

class Browser(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        # definição do pergil do usuário, local que será armazenados os cookies e informações sobre os navegadores
        self.profile = QWebEngineProfile(self)
        self.profile.setHttpUserAgent(__user_agent__)
        self.profile.downloadRequested.connect(self.on_downloadRequested)

        # Ativando tudo o que tiver de direito
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.AutoLoadImages, True)
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        self.settings().setAttribute(
            QWebEngineSettings.WebAttribute.FocusOnNavigationEnabled, True)
        self.settings().setAttribute(
            QWebEngineSettings.WebAttribute.ScrollAnimatorEnabled, True)

        # Cria a WebPage personalizada
        self.whats = WhatsApp(self.profile, self)
        self.setPage(self.whats)
        self.load(QUrl(__whatsapp_url__))

    
    def on_downloadRequested(self, download:QWebEngineDownloadRequest):
        directory=QStandardPaths.writableLocation(
                QStandardPaths.StandardLocation.DownloadLocation)
        
        file_name = download.downloadFileName()  # download.path()
        suffix = QFileInfo(file_name).suffix()
        path, _ = QFileDialog.getSaveFileName(
            self, "Save File", os.path.join(directory,file_name), "*." + suffix
        )
        if path:   
            download.setDownloadFileName(os.path.basename(path))
            download.setDownloadDirectory(os.path.dirname(path))
            download.accept()

class WhatsApp(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        QWebEnginePage.__init__(self, *args, **kwargs)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.view = Browser()
       
        self.setCentralWidget(self.view)

    


def main():
    #os.environ['QT_QPA_PLATFORM'] = 'xcb'
    os.environ['QT_DEBUG_PLUGINS'] = '1'

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
   main()