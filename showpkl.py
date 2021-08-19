import pickle
path='model.pkl' #path='/root/……/aus_openface.pkl' Path where the pkl file is located
	   
f=open(path,'rb')
data=pickle.load(f)
 
print(data)
print(len(data))
