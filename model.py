"""
Machine Learning Model Module
Trains and predicts fitness goals based on user parameters
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os


class FitnessGoalPredictor:
    """
    ML model for predicting fitness goals
    """
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoders = {}
        self.goal_encoder = LabelEncoder()
        
    def load_dataset(self, filepath='dataset.csv'):
        """
        Load training dataset
        """
        try:
            df = pd.read_csv(filepath)
            return df
        except FileNotFoundError:
            print(f"Dataset file '{filepath}' not found!")
            return None
    
    def preprocess_data(self, df):
        """
        Preprocess dataset for training
        """
        # Encode categorical features
        categorical_columns = ['gender', 'activity_level']
        
        for col in categorical_columns:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
            df[col] = self.label_encoders[col].fit_transform(df[col])
        
        # Separate features and target
        X = df.drop('goal', axis=1)
        y = self.goal_encoder.fit_transform(df['goal'])
        
        return X, y
    
    def train(self, X, y):
        """
        Train the model
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Model Training Complete!")
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, 
                                    target_names=self.goal_encoder.classes_))
        
        return accuracy
    
    def predict_goal(self, age, gender, height, weight, bmi, activity_level):
        """
        Predict fitness goal for new user
        
        Args:
            age: Age in years
            gender: 'Male' or 'Female'
            height: Height in cm
            weight: Weight in kg
            bmi: BMI value
            activity_level: Activity level string
        
        Returns:
            Predicted fitness goal
        """
        # Encode inputs
        gender_encoded = self.label_encoders['gender'].transform([gender])[0]
        activity_encoded = self.label_encoders['activity_level'].transform([activity_level])[0]
        
        # Create feature array
        features = np.array([[age, gender_encoded, height, weight, bmi, activity_encoded]])
        
        # Predict
        prediction = self.model.predict(features)
        goal = self.goal_encoder.inverse_transform(prediction)[0]
        
        return goal
    
    def get_prediction_with_confidence(self, age, gender, height, weight, bmi, activity_level):
        """
        Get prediction with confidence scores
        """
        # Encode inputs
        gender_encoded = self.label_encoders['gender'].transform([gender])[0]
        activity_encoded = self.label_encoders['activity_level'].transform([activity_level])[0]
        
        # Create feature array
        features = np.array([[age, gender_encoded, height, weight, bmi, activity_encoded]])
        
        # Get probabilities
        probabilities = self.model.predict_proba(features)[0]
        
        # Create result dictionary
        results = {}
        for idx, goal in enumerate(self.goal_encoder.classes_):
            results[goal] = round(probabilities[idx] * 100, 2)
        
        # Get best prediction
        best_goal = max(results, key=results.get)
        
        return best_goal, results
    
    def save_model(self, filename='fitness_model.pkl'):
        """
        Save trained model to file
        """
        model_data = {
            'model': self.model,
            'label_encoders': self.label_encoders,
            'goal_encoder': self.goal_encoder
        }
        with open(filename, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model saved to {filename}")
    
    def load_model(self, filename='fitness_model.pkl'):
        """
        Load trained model from file
        """
        try:
            with open(filename, 'rb') as f:
                model_data = pickle.load(f)
            self.model = model_data['model']
            self.label_encoders = model_data['label_encoders']
            self.goal_encoder = model_data['goal_encoder']
            print(f"Model loaded from {filename}")
            return True
        except FileNotFoundError:
            print(f"Model file '{filename}' not found. Please train the model first.")
            return False


def train_and_save_model():
    """
    Main function to train and save the model
    """
    print("=== Fitness Goal Prediction Model Training ===\n")
    
    # Initialize predictor
    predictor = FitnessGoalPredictor()
    
    # Load dataset
    print("Loading dataset...")
    df = predictor.load_dataset('dataset.csv')
    
    if df is None:
        return None
    
    print(f"Dataset loaded: {len(df)} samples\n")
    
    # Preprocess
    print("Preprocessing data...")
    X, y = predictor.preprocess_data(df)
    
    # Train
    print("\nTraining model...")
    accuracy = predictor.train(X, y)
    
    # Save model
    print("\nSaving model...")
    predictor.save_model()
    
    return predictor


def predict_from_saved_model(age, gender, height, weight, bmi, activity_level):
    """
    Load saved model and make prediction
    """
    predictor = FitnessGoalPredictor()
    
    if predictor.load_model():
        goal, confidence = predictor.get_prediction_with_confidence(
            age, gender, height, weight, bmi, activity_level
        )
        return goal, confidence
    else:
        # If model not found, use rule-based prediction
        return rule_based_prediction(bmi, age, activity_level)


def rule_based_prediction(bmi, age, activity_level):
    """
    Rule-based prediction as fallback
    """
    confidence = {}
    
    # Rule-based logic
    if bmi > 26:
        goal = "Weight Loss"
        confidence = {
            "Weight Loss": 75.0,
            "Maintenance": 20.0,
            "Muscle Gain": 5.0
        }
    elif bmi < 21:
        goal = "Muscle Gain"
        confidence = {
            "Muscle Gain": 70.0,
            "Maintenance": 25.0,
            "Weight Loss": 5.0
        }
    else:
        if activity_level in ['Very Active', 'Extra Active']:
            goal = "Muscle Gain"
            confidence = {
                "Muscle Gain": 60.0,
                "Maintenance": 35.0,
                "Weight Loss": 5.0
            }
        else:
            goal = "Maintenance"
            confidence = {
                "Maintenance": 65.0,
                "Weight Loss": 20.0,
                "Muscle Gain": 15.0
            }
    
    return goal, confidence


if __name__ == "__main__":
    # Train the model
    predictor = train_and_save_model()
    
    if predictor:
        # Test prediction
        print("\n=== Testing Prediction ===")
        test_age = 23
        test_gender = "Male"
        test_height = 175
        test_weight = 85
        test_bmi = 27.76
        test_activity = "Moderately Active"
        
        goal, confidence = predictor.get_prediction_with_confidence(
            test_age, test_gender, test_height, test_weight, test_bmi, test_activity
        )
        
        print(f"\nInput: Age={test_age}, Gender={test_gender}, Height={test_height}cm, "
              f"Weight={test_weight}kg, BMI={test_bmi}, Activity={test_activity}")
        print(f"\nPredicted Goal: {goal}")
        print("\nConfidence Scores:")
        for g, conf in confidence.items():
            print(f"  {g}: {conf}%")
