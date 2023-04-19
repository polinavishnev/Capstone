import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


smart_df = pd.read_csv('smart_goals.csv')


# make it so the values in all columns but "Goal" are either 0 or 1. If the value is "N" or "No", make it zero. If the value is "Y" or "Yes", make it 1.
smart_df['Specific'] = smart_df['Specific'].replace(['N', 'No'], 0)
smart_df['Specific'] = smart_df['Specific'].replace(['Y', 'Yes'], 1)
smart_df['Measurable'] = smart_df['Measurable'].replace(['N', 'No'], 0)
smart_df['Measurable'] = smart_df['Measurable'].replace(['Y', 'Yes'], 1)
smart_df['Action-oriented'] = smart_df['Action-oriented'].replace(['N', 'No'], 0)
smart_df['Action-oriented'] = smart_df['Action-oriented'].replace(['Y', 'Yes'], 1)
smart_df['Relevant'] = smart_df['Relevant'].replace(['N', 'No'], 0)
smart_df['Relevant'] = smart_df['Relevant'].replace(['Y', 'Yes'], 1)
smart_df['Time-bound'] = smart_df['Time-bound'].replace(['N', 'No'], 0)
smart_df['Time-bound'] = smart_df['Time-bound'].replace(['Y', 'Yes'], 1)

clean_df = pd.read_csv('clean_text.csv')[:290]
smart_df = pd.concat([smart_df, clean_df], axis=0)
smart_df.reset_index(drop=True, inplace=True)
smart_df.drop(smart_df.columns[6], axis=1, inplace=True)

data = smart_df


def classify_goal(goal, data):
    string_output = 'Based on our data, your goal is: \n'
    for component in ['Specific', 'Measurable', 'Action-oriented', 'Relevant', 'Time-bound']:
        goal_pred, accuracy = classify_rf(goal, component, data)
        # write yes if component is equal to 1, no if 0
        if int(goal_pred) == 1:
            goal_pred = ''
        else:
            goal_pred = 'Not yet'
            component = component.lower()
        string_output += (f'Prediction: {goal_pred} {component} with an accuracy of {round(accuracy, 2)} \n')
    return string_output

def classify_rf(goal, component, data):
    X = data['Goal']
    y = data[component]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize the text data
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Initialize and train the Random Forest model
    clf = RandomForestClassifier()
    clf.fit(X_train_vec, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test_vec)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # predict the goal
    goal_vec = vectorizer.transform([goal])
    goal_pred = clf.predict(goal_vec)
    return goal_pred, accuracy
