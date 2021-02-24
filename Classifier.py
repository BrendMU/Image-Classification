from imageai.Classification import ImageClassification
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
        predictions, probabilities = self.prediction.classifyImage(path, result_count=15)
        
        for predict, percentage in zip(predictions, probabilities):
            print(f"{path}: {predict} {percentage}")
        
        