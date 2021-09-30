import pickle
import pandas as pd
import numpy as np

class Persistency(object):
    
    def __init__(self):
        self.Count_Of_Comorbidity_scaler   = pickle.load(open('/Users/Igor/repos/data_glacier/final_project/deploy_streamlit/parameter/Count_Of_Comorbidity_scaler.pkl', 'rb'))
        self.Count_Of_Concomitancy_scaler  = pickle.load(open('/Users/Igor/repos/data_glacier/final_project/deploy_streamlit/parameter/Count_Of_Concomitancy_scaler.pkl', 'rb'))
        self.Dexa_Freq_During_Rx_scaler    = pickle.load(open('/Users/Igor/repos/data_glacier/final_project/deploy_streamlit/parameter/Dexa_Freq_During_Rx_scaler.pkl', 'rb'))
        self.Ntm_Speciality_Bucket_scaler  = pickle.load(open('/Users/Igor/repos/data_glacier/final_project/deploy_streamlit/parameter/Ntm_Speciality_Bucket_scaler.pkl', 'rb')) 
        self.Region_scaler                 = pickle.load(open('/Users/Igor/repos/data_glacier/final_project/deploy_streamlit/parameter/Region_scaler.pkl', 'rb'))
        
    
    def data_preparation(self, df5):
        
        # 5.0. STEP 05 - DATA PREPARATION

        ## 5.2. Rescaling

        # Dexa_Freq_During_Rx uses Robust Scaler
        df5['Dexa_Freq_During_Rx'] = self.Dexa_Freq_During_Rx_scaler.fit_transform(df5[['Dexa_Freq_During_Rx']].values)  

        # Count_Of_Concomitancy uses Min-Max Scaler
        df5['Count_Of_Concomitancy'] = self.Count_Of_Concomitancy_scaler.fit_transform(df5[['Count_Of_Concomitancy']].values)
        
        # Count_Of_Comorbidity uses Min-Max Scaler
        df5['Count_Of_Comorbidity'] = self.Count_Of_Comorbidity_scaler.fit_transform(df5[['Count_Of_Comorbidity']].values)
            
        ## 5.3. TRansformation

        ### 5.3.1. Encoding

        # Categorical Variables

        # Categorical attributes that presents binary values as 'Y' and 'N', the method Label Encoding will be used in order to
        # transfoer 'Y' and 'N' values into 1 and 0 respectively.

        df5 = df5.replace('Y', 1).replace('N', 0)

        # Categorical attributes that do not presents order or scale or idea os state, each value is independent, 
        # will be use the method  Label Encoding

        # Region
        df5['Region'] = self.Region_scaler.fit_transform(df5['Region'])

        # Ntm_Speciality_Bucket
        df5['Ntm_Speciality_Bucket'] = self.Ntm_Speciality_Bucket_scaler.fit_transform(df5['Ntm_Speciality_Bucket'])

        # Categorical attributes that presents a huge amount of values, will be use the method  Target Encoding

        return df5