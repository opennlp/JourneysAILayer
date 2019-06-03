import abc


class BaseRegressionInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def train_regression_model(self, train_data, train_values, **kwargs):
        pass

    @abc.abstractmethod
    def predict_regression_values(self, test_data, **kwargs):
        pass

