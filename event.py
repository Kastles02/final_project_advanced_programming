class Event:
    def __init__(self,name,room_num,club_name,event_time,avg_atten,contact_info):
        self.__name = name
        self.__room_num = room_num
        self.__club_name = club_name
        self.__event_time = event_time
        self.__avg_atten = avg_atten
        self.__contact_info = contact_info
    def set_name(self,name):
        self.__name = name
    def set_room_num(self,room_num):
        self.__room_num = room_num
    def set_club_name(self,club_name):
        self.__club_name = club_name
    def set_event_time(self,event_time):
        self.__event_time = event_time
    def set_avg_atten(self,avg_atten):
        self.__avg_atten = avg_atten
    def set_contact_info(self,contact_info):
        self.__contact_info = contact_info
    def get_name(self,name):
        return self.__name = name
    def get_room_num(self,room_num):
        return self.__room_num
    def get_club_name(self,club_name):
        return self.__club_name
    def get_event_time(self,event_time):
        return self.__event_time
    def get_avg_atten(self,avg_atten):
        return self.__avg_atten
    def get_contact_info(self,contact_info):
        return self.__contact_info