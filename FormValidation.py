from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import sys

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Form Validation")
        self.setGeometry(100, 100, 400, 350)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        form_layout.addRow(QLabel("Name:"), self.name_input)

        self.email_input = QLineEdit()
        form_layout.addRow(QLabel("Email:"), self.email_input)

        self.age_input = QLineEdit()
        form_layout.addRow(QLabel("Age:"), self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 999 9999 9999")
        form_layout.addRow(QLabel("Phone Number:"), self.phone_input)

        self.address_input = QTextEdit()
        form_layout.addRow(QLabel("Address:"), self.address_input)

        self.gender_dropdown = QComboBox()
        self.gender_dropdown.addItems(["", "Male", "Female", "Other"])
        form_layout.addRow(QLabel("Gender:"), self.gender_dropdown)

        self.education_dropdown = QComboBox()
        self.education_dropdown.addItems(["", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])
        form_layout.addRow(QLabel("Education:"), self.education_dropdown)

        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        shortcut = QShortcut(QKeySequence("Q"), self)
        shortcut.activated.connect(QApplication.quit)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_dropdown.currentText()
        education = self.education_dropdown.currentText()

        if not name or not email or not age or not phone or not address or gender == "" or education == "":
            self.show_error("All fields are required.")
            return

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            self.show_error("Please enter a valid email address.")
            return
        
        if not age.isdigit():
            self.show_error("Please enter a valid age (integer value).")
            return
        
        if len(phone.replace(" ", "")) != 14:
            self.show_error("Please enter a valid 13 digit phone number.")
            return
        
        self.show_success()

    def show_error(self, message):
        QMessageBox.warning(self, "Validation Error", message)

    def show_success(self):
        QMessageBox.information(self, "Success", "Profile saved successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_dropdown.setCurrentIndex(0)
        self.education_dropdown.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
