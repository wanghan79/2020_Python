#自定义异常类
class MyError(Exception):
    pass


class DatatypeError(MyError):
    def __init__(self, datatype):
        self.datatype = datatype


class DatarangeError(MyError):
    def __init__(self, datarange):
        self.datarange = datarange


class NumError(MyError):
    pass


class StrlenError(MyError):
    pass


class ParameterError(MyError):
    pass


class RangeError(MyError):
    pass
