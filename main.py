import os
import sys
from PyQt5 import QtWidgets, QtGui

class RenameFilesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Bulk File Rename Tool')
        self.setGeometry(100, 100, 500, 300)

        self.initUI()

    def initUI(self):
        # create directory label and line edit
        directory_label = QtWidgets.QLabel('Directory:', self)
        directory_label.move(20, 20)
        self.directory_line_edit = QtWidgets.QLineEdit(self)
        self.directory_line_edit.move(80, 20)
        self.directory_line_edit.resize(300, 25)
        self.directory_line_edit.setReadOnly(True)

        # create directory browse button
        browse_button = QtWidgets.QPushButton('Browse', self)
        browse_button.move(400, 20)
        browse_button.clicked.connect(self.selectDirectory)

        # create prefix label and line edit
        prefix_label = QtWidgets.QLabel('Prefix:', self)
        prefix_label.move(20, 60)
        self.prefix_line_edit = QtWidgets.QLineEdit(self)
        self.prefix_line_edit.move(80, 60)
        self.prefix_line_edit.resize(100, 25)

        # create suffix label and line edit
        suffix_label = QtWidgets.QLabel('Suffix:', self)
        suffix_label.move(200, 60)
        self.suffix_line_edit = QtWidgets.QLineEdit(self)
        self.suffix_line_edit.move(260, 60)
        self.suffix_line_edit.resize(100, 25)

        # create rename button
        rename_button = QtWidgets.QPushButton('Rename', self)
        rename_button.move(400, 60)
        rename_button.clicked.connect(self.renameFiles)

    def selectDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.directory_line_edit.setText(directory)

    def renameFiles(self):
        directory = self.directory_line_edit.text()
        prefix = self.prefix_line_edit.text()
        suffix = self.suffix_line_edit.text()

        if not directory:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please select a directory.')
            return

        files = os.listdir(directory)
        for i, file in enumerate(files):
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, f'{prefix}{i + 1}{suffix}{os.path.splitext(file)[1]}')
            os.rename(old_file_path,os.rename(old_file_path, new_file_path))

        QtWidgets.QMessageBox.information(self, 'Success', 'Files renamed successfully.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RenameFilesWindow()
    window.show()
    sys.exit(app.exec_())
