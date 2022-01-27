from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow, QAbstractItemView, QHeaderView, QHBoxLayout, \
    QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5.QtGui import QIcon
from TableWidget import PyTableWidget
import sys
from portal_fetch import fetchPortal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Portal HCMUS')
        self.setWindowIcon(QIcon('favicon.ico'))
        self.setMinimumSize(800, 400)
        self.setMaximumSize(800, 400)
        self.setStyleSheet('background-color: #21252d')
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)
        self.table_widget = PyTableWidget()

        self.top_layout = QHBoxLayout()
        self.reload_button = QPushButton('Reload')
        self.reload_button.clicked.connect(self.setupTable)
        self.reload_button.setMaximumWidth(100)
        self.reload_button.setStyleSheet('color: #111;\n'
                                         'background-color: #568af2;\n'
                                         'border-radius: 8px')
        self.top_layout.addWidget(self.reload_button)

        # Main Layout
        self.mainLayout.addLayout(self.top_layout)
        self.mainLayout.addWidget(self.table_widget)

        self.setup_window()
        self.show()

    def setup_window(self):
        self.setupTable()

    def setupTable(self):
        self.table_widget.clear()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("ID")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Subject")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Grade")

        try:
            dataDict = fetchPortal()
        except:
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Message')
            dialog.setText('Fetch Data FAIL')
            dialog.setStyleSheet('color: #8a95aa')
            dialog.show()
            return
        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for code in dataDict:
            name, point = dataDict[code][0], dataDict[code][1]
            n = self.table_widget.rowCount()
            self.table_widget.insertRow(n)
            self.table_widget.setItem(n, 0, QTableWidgetItem(code))
            self.table_widget.setItem(n, 1, QTableWidgetItem(name))
            point_text = QTableWidgetItem()
            point_text.setTextAlignment(Qt.AlignCenter)
            point_text.setText(point)
            self.table_widget.setItem(n, 2, point_text)
            self.table_widget.setRowHeight(n, 22)

        dialog = QMessageBox(self)
        dialog.setWindowTitle('Message')
        dialog.setText('Fetch Data Success')
        dialog.setStyleSheet('color: #8a95aa')
        dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = MainWindow()
    sys.exit(app.exec())
