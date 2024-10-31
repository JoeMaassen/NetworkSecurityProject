This folder contains two jupyter notebooks that were used to process the data, train the models and save them as pickle files.
The first notebook is called:
 `DataProcessing.ipynb` and it contains the steps taken to process the data and create the CSV files used for training the models. It expects that in the Data Folder there is a file called `TrainingDataset.csv` which is the output of the shell script in the Data folder.
The second notebook is called:
`MachineLearning.ipynb` and it contains the steps taken to train the models and save them as pickle files. It expects that in this directory a file called `ProcessedDataset.csv` which is the output of `DataProcessing.ipynb` notebook.