import Constants
from Classifier import Classifier

class Manager:
    
    instance = None
    
    def __init__(self):
        
        if Manager.instance is not None:
            raise Exception("Singleton was already created")
        
        Manager.instance = self
    
    @staticmethod
    def get_instance():
        
        if Manager.instance is None:
            Manager()
            
        return Manager.instance
    
    def create_input(self):
        
        user_input = "" 
        
        while user_input != Constants.EXIT_CODE:
            user_input = input("1. Classify Image\n2. Exit\n")
            
            if user_input == "1":
                Classifier.get_instance().classify_image(input("Enter Path:\n"))
            
            
            
            