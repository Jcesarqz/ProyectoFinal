from PyQt6 import QtWidgets, QtCore
import random
import string
from src.logica.gestorPasskeeper import PassKeeper


class InicioSesion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Configuración de la ventana de inicio de sesión."""
        self.setWindowTitle("Inicio de sesión - PassKeeper")
        self.resize(400, 250)
        self.setStyleSheet("background-color: #F5F5F5;")

        # Etiqueta de título
        self.title_label = QtWidgets.QLabel("Iniciar sesión", self)
        self.title_label.setGeometry(0, 20, 400, 40)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2C3E50;")

        # Campos de entrada para usuario y contraseña
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(100, 80, 200, 30)
        self.username_input.setPlaceholderText("Usuario")
        self.username_input.setStyleSheet("background-color: white; border: 1px solid #BDC3C7; border-radius: 5px;")

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(100, 120, 200, 30)
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: white; border: 1px solid #BDC3C7; border-radius: 5px;")

        # Botón de inicio de sesión
        self.login_button = QtWidgets.QPushButton("Iniciar sesión", self)
        self.login_button.setGeometry(100, 170, 200, 40)
        self.login_button.setStyleSheet(
            "background-color: #3498DB; color: white; font-weight: bold; border-radius: 5px;")
        self.login_button.clicked.connect(self.login)

    def login(self):
        """Verifica las credenciales del usuario."""
        username = self.username_input.text()
        password = self.password_input.text()

        # Verifica las credenciales (cambia esto según tus necesidades)
        if username == "admin" and password == "admin":
            self.accept_login()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def accept_login(self):
        """Cierra la ventana de inicio de sesión y abre la ventana principal."""
        self.close()  # Cierra la ventana de inicio de sesión
        self.main_window = PassKeeperApp()  # Instancia la ventana principal
        self.main_window.show()  # Muestra la ventana principal




class PassKeeperApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.keeper = PassKeeper()
        self.init_ui()

    def init_ui(self):
        """Configuración de la ventana principal de la aplicación."""
        self.setWindowTitle("PassKeeper - Gestor de Contraseñas")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #F5F5F5;")

        # Etiqueta del título
        self.title_label = QtWidgets.QLabel("Gestor de Contraseñas - PassKeeper", self)
        self.title_label.setStyleSheet("color: #2C3E50; font-size: 24px; font-weight: bold;")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Tabla de contraseñas
        self.password_table = QtWidgets.QTableWidget(self)
        self.password_table.setColumnCount(3)
        self.password_table.setHorizontalHeaderLabels(["Servicio", "Usuario", "Contraseña"])
        self.password_table.horizontalHeader().setStretchLastSection(True)

        # Campos de entrada para Servicio, Usuario y Contraseña
        self.service_input = QtWidgets.QLineEdit(self)
        self.service_input.setPlaceholderText("Servicio")
        self.service_input.setStyleSheet("background-color: white; border: 1px solid #BDC3C7; border-radius: 5px;")

        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setPlaceholderText("Usuario")
        self.username_input.setStyleSheet("background-color: white; border: 1px solid #BDC3C7; border-radius: 5px;")

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: white; border: 1px solid #BDC3C7; border-radius: 5px;")

        # Botones para Añadir, Editar y Eliminar
        # Botón "Añadir"
        # Botón "Añadir"
        self.add_button = QtWidgets.QPushButton("Añadir", self)
        self.add_button.setFixedSize(300, 80)  # Tamaño más grande: 300x80
        self.add_button.setStyleSheet(
            "background-color: #2C3E50; color: white; font-weight: bold; border-radius: 10px;")
        self.add_button.clicked.connect(self.add_password)

        # Botón "Editar"
        self.edit_button = QtWidgets.QPushButton("Editar", self)
        self.edit_button.setFixedSize(300, 80)  # Tamaño más grande: 300x80
        self.edit_button.setStyleSheet(
            "background-color: #2C3E50; color: white; font-weight: bold; border-radius: 10px;")
        self.edit_button.clicked.connect(self.edit_password)

        # Botón "Eliminar"
        self.delete_button = QtWidgets.QPushButton("Eliminar", self)
        self.delete_button.setFixedSize(300, 80)  # Tamaño más grande: 300x80
        self.delete_button.setStyleSheet(
            "background-color: #E74C3C; color: white; font-weight: bold; border-radius: 10px;")
        self.delete_button.clicked.connect(self.confirm_delete)

        # Botón "Generar Contraseña"
        self.generate_button = QtWidgets.QPushButton("Generar Contraseña", self)
        self.generate_button.setFixedSize(300, 80)  # Tamaño más grande: 300x80
        self.generate_button.setStyleSheet(
            "background-color: #3498DB; color: white; font-weight: bold; border-radius: 10px;")
        self.generate_button.clicked.connect(self.generate_password)

        # Botón "Generar Contraseña"
        self.generate_button = QtWidgets.QPushButton("Generar Contraseña", self)
        self.generate_button.setFixedSize(300, 80)  # Tamaño más grande: 300x80
        self.generate_button.setStyleSheet(
            "background-color: #3498DB; color: white; font-weight: bold; border-radius: 10px;")
        self.generate_button.clicked.connect(self.generate_password)

        # Layout principal con los elementos a la izquierda y derecha
        main_layout = QtWidgets.QHBoxLayout()

        # Layout para la tabla (izquierda)
        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.password_table)
        left_layout.addWidget(self.service_input)
        left_layout.addWidget(self.username_input)
        left_layout.addWidget(self.password_input)

        # Layout para los botones (derecha)
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.add_button)
        right_layout.addWidget(self.edit_button)
        right_layout.addWidget(self.delete_button)
        right_layout.addWidget(self.generate_button)

        # Añadir ambos layouts al layout principal
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Widget central y establecimiento del layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Actualizar la tabla con datos al inicio
        self.update_password_table()

    def add_password(self):
        """Añade una nueva contraseña, evitando duplicados de servicio y usuario."""
        service = self.service_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if service and username and password:
            # Verificar si el servicio y usuario ya existen
            for row_idx in range(self.password_table.rowCount()):
                existing_service = self.password_table.item(row_idx, 0).text()
                existing_username = self.password_table.item(row_idx, 1).text()
                if service == existing_service and username == existing_username:
                    QtWidgets.QMessageBox.warning(self, "Advertencia", f"El servicio '{service}' y el usuario '{username}' ya existen.")
                    return

            self.keeper.add_password(service, username, password)
            self.update_password_table()
            self.clear_inputs()

    def edit_password(self):
        """Edita los datos seleccionados en la tabla."""
        selected_row = self.password_table.currentRow()  # Obtiene la fila seleccionada

        if selected_row != -1:  # Verifica que se haya seleccionado una fila
            # Obtiene los datos actuales de la fila seleccionada
            old_service = self.password_table.item(selected_row, 0).text()
            old_username = self.password_table.item(selected_row, 1).text()
            old_password = self.password_table.item(selected_row, 2).text()

            # Rellena los campos de entrada con los valores seleccionados
            self.service_input.setText(old_service)
            self.username_input.setText(old_username)
            self.password_input.setText(old_password)

            # Ahora, el usuario puede modificar los campos de entrada y hacer clic en "Guardar"
            self.save_button = QtWidgets.QPushButton("Guardar cambios", self)
            self.save_button.setGeometry(325, 470, 150, 40)
            self.save_button.setStyleSheet(
                "background-color: #3498DB; color: white; font-weight: bold; border-radius: 10px;")
            self.save_button.clicked.connect(lambda: self.save_edited_password(selected_row, old_service))

            # Añadir el botón a la ventana
            self.save_button.show()

    def save_edited_password(self, selected_row, old_service):
        """Guarda los cambios de la contraseña editada."""
        service = self.service_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if service and username and password:
            # Elimina la contraseña antigua
            self.keeper.delete_password(old_service)

            # Añade la nueva contraseña
            self.keeper.add_password(service, username, password)

            # Actualiza la tabla
            self.update_password_table()

            # Limpia los campos de entrada
            self.clear_inputs()

            # Elimina el botón de guardar cambios
            self.save_button.hide()

    def confirm_delete(self):
        """Muestra una ventana de confirmación antes de eliminar."""
        selected_row = self.password_table.currentRow()
        if selected_row != -1:
            service = self.password_table.item(selected_row, 0).text()
            reply = QtWidgets.QMessageBox.question(self, "Confirmar Eliminación", f"¿Estás seguro de eliminar la contraseña para {service}?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                self.delete_password()

    def delete_password(self):
        """Elimina la contraseña seleccionada."""
        selected_row = self.password_table.currentRow()
        if selected_row != -1:
            service = self.password_table.item(selected_row, 0).text()
            self.keeper.delete_password(service)
            self.update_password_table()

    def update_password_table(self):
        """Actualiza la tabla con las contraseñas almacenadas."""
        passwords = self.keeper.view_passwords()
        self.password_table.setRowCount(len(passwords))
        for row_idx, (service, username, password) in enumerate(passwords):
            service_item = QtWidgets.QTableWidgetItem(service)
            username_item = QtWidgets.QTableWidgetItem(username)
            password_item = QtWidgets.QTableWidgetItem(password)

            # Hacer las celdas no editables
            service_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            username_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            password_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)

            self.password_table.setItem(row_idx, 0, service_item)
            self.password_table.setItem(row_idx, 1, username_item)
            self.password_table.setItem(row_idx, 2, password_item)

    def clear_inputs(self):
        """Limpia los campos de entrada."""
        self.service_input.clear()
        self.username_input.clear()
        self.password_input.clear()

    def generate_password(self):
        """Genera una contraseña aleatoria y la muestra en el campo de entrada."""
        length = 12
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.password_input.setText(generated_password)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_window = InicioSesion()
    login_window.show()  # Muestra la ventana de inicio de sesión primero
    sys.exit(app.exec())
