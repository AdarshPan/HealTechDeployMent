
from django.shortcuts import render
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
#from tensorflow.python.framework import ops
#from tensorflow.keras import backend

from keras import backend as K

# global graph,model


print("Model Loading......")
model=load_model('XrayApp/my_model.h5')
print("model loaded sucessfully")

class_dict={'0':'Yes. The Patient is Pneumonia Positive According to the Model.....The Confidence Score out of 1 is = ',
            '1':'No! The Patient Is Pneumonia Negative According to the Model!!....The Confidence Score out of 1is  = '}

class_names = list(class_dict.values())

'''def load_modelo
	global model
	model = load_model("XrayApp/my_model.h5")
	global graph
	graph = tf.Graph()
'''

def prediction(request):
    if request.method == 'POST' and request.FILES['myfile']:
        post = request.method == 'POST'
        myfile = request.FILES['myfile']
        #load_modelo()
        img = image.load_img(myfile, target_size=(64,64))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img/255
        #keras.backend.clear_session()
        # graph = tf.Graph()
        model= load_model("XrayApp/my_model.h5")

        # with graph.as_default():

        preds = model.predict(img)
        print("Unflattendee"+str(preds))
            #K.clear_session()
        preds = preds.flatten()
        print(str(preds)+"This is the pred")
        x=(1-float(preds[0]))
        preds=np.append(preds,[x])
        print(preds)
        m = max(preds)
        print(m)
        for index, item in enumerate(preds):
            print(index,item)
            if item == m:
             result = class_names[index]+str(m)
             return render(request, "XrayApp/prediction.html", {
                    'result': result})
    else:
        return render(request, "XrayApp/prediction.html")





def DiagnoseXray (request):
    return render(request,'XrayApp/diagnoseXray.html')
def loginView(request):
    return render(request,'XrayApp/login.html')