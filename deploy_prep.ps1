# Deployment Preparation Script for Windows
# Run this before deploying to ensure everything is ready

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  AI Fitness Planner - Deployment Prep  " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python
Write-Host "[1/5] Checking Python installation..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Python found" -ForegroundColor Green
Write-Host ""

# Step 2: Install dependencies
Write-Host "[2/5] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Dependencies installed" -ForegroundColor Green
Write-Host ""

# Step 3: Train ML model
Write-Host "[3/5] Training ML model..." -ForegroundColor Yellow
python model.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Model training failed" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Model trained successfully" -ForegroundColor Green
Write-Host ""

# Step 4: Test the app locally
Write-Host "[4/5] Testing app locally..." -ForegroundColor Yellow
Write-Host "Starting Streamlit app (Press Ctrl+C to stop)..." -ForegroundColor Cyan
Write-Host "The app should open in your browser at http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "After testing, press Ctrl+C and continue with deployment." -ForegroundColor Yellow
Write-Host ""

# Ask user if they want to test
$response = Read-Host "Do you want to test the app now? (y/n)"
if ($response -eq 'y' -or $response -eq 'Y') {
    streamlit run app.py
}

Write-Host ""
Write-Host "[5/5] Preparing for Git deployment..." -ForegroundColor Yellow

# Check if git is initialized
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Cyan
    git init
    Write-Host "✓ Git initialized" -ForegroundColor Green
} else {
    Write-Host "✓ Git already initialized" -ForegroundColor Green
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Deployment Preparation Complete! ✓    " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Push code to GitHub:" -ForegroundColor White
Write-Host "   git add ." -ForegroundColor Gray
Write-Host "   git commit -m 'Initial commit'" -ForegroundColor Gray
Write-Host "   git remote add origin YOUR_GITHUB_URL" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Deploy on Streamlit Cloud:" -ForegroundColor White
Write-Host "   - Go to https://share.streamlit.io" -ForegroundColor Gray
Write-Host "   - Sign in with GitHub" -ForegroundColor Gray
Write-Host "   - Click 'New app' and select your repo" -ForegroundColor Gray
Write-Host ""
Write-Host "3. See DEPLOYMENT.md for detailed instructions" -ForegroundColor White
Write-Host ""
Write-Host "Your app will be live at: https://your-app-name.streamlit.app" -ForegroundColor Cyan
Write-Host ""
