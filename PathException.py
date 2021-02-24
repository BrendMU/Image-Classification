class PathException(Exception):
    
    def __init__(self, path):
        super().__init__(path)
        self.path = path
        
    def __str__(self):
        return f"{self.path} is not a file or a folder"
    
    def __repr__(self):
        return self.__str__()