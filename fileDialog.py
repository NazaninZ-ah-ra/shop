import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog


class FileOpenDialog(QWidget):

    # Open single file dialog
    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            parent=self,
            directory="",
            caption="Open Image",
            filter="Image Files (*.jpg *.png)"
        )
        if fileName:
            return fileName
        else:
            return None

    # Open multiple files
    def openFileNamesDialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Open Files",
            directory="",
            filter="Text Files (*.txt);;All Files (*)"
        )
        if files:
            print(files)

    # Save file dialog
    def saveFileDialog(self):
        fileName, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save File",
            directory="",
            filter="Text Files (*.txt)"
        )
        if fileName:
            return fileName
        else:
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOpenDialog()
    window.show()
    sys.exit(app.exec_())
