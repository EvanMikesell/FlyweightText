import tkinter
import tkinter.font
from abc import ABC, abstractmethod


# we have to create a tkinter window to create font objects
window = tkinter.Tk()


class Character:
    def __init__(self, char: str):
        self.__unicode_code_point = ord(char)

    def get_unicode(self):
        return self.__unicode_code_point


class Factory(ABC):
    """
    Factory Abstract Class
    Factories are singletons
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Factory, cls).__new__(cls)
        return cls.__instance

    @abstractmethod
    def get_flyweight(self, flyweight_info):
        pass


class FontFactory(Factory):
    def __init__(self):
        self.__flyweights = dict()

    def get_flyweight(self, font_info) -> tkinter.font.Font:
        """
        :param font_info: triple of form (font family, font size, font style)

            font style is a string containing any the following:
                "bold" for boldface or "normal" for regular weight.
                "italic" for italic, "roman" for unslanted.
                underline
                overstrike

                for example, "bold italic underlined", 
                "normal overstrike", "normal", "", etc.

            python's tkinter will use this triple as a font

        :return: tkinter Font object
        """

        if font_info not in self.__flyweights:
            self.__flyweights[font_info] = tkinter.font.Font(font=font_info)

        return self.__flyweights[font_info]


class CharacterFactory(Factory):
    def __init__(self):
        self.__flyweights = dict()

    def get_flyweight(self, char: str) -> Character:

        if char not in self.__flyweights.keys():
            self.__flyweights[char] = Character(char)

        return self.__flyweights[char]
