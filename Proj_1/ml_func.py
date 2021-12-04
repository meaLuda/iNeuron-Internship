# feature selector class
# ================== UNTESTED CODE ===========================
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score



class FeatureSelector:
    """
        Code by :Munyala Eliud

        # libraries youll need


        link to tut: [https://chrisalbon.com/code/machine_learning/trees_and_forests/feature_selection_using_random_forest/]
        
        # input descriptions
        ```
        1. data: the data frame you are working on, should be cleaned
        2. X_set_columns:features,list of columns for the X 
        3. split_size: percent you want the data to be split by i.e 0.2,0.3..... default is 0.3
        ```
    """
    def __init__(self,data,X_set_columns,y_set_columns,split_size=0.3):
        self.data = data
        self.X_set_columns = X_set_columns
        self.y_set_columns = y_set_columns
        self.split_size = split_size

    def split_data(self):
        X = self.data[self.X_set_columns]
        y = self.data[self.y_set_columns]

        # Split the data into 40% test and 60% training
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.split_size, random_state=0)

        return X_train, X_test, y_train, y_test
    
    def rf_classifier_viewer(self):
        """
            Feature selection using Random Forest
            Identify And Select Most Important Features
            
            ## return feature_list, feature_list_best
        """
        X_train, X_test, y_train, y_test = self.split_data()

        # Create a random forest classifier
        clf = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)

        # Train the classifier
        clf.fit(X_train, y_train)

        feature_list = list()

        # Print the name and gini importance of each feature
        for feature in zip(self.X_set_columns, clf.feature_importances_):
            # print(feature)
            feature_list.append(feature)
        
        # Create a selector object that will use the random forest classifier to identify
        # features that have an importance of more than 0.15
        sfm = SelectFromModel(clf, threshold=0.15)

        # Train the selector
        sfm.fit(X_train, y_train)

        feature_list_best = list()
        # Print the names of the most important features
        for feature_list_index in sfm.get_support(indices=True):
            # print(self.X_set_columns[feature_list_index])
            feature_list_best.append(self.X_set_columns[feature_list_index])

        # Apply The Full Featured Classifier To The Test Data
        y_pred = clf.predict(X_test)

        # View The Accuracy Of Our Full Feature (4 Features) Model
        acc_feature_list = accuracy_score(y_test, y_pred)

        # Create a new random forest classifier for the most important features
        clf_important = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)

        # Train the new classifier on the new dataset containing the most important features
        clf_important.fit(X_test, y_train)


        # Apply The Full Featured Classifier To The Test Data
        y_important_pred = clf_important.predict(X_test)

        # View The Accuracy Of Our Limited Feature (2 Features) Model
        acc_feature_best = accuracy_score(y_test, y_important_pred)


        predictions = {
            "Accuracy_score_of_list":acc_feature_list,
            "Accuracy_score_of_best":acc_feature_best,
        }

        final = {
            "Features_list": feature_list,
            "Best features": feature_list_best,
            "Predictions": predictions,
        }
        
        # return feature_list, feature_list_best,predictions
        return final


    def __init__(self) -> None:
        pass