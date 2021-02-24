from imageai.Classification import ImageClassification
from PathException import PathException
import os

class Classifier:
    
    instance = None
    
    def __init__(self):
        if Classifier.instance is not None:
            raise Exception("Singleton already created")
            
        Classifier.instance = self
        self.prediction = ImageClassification()
        self.prediction.setModelTypeAsResNet50()
        self.prediction.setModelPath(os.getcwd() + "/resnet50_imagenet_tf.2.0.h5")
        self.prediction.loadModel()
                
    @staticmethod
    def get_instance():
        
        if Classifier.instance is None:
            Classifier()
        
        return Classifier.instance
            
    def classify_image(self, path):
        
        file_name = path[path.rfind("/") + 1:]
        
        try:
            predictions, probabilities = self.prediction.classifyImage(path, result_count=3)
            
            for predict, percentage in zip(predictions, probabilities):
                print(f"{file_name}: {predict}")
            
        except ValueError:
            raise PathException(path)
   
    def classify_folder(self, path):
        
        if not os.path.isdir(path):
            raise PathException(path)
        
        files = (os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
        folders = (folder[0] for folder in os.walk(path))
         
        for file in files:
            Classifier.get_instance().classify_image(file) 
        
        next(folders)
        for folder in folders:
            self.classify_folder(folder)