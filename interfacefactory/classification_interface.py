import abc


class BaseClassifierInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def train_classification_model(self,train_data,train_labels,**kwargs):
        pass

    @abc.abstractmethod
    def predict_class_labels(self, test_data, **kwargs):
        pass

