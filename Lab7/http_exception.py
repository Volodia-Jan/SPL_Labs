class HttpException(Exception):
    def __init__(self, message, data=None):
        super().__init__(message)
        self.data = data
