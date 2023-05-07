import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.nueral_network import MLPClassifier

dataset=pd.read_csv('new_radar_distance_data.csv')

x=dataset.iloc[:,[2,4]].values
y=dataset.iloc[:,5].values

model=MLPClassifier(hidder_layer_sizes=(20),
						random_state=5,
						activation='relu',
						batch_size=200,
						learning_rate_init=0.03)

model.fit(x,y)
predictions=model.predict(x)

file=open('model.pkl','wb')
pickle.dump(model,file)

saved_model_file=open('model.pkl','rb')
saved_model=pickle.load(saved_model_file)

car_data={
	'throttle':[0.364332455],
	'distance': [6.674762726]
}

data=pd.DataFrame(car_data, columns=['throttle','distance'])
predicated_data=saved_model.predict(data)
print("Model prediction:", predicated_data)