from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebEngineCore
from PyQt6.QtWebEngineCore import QWebEngineDownloadRequest, QWebEngineSettings
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QStandardPaths, QFileInfo

import os
import sys

os.environ['QT_QPA_PLATFORM'] = 'xcb'
__appname__ = "MainTestApp"

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

       

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.page().profile().downloadRequested.connect(
            self.on_downloadRequested
        )

    
        # Ativando tudo o que tiver de direito
        self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.AutoLoadImages, True)
        self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)


        #self.url = "https://web-push-book.gauntface.com/demos/notification-examples/"
        #self.url ='https://www.bennish.net/web-notifications.html'

        self.url = 'https://demo.borland.com/testsite/download_testpage.php'


        self.page = QtWebEngineCore.QWebEnginePage(self.view)
        self.page.loadFinished.connect(self.load_finished)
        self.page.featurePermissionRequested.connect(self.permission)

        self.view.setPage(self.page)
        self.view.load(QtCore.QUrl(self.url))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)

    def load_finished(self, flag):
        self.page.setFeaturePermission(
            self.page.url(),  QtWebEngineCore.QWebEnginePage.Feature.Notifications,
                                       QtWebEngineCore.QWebEnginePage.PermissionPolicy.PermissionGrantedByUser)

    def permission(self, frame, feature):
            self.page.setFeaturePermission(
                frame, feature,  QtWebEngineCore.QWebEnginePage.PermissionPolicy.PermissionGrantedByUser)
   
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

    def foo(self):
        print("finished")


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
   main()