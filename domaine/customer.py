import datetime


class Customer:

    def __init__(self, id: int, first_name: str = None, last_name: str = None, email: str = None,
                 date_birth: datetime = None, job_title: str = None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_birth = date_birth
        self.job_title = job_title
        self.invitations = []

    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __repr__(self) -> str:
        return "Customer " + self.first_name + " " + self.last_name

    def add_invite(self, invitation):
        """
        Ajoute un client à la liste des clients invités
        :param invitation: un client
        """
        self.invitations.append(invitation)

    def get_age(self):
        """
        Calcule l'âge du client en se basant sur la date de naissance
        :return: int qui correspond à l'âge de la personne
        """
        today = datetime.datetime.now()

        age = int(today.year - self.date_birth.year - ((today.month, today.day) < (self.date_birth.month, self.date_birth.day)))
        return age
