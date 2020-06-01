from django.shortcuts import render# from django.http import JsonResponseimport osimport picklefrom django.shortcuts import HttpResponsefrom django.conf import settingsimport osfrom django.http import JsonResponsefrom sklearn.externals import joblibdef html(request):    return render(request,"corona/meo.html")    # return HttpResponse("Hey Man  HTML")def api_sentiment_pred(request):    import sklearn    import numpy as np    from sklearn.preprocessing import Imputer    import matplotlib.pyplot as plt    import pandas as pd    from pandas import datetime as dt    from sklearn.preprocessing import OneHotEncoder    import pandas as pd    if request.method == 'POST' and request.POST['location'] and request.POST['case'] and request.POST['country'] and request.POST['month_reporting'] and request.POST['year_reporting'] and request.POST['day_reporting'] :      location=request.POST['location']      print(type(location))      case=int(request.POST['case'])      country=request.POST['country']      month_reporting=int(request.POST['month_reporting'])      year_reporting=int(request.POST['year_reporting'])      day_reporting=int(request.POST['day_reporting'])      gender=request.POST['gender']      age=int(request.POST['age'])      print(type(age))      month_symptom=int(request.POST['month_symptom'])      day_symptom=int(request.POST['day_symptom'])      year_symptom=int(request.POST['year_symptom'])      set_approximation=int(request.POST['set_approximation'])      month_hospital=int(request.POST['month_hospital'])      year_hospital=int(request.POST['year_hospital'])      day_hospital=int(request.POST['day_hospital'])      print('This is day_hospital')      print(day_hospital)      print(type(day_hospital))      day_exp_start=int(request.POST['day_exp_start'])      month_exp_start=int(request.POST['month_exp_start'])      year_exp_start=int(request.POST['year_exp_start'])      day_exp_end=int(request.POST['day_exp_end'])      month_exp_end=int(request.POST['month_exp_end'])      year_exp_end=int(request.POST['year_exp_end'])      visited_wuhan=int(request.POST['visited_wuhan'])      from_wuhan=int(request.POST['from_wuhan'])      recovered=int(request.POST['recovered'])      #train the model write now.......      # Importing the dataset      dataset = pd.read_csv("C:\\Users\SHRIKANT\PycharmProjects\HealTech\HealthTechnology\corona\cvf19.csv")      dataset['gender'].fillna("GenderLess", inplace=True)      dataset['reporting date'] = pd.to_datetime(dataset['reporting date'], )      dataset['reporting_date_month'] = dataset['reporting date'].dt.month      dataset['reporting_date_year'] = dataset['reporting date'].dt.year      dataset['reporting_date_day'] = dataset['reporting date'].dt.day      dataset['symptom_onset'] = pd.to_datetime(dataset['symptom_onset'], )      dataset['symptom_onset_month'] = dataset['symptom_onset'].dt.month      dataset['symptom_onset_year'] = dataset['symptom_onset'].dt.year      dataset['symptom_onset_day'] = dataset['symptom_onset'].dt.day      dataset['hosp_visit_date'] = pd.to_datetime(dataset['hosp_visit_date'], )      dataset['hosp_visit_month'] = dataset['hosp_visit_date'].dt.month      dataset['hosp_visit_year'] = dataset['hosp_visit_date'].dt.year      dataset['hosp_visit_day'] = dataset['hosp_visit_date'].dt.day      dataset['exposure_start'] = pd.to_datetime(dataset['exposure_start'], )      dataset['exposure_start_month'] = dataset['exposure_start'].dt.month      dataset['exposure_start_year'] = dataset['exposure_start'].dt.year      dataset['exposure_start_day'] = dataset['exposure_start'].dt.day      dataset['exposure_end'] = pd.to_datetime(dataset['exposure_end'], )      dataset['exposure_end_month'] = dataset['exposure_end'].dt.month      dataset['exposure_end_year'] = dataset['exposure_end'].dt.year      dataset['exposure_end_day'] = dataset['exposure_end'].dt.day      X = dataset.iloc[:,          [1, 4, 5, 6, 7, 9, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]].values      y = dataset.iloc[:, 16].values      imputer = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)      imputer1 = Imputer(missing_values='NaN', strategy='mean', axis=0)      imputer1 = imputer1.fit(X[:, 0:1])      X[:, 0:1] = imputer1.transform(X[:, 0:1])      imputer = imputer.fit(X[:, 4:5])      X[:, 4:5] = imputer.transform(X[:, 4:5])      imputer = imputer.fit(X[:, 5:6])      X[:, 5:6] = imputer.transform(X[:, 5:6])      imputer = imputer.fit(X[:, 7:8])      X[:, 7:8] = imputer.transform(X[:, 7:8])      imputer = imputer.fit(X[:, 9:10])      X[:, 9:10] = imputer.transform(X[:, 9:10])      imputer = imputer.fit(X[:, 10:11])      X[:, 10:11] = imputer.transform(X[:, 10:11])      imputer = imputer.fit(X[:, 11:12])      X[:, 11:12] = imputer.transform(X[:, 11:12])      imputer = imputer.fit(X[:, 12:13])      X[:, 12:13] = imputer.transform(X[:, 12:13])      imputer = imputer.fit(X[:, 13:14])      X[:, 13:14] = imputer.transform(X[:, 13:14])      imputer = imputer.fit(X[:, 14:15])      X[:, 14:15] = imputer.transform(X[:, 14:15])      imputer = imputer.fit(X[:, 15:16])      X[:, 15:16] = imputer.transform(X[:, 15:16])      imputer = imputer.fit(X[:, 16:17])      X[:, 16:17] = imputer.transform(X[:, 16:17])      imputer = imputer.fit(X[:, 17:18])      X[:, 17:18] = imputer.transform(X[:, 17:18])      X[:, 18:19] = imputer.transform(X[:, 18:19])      imputer = imputer.fit(X[:, 18:19])      imputer = imputer.fit(X[:, 19:20])      X[:, 19:20] = imputer.transform(X[:, 19:20])      imputer = imputer.fit(X[:, 20:21])      X[:, 20:21] = imputer.transform(X[:, 20:21])      imputer = imputer.fit(X[:, 21:22])      X[:, 21:22] = imputer.transform(X[:, 21:22])      imputer = imputer.fit(X[:, 22:23])      X[:, 22:23] = imputer.transform(X[:, 22:23])      imputer = imputer.fit(X[:, 23:24])      X[:, 23:24] = imputer.transform(X[:, 23:24])      # labelencoding as well as one hot encoding      from sklearn.preprocessing import LabelEncoder      labelencoder_x = LabelEncoder()      X[:, 1] = labelencoder_x.fit_transform(X[:, 1])      loca_label=labelencoder_x      final_location=loca_label.transform([location])      final_location=np.asarray(final_location,dtype=object)      final_location=final_location[0]      print("The final location is this::::::")      print(final_location)      X[:, 2] = labelencoder_x.fit_transform(X[:, 2])      country_label=labelencoder_x      final_country=country_label.transform([country])      print("The final country of the human is this:::")      final_country=np.asarray(final_country,dtype=object)      final_country=final_country[0]      print(final_country)      print("the type of the final location is this")      print(type(final_location))      X[:, 3] = labelencoder_x.fit_transform(X[:, 3])      gender_label=labelencoder_x      final_gender=gender_label.transform([gender])      final_gender=np.asarray(final_gender,dtype=object)      final_gender=final_gender[0]      X_input=[case,final_location,final_country,final_gender,age,set_approximation,visited_wuhan,from_wuhan,recovered,month_reporting,year_reporting,day_reporting,month_symptom,year_symptom,day_symptom,month_hospital,year_hospital,day_hospital,month_exp_start,year_exp_start,day_exp_start,month_exp_end,year_exp_end,day_exp_end,]      onehotencoder = OneHotEncoder(drop="first", categories="auto")      X = onehotencoder.fit_transform(X).toarray()      # X_input=np.asarray(X_input,dtype=object)      print("Now the X_input........")      print(type(X_input))      print(X_input)      X_input=onehotencoder.transform([X_input]).toarray()      print("the final x_input")      print(X_input)      '''      one= OneHotEncoder(categorical_features = [2])       X = one.fit_transform(X).toarray()      one8=OneHotEncoder(categorical_features=[3])      X=one8.fit_transform(X).toarray()      '''      # Avoiding the dummy variable trap      # Splitting the dataset into the Training set and Test set      from sklearn.model_selection import train_test_split      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)      from sklearn.preprocessing import StandardScaler      sc = StandardScaler()      X_train = sc.fit_transform(X_train)      X_test = sc.transform(X_test)      X_input=sc.transform(X_input)      # Applying LDA      from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA      lda = LDA(n_components=2)      X_train = lda.fit_transform(X_train, y_train)      X_test = lda.transform(X_test)      X_input=lda.transform(X_input)      from sklearn.linear_model import LogisticRegression      classifier = LogisticRegression(random_state=0)      classifier.fit(X_train, y_train)      result=classifier.predict(X_input)      result=result[0]      probabilities = classifier.predict_proba(X_input)      probabilities=probabilities[0][1]      probabilities=probabilities-0.0005      log_prob=classifier.predict_log_proba(X_input)      print(classifier.predict_proba(X_input))      #from here start the stuffs      #use the data  wisely man !!!      # print(loca_label.classes_)      # print(final_location)      if result==0:        result="Yes!!....The Patient Has A Higher Rate of Survival Out Of 1:Approximately="      elif result==1:        probabilities=1-probabilities        result="No.The patients has a low rate of Survival Out Of 1:Approximately="      return render(request,'corona/meo.html',{'result':result,'probability':probabilities,'log_probability':log_prob})    else:      return render(request,"corona/meo.html")# CURRENT_DIR = os.path.dirname(__file__)# model_file = os.path.join(CURRENT_DIR, 'model.file')# model = joblib.load(model_file)# path = os.path.join(settings.MODELS, 'mymodels.p')# with open(path, 'rb') as pickled:#     data = pickle.load(pickled)##     classifier = data['classifier']#     onehotencoder = data['onehotencoder']#     label_encoder = data['label_encoder']#     feature_scaler = data['feature_scaler']#     '''#     if request.method == 'POST' and request.POST['location']:##         post = request.method == 'POST'#         print(post)#         review=request.POST['POST']#         print(review)# ''''''    review = request.GET.get('location',None)    print(review)    return HttpResponse(review)    # o=model['onehotencoder']    # # result = 'Positive' if model.predict([review]) else 'Negative'    # return (JsonResponse(o, safe=False))''''''class call_model(APIView):    def post(self, request):        if request.method == "POST":            # get sound from request            sound = request.POST()            #here we are gonna have a lot of other features .....like case in country,#and all of them actually......            # vectorize sound            onehotencoder = Covid19Config.onehotencoder.transform([sound])            # predict based on vector            prediction = Covid19Config.classifier.predict(onehotencoder)[0]            # build response            response = {'dog': prediction}            # return response            return JsonResponse(response)'''# def me(request):###  if request.method == "GET":#        # return HttpResponse("Gotch")##        data_user=request.GET['data_user']#        path = os.path.join(settings.MODELS, 'mymodels.p')#        with open(path, 'rb') as pickled:#            data = pickle.load(pickled)#        classifier = data['classifier']#        onehotencoder = data['onehotencoder']#        label_encoder=data['label_encoder']#        feature_scaler=data['feature_scaler']#        return render(request,"corona/re.html",{'onehot':onehotencoder})#  else:#      return HttpResponse("not gotch")