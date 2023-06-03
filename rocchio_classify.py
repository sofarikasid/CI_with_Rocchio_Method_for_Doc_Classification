import pandas as pd
import numpy as np
from tqdm.notebook import tqdm

train_label = pd.read_csv("BBC_News_5_Train_Labels.csv", header=None)
train = pd.read_csv("BBC_News_5_Train.csv", header=None)
test = pd.read_csv("BBC_News_5_Test.csv", header=None)
test_label = pd.read_csv("BBC_News_5_Test_Labels.csv", header=None)
feature_ = pd.read_csv("BBC_News_5_Features.csv", header=None)
full_data = pd.read_csv("bbc-5categories.csv")


def Rocchio_Classify_train(train, train_label):
    "This function classified text using Rocchio Method"
    import numpy as np

    merged_df = pd.merge(train, train_label, left_index=True, right_index=True)
    # merged_df=merged_df.set_index("0_x")

    ################
    # train.head()
    indexed_train = train.set_index(0)
    indexed_train.head()

    # Create an empty dictionary to hold the inverted index
    inverted_index = {}

    # Loop through each row in the DataFrame and update the inverted index
    for i, row in merged_df.iterrows():
        train_id = row["0_y"]
        if train_id not in inverted_index:
            inverted_index[train_id] = []
        inverted_index[train_id].append(merged_df["0_x"][i])

    # Create a list of dictionaries to store the data
    data = []
    norm_ = {}
    proto__ = {}
    for token in inverted_index:
        protoo_ = (
            indexed_train.loc[inverted_index[token]].sum(axis=0)
        ).values  ##COMPUTED THE protptype for each CATEGORY
        proto__[token] = protoo_
        # Compute the norm of each array in the dictionary
        for key, value in proto__.items():
            norm = np.linalg.norm(value)
            norm_[token] = norm
    return norm_, proto__


def Rocchio_Classify_test(train_model, test_instance, train_data, train_label):
    "This function runs test using the Rocchio_Classify_train model above"

    ##Load or run the train model
    D_norm, prototypee = Rocchio_Classify_train(train_data, train_label)

    x_norm = np.linalg.norm(test_instance)
    # Compute the cosine SIM on the new instance and each protopype

    sims = {
        k: np.dot(prototypee[k], test_instance) / (D_norm[k] * x_norm)
        for k in prototypee
    }
    # rank the dictionary by values

    sorted_list = sorted(sims.items(), key=lambda x: x[1])

    return sorted_list[-1][0], sorted_list[-1][1]


def run_roochio(Rocchio_Classify_train, train, train_label, test, set_index=False, k=None):
    if set_index:
        test = test.set_index(0)
    
    if k is None:
        print('The default runs the first 20 documents')
        k_values = range(0, 20, 1)
    else:
        k_values = [k]
    
    for k in k_values:
        test_instance = np.array(test.iloc[k])
        predicted_class, cosin_SIM = Rocchio_Classify_test(Rocchio_Classify_train, test_instance, train, train_label)
        print(f"Test Item {k} - Predicted Class: {predicted_class} -- Actual Class: {test_label[0].iloc[k]} COSINE_SIM: {cosin_SIM}")

def run_roochio_with_metric(Rocchio_Classify_train, train, train_label, test, set_index=False, k=None):
    if set_index:
        test = test.set_index(0)
    
    if k is None:
        k_values = range(len(test))
    else:
        k_values = [k]
    
    predict = []
    count = 0
    
    for k in k_values:
        test_instance = np.array(test.iloc[k])
        predicted_class, cosin_SIM = Rocchio_Classify_test(Rocchio_Classify_train, test_instance, train, train_label)
        predict.append(predicted_class)
        
        if predict[k] == test_label[0].iloc[k]:
            count += 1
    
    accuracy = count / len(test)
    print(f"The Rocchio's Method accuracy is {accuracy}")