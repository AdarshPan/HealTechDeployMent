from django.apps import AppConfig
import pickle
import os
from django.conf import settings
import sklearn
class CoronaConfig(AppConfig):
    name = 'corona'
# '''
#     # create path to models
#     path = os.path.join(settings.MODELS, 'mymodels.p')
#     # path=r"C:\Users\SHRIKANT\PycharmProjects\HealTech\HealthTechnology\corona\modeloo\mymodels.p"
#     # load models into separate variables
#     # these will be accessible via this class
#     with open(path, 'rb') as pickled:
#         data = pickle.load(pickled)
#     classifier = data['classifier']
#     onehotencoder = data['onehotencoder']
#     label_encoder=data['label_encoder']
#     feature_scaler=data['feature_scaler']
# '''