import pickle
import numpy as np
import streamlit as st
from sklearn.preprocessing import robust_scale

# loading the trained model
pickle_in = open('model/model_classification.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
# defining the prediction function
def prediction(Region, Ntm_Speciality_Bucket, Dexa_Freq_During_Rx, Comorb_Encounter_For_Screening_For_Malignant_Neoplasms,
       Comorb_Encounter_For_Immunization,
       Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx,
       Comorb_Vitamin_D_Deficiency,
       Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified,
       Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx,
       Comorb_Long_Term_Current_Drug_Therapy, Comorb_Dorsalgia,
       Comorb_Personal_History_Of_Other_Diseases_And_Conditions,
       Comorb_Other_Disorders_Of_Bone_Density_And_Structure,
       Comorb_Gastro_esophageal_reflux_disease,
       Concom_Systemic_Corticosteroids_Plain, Concom_Cephalosporins,
       Concom_Macrolides_And_Similar_Types, Concom_Anaesthetics_General,
       Concom_Viral_Vaccines, Count_Of_Concomitancy, Count_Of_Comorbidity):

    # making the prediction
    yhat = classifier.predict([[Region, Ntm_Speciality_Bucket, Dexa_Freq_During_Rx, Comorb_Encounter_For_Screening_For_Malignant_Neoplasms,
       Comorb_Encounter_For_Immunization,
       Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx,
       Comorb_Vitamin_D_Deficiency,
       Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified,
       Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx,
       Comorb_Long_Term_Current_Drug_Therapy, Comorb_Dorsalgia,
       Comorb_Personal_History_Of_Other_Diseases_And_Conditions,
       Comorb_Other_Disorders_Of_Bone_Density_And_Structure,
       Comorb_Gastro_esophageal_reflux_disease,
       Concom_Systemic_Corticosteroids_Plain, Concom_Cephalosporins,
       Concom_Macrolides_And_Similar_Types, Concom_Anaesthetics_General,
       Concom_Viral_Vaccines, Count_Of_Concomitancy, Count_Of_Comorbidity]])

    # giving the answer
    prediction = (yhat)

    return prediction


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Persistency of Drug Classification ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("Author: Igor Queiroz - Data Scientist")

    # defining Region
    Region = st.selectbox('Region', ('West', 'Midwest', 'South', 'Other/Unknown', 'Northeast'))

    if Region == 'Midwest':
        Region = 0

    elif Region == 'Northeast':
        Region = 1

    elif Region == 'Other/Unknown':
        Region = 2

    elif Region == 'South':
        Region = 3

    elif Region == 'West':
        Region = 4

    # defining Ntm_Speciality_Bucket
    Ntm_Speciality_Bucket = st.selectbox('Ntm_Speciality_Bucket', ('OB/GYN/Others/PCP/Unknown', 'Endo/Onc/Uro', 'Rheum'))

    if Ntm_Speciality_Bucket == 'Endo/Onc/Uro':
        Ntm_Speciality_Bucket = 0

    elif Ntm_Speciality_Bucket == 'OB/GYN/Others/PCP/Unknown':
        Ntm_Speciality_Bucket = 1

    else:
        Ntm_Speciality_Bucket = 2

    # defining Dexa_Freq_During_Rx
    Dexa_Freq_During_Rx = st.number_input("Dexa_Freq_During_Rx")

    st.header('Types of Comorbidity')

    # defining Comorb_Encounter_For_Screening_For_Malignant_Neoplasms
    Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = st.checkbox('Comorb_Encounter_For_Screening_For_Malignant_Neoplasms')

    if Comorb_Encounter_For_Screening_For_Malignant_Neoplasms:
        Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = 1

    else:
        Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = 0

    # defining Comorb_Encounter_For_Immunization
    Comorb_Encounter_For_Immunization = st.checkbox('Comorb_Encounter_For_Immunization')

    if Comorb_Encounter_For_Immunization:
        Comorb_Encounter_For_Immunization = 1

    else:
        Comorb_Encounter_For_Immunization = 0

    # defining Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx
    Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = st.checkbox('Comorb_Encntr_For_General_Exam_W_O_Complaint,_Susp_Or_Reprtd_Dx')

    if Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx:
        Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = 1

    else:
        Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = 0

    # defining Comorb_Vitamin_D_Deficiency
    Comorb_Vitamin_D_Deficiency = st.checkbox('Comorb_Vitamin_D_Deficiency')

    if Comorb_Vitamin_D_Deficiency:
        Comorb_Vitamin_D_Deficiency = 1

    else:
        Comorb_Vitamin_D_Deficiency = 0

    # defining Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified
    Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = st.checkbox('Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified')

    if Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified:
        Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = 1

    else:
        Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = 0

    # defining Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx
    Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = st.checkbox('Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx')

    if Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx:
        Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = 1

    else:
        Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = 0

    # defining Comorb_Long_Term_Current_Drug_Therapy
    Comorb_Long_Term_Current_Drug_Therapy = st.checkbox('Comorb_Long_Term_Current_Drug_Therapy')

    if Comorb_Long_Term_Current_Drug_Therapy:
        Comorb_Long_Term_Current_Drug_Therapy = 1

    else:
        Comorb_Long_Term_Current_Drug_Therapy = 0

    # defining Comorb_Dorsalgia
    Comorb_Dorsalgia = st.checkbox('Comorb_Dorsalgia')

    if Comorb_Dorsalgia:
        Comorb_Dorsalgia = 1

    else:
        Comorb_Dorsalgia = 0

    # defining Comorb_Personal_History_Of_Other_Diseases_And_Conditions
    Comorb_Personal_History_Of_Other_Diseases_And_Conditions = st.checkbox('Comorb_Personal_History_Of_Other_Diseases_And_Conditions')

    if Comorb_Personal_History_Of_Other_Diseases_And_Conditions:
        Comorb_Personal_History_Of_Other_Diseases_And_Conditions = 1

    else:
        Comorb_Personal_History_Of_Other_Diseases_And_Conditions = 0

    # defining Comorb_Other_Disorders_Of_Bone_Density_And_Structure
    Comorb_Other_Disorders_Of_Bone_Density_And_Structure = st.checkbox('Comorb_Other_Disorders_Of_Bone_Density_And_Structure')

    if Comorb_Other_Disorders_Of_Bone_Density_And_Structure:
        Comorb_Other_Disorders_Of_Bone_Density_And_Structure = 1

    else:
        Comorb_Other_Disorders_Of_Bone_Density_And_Structure = 0

    # defining Comorb_Gastro_esophageal_reflux_disease
    Comorb_Gastro_esophageal_reflux_disease = st.checkbox('Comorb_Gastro_esophageal_reflux_disease')

    if Comorb_Gastro_esophageal_reflux_disease:
        Comorb_Gastro_esophageal_reflux_disease = 1

    else:
        Comorb_Gastro_esophageal_reflux_disease = 0

    st.header('Types of Concomitancy')

    # defining Concom_Systemic_Corticosteroids_Plain
    Concom_Systemic_Corticosteroids_Plain = st.checkbox('Concom_Systemic_Corticosteroids_Plain')

    if Concom_Systemic_Corticosteroids_Plain:
        Concom_Systemic_Corticosteroids_Plain = 1

    else:
        Concom_Systemic_Corticosteroids_Plain = 0

    # defining Concom_Cephalosporins
    Concom_Cephalosporins = st.checkbox('Concom_Cephalosporins')

    if Concom_Cephalosporins:
        Concom_Cephalosporins = 1

    else:
        Concom_Cephalosporins = 0

    # defining Concom_Macrolides_And_Similar_Types
    Concom_Macrolides_And_Similar_Types = st.checkbox('Concom_Macrolides_And_Similar_Types')

    if Concom_Macrolides_And_Similar_Types:
        Concom_Macrolides_And_Similar_Types = 1

    else:
        Concom_Macrolides_And_Similar_Types = 0

    # defining Concom_Anaesthetics_General
    Concom_Anaesthetics_General = st.checkbox('Concom_Anaesthetics_General')

    if Concom_Anaesthetics_General:
        Concom_Anaesthetics_General = 1

    else:
        Concom_Anaesthetics_General = 0

    # defining Concom_Viral_Vaccines
    Concom_Viral_Vaccines = st.checkbox('Concom_Viral_Vaccines')

    if Concom_Viral_Vaccines:
        Concom_Viral_Vaccines = 1

    else:
        Concom_Viral_Vaccines = 0

    # defining Count_Of_Concomitancy
    Count_Of_Concomitancy = st.number_input("Count_Of_Concomitancy")

    # defining Count_Of_Comorbidity
    Count_Of_Comorbidity = st.number_input("Count_Of_Comorbidity")


    # defining result
    result = ''
    final_result = ''

    if st.button('Predict'):
        # making the prediction
        result = prediction(Region, Ntm_Speciality_Bucket, Dexa_Freq_During_Rx, Comorb_Encounter_For_Screening_For_Malignant_Neoplasms,
       Comorb_Encounter_For_Immunization,
       Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx,
       Comorb_Vitamin_D_Deficiency,
       Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified,
       Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx,
       Comorb_Long_Term_Current_Drug_Therapy, Comorb_Dorsalgia,
       Comorb_Personal_History_Of_Other_Diseases_And_Conditions,
       Comorb_Other_Disorders_Of_Bone_Density_And_Structure,
       Comorb_Gastro_esophageal_reflux_disease,
       Concom_Systemic_Corticosteroids_Plain, Concom_Cephalosporins,
       Concom_Macrolides_And_Similar_Types, Concom_Anaesthetics_General,
       Concom_Viral_Vaccines, Count_Of_Concomitancy, Count_Of_Comorbidity)

        # converting and showing result

        if result == 1:
            result_final = 'Persistency of Drug'

        elif result == 0:
            result_final = 'Non-Persistency of Drug'

        st.success('The Persistency Flag is: {}'.format(result_final))


if __name__ == '__main__':

    main()


