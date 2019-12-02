from domaine.customer import Customer


class CustomerTree:

    def __init__(self) -> None:
        super().__init__()
        self.root: Customer = None
        self.size = 0

    def build_tree(self, costumers: list, relations: list) -> None:
        """
        Utilise les listes de clients et de relations pour créer un arbre
        :param costumers: liste de clients
        :param relations: liste de relations
        """
        for relation in relations:
            costumers[int(relation[0]) - 1].add_invite(costumers[int(relation[1]) - 1])
        self.root = costumers[0]
        self.size = len(costumers)

    def add(self, customer: Customer, to: Customer) -> None:
        """
        Ajoute un client à l'arbre
        :param customer: client à ajouter à l'arbre
        :param to: client qui a invité le client à ajouter
        """
        to.add_invite(customer)
        self.size += 1

    def remove(self, customer: Customer) -> None:
        """
        Supprime un client de l'arbre. Supprime également tous les fils de ce client
        :param customer: Le client à supprimer
        """
        if customer == self.root:
            self.root = None
            self.size = 0
        elif not self.__remove(self.root, customer):
            raise Exception("Ce client n'existe pas !")

        self.size = self.determine_size()

    def __remove(self, current: Customer, customer: Customer) -> bool:
        for i in range(len(current.invitations)):
            c = current.invitations[i]
            if c == customer:
                current.invitations.pop(i)
                return True
            found: Customer = self.__remove(customer, c)
            if found:
                return True

        return False

    def determine_size(self) -> int:
        """
        Determiner la taille totale de l'arbre
        :return: taille de l'arbre
        """
        size: int = 0
        if self.root is not None:
            size = self.__count_elements(self.root, size)
        return size

    def __count_elements(self, current: Customer, size:int) -> int:
        """
        Compter tous les éléments de l'arbre
        :param current: noeud actuel
        :param size: taille courrante de l'arbre
        :return: retourne la taille incrémentée
        """
        size += 1
        for customer in current.invitations:
            size = self.__count_elements(customer, size)
        return size

    def get(self, customer: Customer) -> Customer:
        """
        Retourne un élément de l'arbre
        :param customer: Le client à trouver
        :return: le client trouvé
        """
        return self.__get_customer(self.root, customer)

    def __get_customer(self, current: Customer, to_find: Customer) -> Customer:
        if current == to_find:
            return current

        for customer in current.invitations:
            found: Customer = self.__get_customer(customer, to_find)
            if found is not None:
                return found

        return None

    def get_average_age(self) -> float:
        """
        Calcule la moyenne d'âge des clients présents dans l'arbre
        :return: la moyenne d'âge
        """
        if self.size == 0:
            return 0.0
        return self.__get_sum_ages(self.root) / self.size

    def __get_sum_ages(self, current: Customer) -> int:
        sum_ages = current.get_age()

        for customer in current.invitations:
            sum_ages += self.__get_sum_ages(customer)

        return sum_ages

    def get_average_invitations(self) -> float:
        """
        Calcule le nombre d'invitations moyen par client
        :return: la moyenne des invitations
        """
        if self.size == 0:
            return 0.0
        return self.__get_sum_invitations(self.root) / self.size

    def __get_sum_invitations(self, current: Customer):
        sum_invitations = len(current.invitations)

        for customer in current.invitations:
            sum_invitations += self.__get_sum_invitations(customer)

        return sum_invitations

    def get_row(self, n_row: int):
        """
        Retourne une liste contenant les clients se trouvant à une certaine profondeur
        :param n_row: numéro de la profondeur
        :return: liste de clients
        """
        customers = []
        self.__get_row(self.root, customers, n_row, 1)
        return customers

    def __get_row(self, current: Customer, customers: list, n_row: int, current_row: int):
        if current_row == n_row:
            customers.append(current)
            return

        for customer in current.invitations:
            self.__get_row(customer, customers, n_row, current_row + 1)

    def linear_sort_by_job(self, job_contains: str) -> list:
        """
        Retourne une liste triée contenant les clients dont leur job contient un certain string au début de la liste.
        Par exemple, tous les "IT" au début de la liste et ensuite les autres.
        :param job_contains: le contenu à chercher dans le job des clients
        :return: liste de clients
        """
        list_customers = [None] * self.size
        self.__sort_by_job(self.root, job_contains, list_customers, 0, self.size - 1)
        return list_customers

    def __sort_by_job(self, current: Customer, job_contains: str, list_customers: list, start: int, end: int):
        if start > end:
            return start, end
        else:
            if job_contains in current.job_title:
                list_customers[start] = current
                start += 1
            else:
                list_customers[end] = current
                end -= 1

            for customer in current.invitations:
                start, end = self.__sort_by_job(customer, job_contains, list_customers, start, end)
            return start, end

    def linear_sort_by_class_age(self, classes: list):
        """
        Retourne une matrice contenant n-classes. Chaque ligne de cette liste contient les clients se trouvant
        dans une classe d'âge donnée
        :param classes: liste de classes d'âge - [10, 15, 20, 25]
                                                Ceci veut dire que vous avez 3 classes d'âge (ou 3 listes) :
                                                [10, 15[, [15, 20[, [20, 25[

        :return: matrice contenant les clients se trouvant dans une classe d'âge
        """
        sorted_classes = []
        for i in range(len(classes) - 1):
            sorted_classes.append([])

        self.__sort_by_classes(self.root, classes, sorted_classes)
        return sorted_classes

    def __sort_by_classes(self, current: Customer, classes: list, sorted_classes: list):
        for i in range(len(classes) - 1):
            if classes[i] <= current.get_age() < classes[i + 1]:
                sorted_classes[i].append(current)

        for costumer in current.invitations:
            self.__sort_by_classes(costumer, classes, sorted_classes)

    def __str__(self) -> str:
        """
        Retourne une représentation en string de l'arbre sous la forme suivante :
        Customer Remy Reese
        |__Customer Allison Bingham
        ||__Customer Julius Morrison
        |||__Customer Alba Ripley
        ....
        |__Customer Barney Curtis
        ||__Customer Cristal Gardner
        |||__Customer Abdul Archer
        ||||__Customer Barry Ranks
        ||||__Customer ...

        :return: représentation de l'arbre
        """
        return self.__show(self.root)

    def __show(self, customer: Customer, tab: str = "|") -> str:
        msg: str = ""
        msg += customer.__str__() + "\n"
        if len(customer.invitations) == 0:
            return msg
        for c in customer.invitations:
            msg += tab + "__" + self.__show(c, tab + "|")
        return msg
