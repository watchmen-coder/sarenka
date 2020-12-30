"""
Moduł do przechowywania danych użytkownika takich jak klucze do serwisów,
które wymagają kont dla korzystania z ich api i/lub funkcjonalności.
"""
import json
from .censys_credentials import CensysCredentials
from .shodan_credentials import ShodanCredentials

class UserCredentialsError(Exception):
    """
    Zgłoszenie wyjąktu gdy są problemy z danymi użytkownika do serwisów trzecich.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class UserCredentials:
    """Singleton - Klasa przechowująca dane użytkownika do serwisów trzecich niezbędne do korzystania z ich funkcjonalności."""
    __instance = None
    __config_file = "user_credentials.json"

    def __init__(self):

        if not UserCredentials.__instance:
            try:
                with open(self.__config_file) as f:
                    data = json.load(f)
            except FileNotFoundError:
                raise UserCredentialsError("User credential file does not exist. "
                                           "Create file sarenka/backend/api_searcher/search_engines/user_credentials.json "
                                           "or clone from repository https://github.com/pawlaczyk/sarenka")

            self.__censys = CensysCredentials(data["censys"])
            self.__shodan = ShodanCredentials(data["shodan"])
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = UserCredentials()
        return cls.__instance

    @property
    def censys(self):
        return self.__censys

    @property
    def shodan(self):
        return self.__shodan