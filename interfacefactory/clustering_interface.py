import abc


class BaseClusteringInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fit_cluster_data(self,data,**kwargs):
        pass

    @abc.abstractmethod
    def get_cluster_centers(self):
        pass

    @abc.abstractmethod
    def get_cluster_labels(self):
        pass
