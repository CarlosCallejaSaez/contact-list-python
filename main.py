class Contact:
    """
    Representa un contacto con nombre, teléfono y email.
    """

    def __init__(self, name, tel, email):
        """
        Inicializa un objeto de contacto con nombre, teléfono y email.

        Args:
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono del contacto.
            email (str): Dirección de correo electrónico del contacto.
        """
        self.name = name
        self.tel = tel
        self.email = email

class Agenda:
    """
    Representa una lista de contactos y proporciona métodos para gestionarla.
    """

    def __init__(self):
        """
        Inicializa una nueva agenda vacía.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Agrega un nuevo contacto a la agenda.

        Args:
            contacto (Contacto): Objeto de la clase Contacto a añadir a la agenda.
        """
        self.contacts.append(contact)

    def show_contacts(self):
        """
        Muestra todos los contactos en la agenda o un mensaje si no hay contactos.
        """
        if not self.contacts:
            print("No tiene contactos en su lista de contactos.")
        else:
            print(f"Usted tiene {len(self.contacts)} contacto/s en su lista de contactos:")
            for contact in self.contacts:
                print(f"Nombre: {contact.name}")
                print(f"Teléfono: {contact.tel}")
                print(f"Email: {contact.email}")
                print("-" * 20)

    def find_contact(self, name):
        """
        Busca un contacto por nombre en la agenda.

        Args:
            nombre (str): Nombre del contacto a buscar.

        Returns:
            Contacto or None: Retorna el objeto de contacto si se encuentra, None si no se encuentra.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        """
        Elimina un contacto por nombre de la agenda.

        Args:
            nombre (str): Nombre del contacto a eliminar.
        """
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"{name} ha sido eliminado.")
        else:
            print(f"El contacto {name} no se encontraba en su lista de contactos.")

def main():
    """
    Función principal del programa. Permite al usuario interactuar con la agenda de contactos.
    """
    agenda = Agenda()

    while True:
        print("1. Añadir contacto")
        print("2. Mostrar todos los contactos")
        print("3. Encontrar un contacto")
        print("4. Borrar contacto")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre: ")
            tel = input("Teléfono: ")
            email = input("Email: ")
            new_contact = Contact(name, tel, email)
            agenda.add_contact(new_contact)
            print("Contacto añadido.")
        elif choice == "2":
            agenda.show_contacts()
        elif choice == "3":
            name = input("Introduce el nombre del contacto: ")
            contact = agenda.find_contact(name)
            if contact:
                print(f"Nombre: {contact.name}")
                print(f"Teléfono: {contact.tel}")
                print(f"Email: {contact.email}")
            else:
                print(f"El contacto {name} no ha sido encontrado.")
        elif choice == "4":
            name = input("Introduce el nombre del contacto que quieres borrar: ")
            agenda.delete_contact(name)
        elif choice == "5":
            print("¡Hasta la próxima!")
            break
        else:
            print("Por favor, escoge una opción válida.")

if __name__ == "__main__":
    main()
