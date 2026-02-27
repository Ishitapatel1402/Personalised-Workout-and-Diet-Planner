# 🚀 Quick Start Guide

## Getting Started in 3 Simple Steps

### Step 1️⃣: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2️⃣: Train the ML Model (First Time Only)
```bash
python model.py
```
This creates the `fitness_model.pkl` file needed for AI predictions.

### Step 3️⃣: Launch the Application
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 🎯 How to Use the App

1. **Fill Your Profile** in the left sidebar:
   - Age, Gender, Height, Weight
   - Activity Level
   - Equipment (Home/Gym)
   - Food Preference (Veg/Non-Veg)
   - Budget (Low/Medium/High)

2. **Click "Generate My Plan"** button

3. **Explore Your Results**:
   - 📊 Health Metrics: BMI, calories
   - 🤖 AI Prediction: Your fitness goal
   - 💪 Workout Plan: Weekly exercises
   - 🍽️ Diet Plan: Indian meal plans

4. **Download Your Plan** for offline use

---

## 🐛 Troubleshooting

### Issue: Module not found errors
**Solution**: Make sure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Model file not found
**Solution**: Train the model first
```bash
python model.py
```

### Issue: Port already in use
**Solution**: Use a different port
```bash
streamlit run app.py --server.port 8502
```

---

## 💡 Tips

- Update your profile anytime in the sidebar
- Try different combinations to see various plans
- The AI considers your BMI and activity level
- All diet plans use Indian cuisine
- Budget affects meal options but not nutrition quality

---

## 📧 Need Help?

- Check the full [README.md](README.md) for detailed documentation
- Review the code comments for technical details
- Open an issue for bugs or suggestions

---

**Happy Fitness Journey! 💪**
