
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False

    def mute(self):
        if self.__status is True:
            if self.__muted is False:
                self.__muted = True
            elif self.__muted is True:
                self.__muted = False

    def channel_up(self):
        if self.__status is True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status is True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status is True:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            self.__muted = False

    def volume_down(self):
        if self.__status is True:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            self.__muted = False

    def __str__(self):
        if self.__muted is True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        elif self.__muted is False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

