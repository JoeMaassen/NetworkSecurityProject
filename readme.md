# Network Analysis Project
##### By: [Bogdan Bruma and Joe Maaßen]()

This is our complete implementation for the Network Analysis Project. The project is divided into 3 main parts, each correspoding to a diffrerent folder. Morevoer, each folder contains additional ReadMe files that explain the content of the folder in more detail. The 3 main parts are:
1. **Data** - This folder contains a shell script that automatically splits the data and creates the corresponding CSV used for machine learning.
2. **Machine Learning** - This folder contains the implementation of the machine learning models used for the project, as well as the steps taken for data processing. 
3. **IDS** - This folder contains the implementation of the Intrusion Detection System.

On top of this we provide the four resulting models that we used to extract the data presented in the report. The models are in saved in PreTrainedModels folder:
1. **Standard Random Forest** called trained_model_srf.pkl
2. **Balanced Random Forest without Smote** called trained_model_brfNoSmote.pkl
3. **Balanced Random Forest with Smote** called trained_model_brfSmote.pkl
4. **Logistic Regrssion** called trained_model_logisticRegression.pkl
