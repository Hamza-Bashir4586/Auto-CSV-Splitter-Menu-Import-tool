import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QDropEvent, QFont
import csv

class Hamza_CSVSplitterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hamza's CSV Splitter App")
        self.setGeometry(700, 500, 700, 500)

        self.layout = QVBoxLayout()

        self.label = QLabel('Drag and drop a CSV file here')
        
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.label.setFont(QFont('Times', 10))

        self.download_button = QPushButton('Download Split Files')
        self.download_button.setFont(QFont('Times', 10))
        self.download_button.clicked.connect(self.split_and_download)
        self.layout.addWidget(self.download_button)

        self.setLayout(self.layout)

        # Enable drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.label.setText(f'Selected file: {file_path}')
            self.input_file_path = file_path
            self.download_button.setText(f'Download Split Files')

    def split_and_download(self):
        if hasattr(self, 'input_file_path'):
            # Perform CSV splitting logic
            input_file_path = self.input_file_path
            download_folder = os.path.expanduser("~/Downloads")
            
            # Create a new split folder with a timestamp in "HH_MM - yyyy" format
            timestamp = QDateTime.currentDateTime().toString("HH_mm_ss_-_yyyy")
            folder_name = f'split_folder_{timestamp}'
            folder_path = os.path.join(download_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            new_file_path = os.path.join(folder_path, 'split_file_1.csv')
            amt_file = 1

            with open(input_file_path, 'r', encoding='utf-8') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
            
                r_amt = 1
            
                csv_file = open(new_file_path, 'w', newline='')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(header)

                for row in csvreader:
                    #print(row[0])
                    csv_writer.writerow(row)
                    
                    r_amt += 1

                    if r_amt == 4000:
                        try: 
                            rw = next(csvreader)
                        except StopIteration:
                            break

                        prev_famt = amt_file
                        amt_file += 1
                        r_amt = 1

                        new_file_path = os.path.join(folder_path, f'split_file_{amt_file}.csv')
                        csv_file.close()
                    
                        csv_file = open(new_file_path, 'w', newline='')
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(header)
                csv_file.close()


            self.label.setText(f'File Split Complete \n\n - drag another - ')  
            self.download_button.setText(f'Re - download Split Files')
            print(f'Split files saved in: {folder_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Hamza_CSVSplitterApp()
    window.show()
    sys.exit(app.exec_())
