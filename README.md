# 💪 Personalized Workout and Diet Planner

## A Python + Machine Learning + Streamlit Based Intelligent Fitness Recommendation System

### 📌 Problem Statement

Most existing fitness applications provide generic workout routines and diet charts. They do not consider:
- Individual body parameters
- Student lifestyle
- Indian/cultural food habits
- Budget constraints
- Available workout equipment

As a result, students either cannot follow the plans or they become ineffective.

This project proposes an **AI-powered personalized recommendation system** that generates customized workout routines and diet plans based on a user's personal profile.

---

## 🎯 Objectives

The main objectives of this project are:
1. To analyze user body metrics and lifestyle
2. To classify fitness goal (Weight Loss / Muscle Gain / Maintenance)
3. To recommend personalized workout plan
4. To generate diet plan based on Indian food habits
5. To provide budget-friendly meal suggestions
6. To deploy the system as a web app using Streamlit

---

## 💡 Key Features

✔ **Personalized workout plan** based on goals and equipment  
✔ **Indian diet recommendation** (veg & non-veg options)  
✔ **BMI & calorie requirement calculation**  
✔ **Goal-based plan generation** using AI  
✔ **Budget-friendly meals** (Low/Medium/High)  
✔ **Simple UI** for students  
✔ **Web deployment** using Streamlit  

---

## 🧠 AI Concept Used

This system uses **Artificial Intelligence based Recommendation Logic**:
- Rule-based intelligent system
- BMI Classification
- Calorie requirement estimation (BMR & TDEE)
- **Machine Learning classification** (goal prediction)
- Personalized recommendation engine

**ML Algorithm**: Random Forest Classifier trained on 100+ samples

---

## 🏗 System Architecture

```
User enters personal details
        ↓
System calculates BMI & calorie requirement
        ↓
AI model predicts fitness category
        ↓
Recommendation engine generates:
  • Workout schedule
  • Diet plan
        ↓
Results displayed in Streamlit Web App
```

---

## 📊 Input Parameters

The system takes the following user inputs:
- Age
- Gender
- Height
- Weight
- Activity Level
- Budget Preference (Low/Medium/High)
- Food Preference (Veg / Non-Veg)
- Available Equipment (Gym / Home)

---

## 📤 Output

The system provides:
- **BMI value** & health category
- **Daily calorie requirement** (BMR & TDEE)
- **AI-predicted fitness goal** with confidence scores
- **Weekly workout routine** tailored to goal and equipment
- **Personalized meal plan** with Indian foods
- **Downloadable plan** as text file

---

## 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Programming | Python 3.8+ |
| AI/ML | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib |
| Deployment | Streamlit |
| Interface | Web App UI |

---

## 📂 Project Structure

```
Personalised-Workout-and-Diet-Planner/
│
├── app.py                 # Streamlit application (main file)
├── model.py               # ML model training and prediction
├── diet_planner.py        # Diet recommendation logic
├── workout_planner.py     # Workout recommendation logic
├── bmi_calculator.py      # BMI & calorie calculations
├── dataset.csv            # Training dataset (100+ samples)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Personalised-Workout-and-Diet-Planner
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the ML Model (Optional)
```bash
python model.py
```
This will train the Random Forest model and save it as `fitness_model.pkl`

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

---

## 💻 How to Use

1. **Enter Your Details** in the sidebar:
   - Personal information (age, gender)
   - Body metrics (height, weight)
   - Lifestyle (activity level)
   - Preferences (equipment, food, budget)

2. **Click "Generate My Plan"** button

3. **View Your Results** in 4 tabs:
   - 📊 **Health Metrics**: BMI, BMR, TDEE, Target Calories
   - 🤖 **AI Prediction**: Recommended goal with confidence scores
   - 💪 **Workout Plan**: Day-by-day exercise routines
   - 🍽️ **Diet Plan**: Complete meal plan with timings and costs

4. **Download Your Plan** as a text file for offline reference

---

## 📸 Screenshots

### Home Screen
The landing page with feature highlights and instructions.

### Health Metrics Tab
Displays BMI, BMR, TDEE, and target calories with visual metrics.

### AI Prediction Tab
Shows predicted fitness goal with confidence scores and explanation.

### Workout Plan Tab
Complete weekly workout schedule based on goal and equipment.

### Diet Plan Tab
Indian meal plans with macro distribution, timings, and budget-friendly options.

---

## 🎓 Sample Use Cases

### Case 1: Student with High BMI
- **Input**: Age 22, Male, 175cm, 85kg, Sedentary
- **AI Prediction**: Weight Loss (75% confidence)
- **Output**: High cardio workout + 2000 cal diet plan

### Case 2: Student with Low BMI
- **Input**: Age 21, Male, 180cm, 65kg, Moderately Active
- **AI Prediction**: Muscle Gain (70% confidence)
- **Output**: Strength training + 2800 cal diet plan

### Case 3: Student with Normal BMI
- **Input**: Age 23, Female, 165cm, 60kg, Lightly Active
- **AI Prediction**: Maintenance (65% confidence)
- **Output**: Balanced workout + 1800 cal diet plan

---

## 🔬 Machine Learning Details

### Dataset
- **Size**: 100+ samples
- **Features**: age, gender, height, weight, BMI, activity_level
- **Target**: goal (Weight Loss / Muscle Gain / Maintenance)

### Model
- **Algorithm**: Random Forest Classifier
- **Parameters**: 100 estimators, random_state=42
- **Accuracy**: ~85-90% on test data
- **Fallback**: Rule-based prediction if model not found

### Training
```python
# Run model training
python model.py
```

---

## 📚 Diet Plan Features

### Indian Cuisine Focus
- Traditional breakfast options (Poha, Upma, Paratha)
- Dal, Rice, Chapati combinations
- Regional dishes (Rajma, Chole, Paneer)
- Both vegetarian and non-vegetarian options

### Budget Categories
- **Low Budget**: ₹150-200 per day
- **Medium Budget**: ₹300-400 per day
- **High Budget**: ₹600-800 per day

### Macro Distribution
- **Weight Loss**: 30% protein, 40% carbs, 30% fats
- **Muscle Gain**: 35-40% protein, 40-45% carbs, 20% fats
- **Maintenance**: 25-30% protein, 45-50% carbs, 25% fats

---

## 🏋️ Workout Plan Features

### Customization Based On
- Fitness goal (Weight Loss / Muscle Gain / Maintenance)
- Equipment availability (Home / Gym)
- 7-day weekly schedule

### Workout Components
- Strength training exercises
- Cardio routines
- Core strengthening
- Active recovery
- Rest days

---

## 🔮 Future Enhancements

- [ ] User authentication and progress tracking
- [ ] Integration with fitness trackers
- [ ] Meal photo recognition
- [ ] Video demonstrations for exercises
- [ ] Community features and challenges
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Integration with food delivery apps

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is created for educational purposes.

---

## 👥 Authors

Created as an IBM Project for intelligent fitness recommendation system.

---

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

## 🙏 Acknowledgments

- Scikit-learn for machine learning library
- Streamlit for the amazing web framework
- Indian nutrition guidelines for diet recommendations
- Fitness experts for workout plan validation

---

## ⚠️ Disclaimer

This application provides general fitness recommendations. Always consult with healthcare professionals before starting any new diet or exercise program, especially if you have any health conditions.

---

**Made with ❤️ for students seeking personalized fitness guidance**