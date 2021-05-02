from typing import Any
from kivy.logger import Logger


class BikeWarn:
    def __init__(self, message: str, cls_self=None):
        self.message = f'Bike: {message}. {cls_self}'
        self.logger_run()

    def logger_run(self):
        Logger.warn(self.message)


class BikeError(BikeWarn):
    def logger_run(self):
        Logger.error(self.message)


class BikeInfo(BikeWarn):
    def logger_run(self):
        Logger.info(self.message)


# warn

class WarnBikeIsNotConfig(BikeWarn):
    def __init__(self, bike_title: str, cls_self: Any):
        self.message = f'The `{bike_title}` bike is not installed in configuration'
        super().__init__(self.message, cls_self)


class WarnTrySetBikeFromLayoutWarn(BikeWarn):
    def __init__(self, cls_self: Any):
        self.message = 'Try to set bike from layouts to road'
        super().__init__(self.message, cls_self)


# error

class ErrBikeIsNotConfig(BikeError):
    def __init__(self, cls_self: Any):
        self.message = 'Bike was not set! That can crash the entire application'
        super().__init__(self.message, cls_self)


# info

class InfoBikeInstalledFor(BikeInfo):
    def __init__(self, cls_self: Any):
        self.message = 'The bike has been successfully installed for {cls_self}'
        super().__init__(self.message, cls_self)
