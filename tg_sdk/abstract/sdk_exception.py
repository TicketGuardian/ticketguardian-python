class SDKException(Exception):
    def __str__(self):
        return self.message
