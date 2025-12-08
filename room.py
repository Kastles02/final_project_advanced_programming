class Room:
    def __init__(self,name,size,computers,person_size,availability,projector):
        self.__name = name
        self.__size = size
        self.__computers = computers
        self.__person_size = person_size
        self.__availability = availability
        self.__projector = projector
    def set_name(self,name):
        self.__name = name
    def set_size(self,size):
        self.__size = size
    def set_computers(self,computers):
        self.__computers = computers
    def set_person_size(self,person_size):
        self.__person_size = person_size
    def set_availability(self,availability):
        self.__availability = availability
    def set_projector(self,projector):
        self.__projector = projector
    def get_name(self,name):
        self.__name = name
    def get_size(self,size):
        self.__size = size
    def get_computers(self,computers):
        self.__computers = computers
    def get_person_size(self,person_size):
        self.__person_size = person_size
    def get_availability(self,availability):
        self.__availability = availability
    def get_projector(self,projector):
        self.__projector = projector