""" 
Functions of this file are:
    Load feature vectors
    Data Normalization, Split and clean
    Perform ML Model training and Validation
    Logging of results

"""

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, roc_auc_score, precision_score, recall_score, balanced_accuracy_score
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
import pandas as pd
import os
import traceback


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

""" 
Data loading , cleaning and Normalization

"""
def prepare_and_split_data(commits_df: pd.DataFrame):
    # removed zero valued columns
    commits_df = commits_df.loc[:, (commits_df != 0).any(axis=0)]
    # split data
    X = commits_df.drop(['LABEL'], axis=1)
    y = commits_df['LABEL']
    training, testing, training_labels, testing_labels = train_test_split(
        X, y, test_size=.25, random_state=42)
    # return training, training_labels, testing, testing_labels
    # Normalize the data
    sc = StandardScaler()
    normed_train_data = pd.DataFrame(
        sc.fit_transform(training), columns=X.columns)
    normed_test_data = pd.DataFrame(
        sc.fit_transform(testing), columns=X.columns)

    return normed_train_data, training_labels, normed_test_data, testing_labels


# Classifiers under consideration

classifiers_names = [
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Gaussian Process",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
    "QDA",
    "Logistic Regression",
    "Ridge Classifier",
]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear",max_iter=2000),
    SVC(max_iter=2000),
    GaussianProcessClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    MLPClassifier(hidden_layer_sizes=(100,100)),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    LogisticRegression(),
    RidgeClassifier(),
]

""" 
Function for performing ML training and validation
for all classifier with given dataset

"""

def generate_all_clf_perf(normed_train_data, training_labels, normed_test_data, testing_labels,selected_classifiers = None):
    classifiers_perf = []
    for i, clf in enumerate(classifiers):
        if selected_classifiers and i not in selected_classifiers:
            break
        try:
            clf.fit(normed_train_data, training_labels)
            preds = clf.predict(normed_test_data)

            print(
                f'\t\t {clf} accuracy = {accuracy_score(testing_labels,preds)}')
            print(classification_report(testing_labels,preds))
            print(confusion_matrix(testing_labels, preds))
            classifiers_perf.append({
                "classifier": classifiers_names[i],
                "accuracy_score": accuracy_score(testing_labels, preds),
                "balanced_accuracy_score": balanced_accuracy_score(testing_labels, preds),
                "f1_score": f1_score(testing_labels, preds),
                "roc_auc_score": roc_auc_score(testing_labels, preds),
                "precision_score": precision_score(testing_labels, preds),
                "recall_score": recall_score(testing_labels, preds),
            })

        except Exception as e:
            print(f'\tProcessing Classifer {classifiers_names[i]} failed with error {e}')
            traceback.print_exc()
    return classifiers_perf


""" 
Final driver code for performing ML training and validation
for all repository all classifier

"""
def do():
    processed_files_path = 'processed_data/'
    processed_files = os.listdir(processed_files_path)

    for p_file in processed_files:
        try:
            print(f'Processing {p_file} started ...')
            commits_df = pd.read_csv(processed_files_path+p_file)
            print(f'\tData Shape : {commits_df.shape}')
            print(f'\tAvailable cols : {commits_df.columns}')
            #print(f'Available cols : {commits_df.describe()}')
            notna = np.all(commits_df.notna())
            if not notna:
                print(f"\tDataset has Nan in following columns :")
                for f in commits_df.columns:
                    if not np.all(commits_df[f].notna()):
                        print(f"\t\t\t{f} ")
                continue

            x_train, y_train, x_test, y_test = prepare_and_split_data(commits_df)
            classifiers_perf = generate_all_clf_perf(
                x_train, y_train, x_test, y_test)
            pd.DataFrame(classifiers_perf).to_csv(
                f'ml_perf_report/{p_file}', index=False)
            print(f'Processing {p_file} successfully complete!\n')
        except Exception as e:
            print(f'Processing {p_file} failed with error {e}')
            traceback.print_exc()
