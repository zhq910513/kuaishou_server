
class ErrorClass(Exception):

    def __init__(self, errorinfo):
        super().__init__(self)
        self.errorinfo = errorinfo

    def __str__(self):
        return self.errorinfo


class FuncParaError(ErrorClass):
    "函数参数错误"
    pass


class WebParaError(ErrorClass):
    "前端传参错误"
    pass
