import abc


class BaseEvaluationInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_predicted_data(self, trained_model, test_data,**kwargs):
        pass

    @abc.abstractmethod
    def get_evaluation_score(self, test_values, predicted_values, **kwargs):
        pass
