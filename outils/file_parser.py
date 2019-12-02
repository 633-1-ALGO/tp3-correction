from domaine.customer import Customer
from datetime import datetime


class FileParser:

    def parse_costumers(self, file_content: str) -> list:
        """
        Converti le contenu d'un fichier en une liste de clients
        :param file_content: contenu d'un fichier
        :return: liste de clients
        """
        lines: str = file_content.split("\n")
        costumers: list = []
        for i in range(1, len(lines)):
            line = lines[i]
            fields = line.split(",")
            costumer = Customer(int(fields[0]), fields[1], fields[2], fields[3],
                                datetime.strptime(fields[4], '%m/%d/%Y'), fields[5])
            costumers.append(costumer)
        return costumers

    def parse_relations(self, file_content: str) -> list:
        """
        Converti le contenu d'un fichier en une liste de relations
        :param file_content: contenu d'un fichier
        :return: liste de relations
        """
        lines: str = file_content.split("\n")
        relations: list = []
        for i in range(1, len(lines)):
            line = lines[i]
            fields = line.split(",")

            relations.append([fields[0], fields[1]])

        return relations
