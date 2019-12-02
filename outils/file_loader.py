class FileLoader:

    def load(self, path: str) -> str:
        """
        Charge un fichier donné
        :param path: Le chemin d'accès vers le fichier voulu
        :return: Un string qui correspond au contenu du fichier
        """
        return open(path, 'r').read()
