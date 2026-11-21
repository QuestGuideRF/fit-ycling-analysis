import pandas as pd
from sklearn import preprocessing
df =pd .read_csv ('power_zones_data_label.csv',index_col =0 )
df_train =df [df ['label'].notnull ()]
df_train ['label']=df_train ['label'].astype (int )
df_train ['zone_1_2']=df_train ['zone_1']+df_train ['zone_2']
df_train ['zone_4_6']=df_train ['zone_4']+df_train ['zone_5']+df_train ['zone_6']
df_train
from sklearn .model_selection import train_test_split
X =df_train [['time_n','zone_1_2','zone_3','zone_4_6','cadence_zone_1']]
y =df_train ['label']
X_train ,X_test ,y_train ,y_test =train_test_split (X ,y ,test_size =0.3 )
from sklearn .ensemble import RandomForestClassifier
clf =RandomForestClassifier (n_estimators =100 )
clf .fit (X ,y )
y_pred =clf .predict (X_test )
from sklearn import metrics
print ("Accuracy:",metrics .accuracy_score (y_test ,y_pred ))
data =pd .read_csv ('power_zones_data_label.csv',index_col =0 )
data ['zone_1_2']=data ['zone_1']+data ['zone_2']
data ['zone_4_6']=data ['zone_4']+data ['zone_5']+data ['zone_6']
I =data [['time_n','zone_1_2','zone_3','zone_4_6','cadence_zone_1']]
data ['prediction']=clf .predict (I )
data .to_csv ('random_forest_prediction.csv')