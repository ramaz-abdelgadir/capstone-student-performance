# 📊 Dashboard Configuration
"""
Configuration settings for Student Performance Dashboard
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "Data"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

# Data sources
DATA_SOURCES = {
    "raw_data": DATA_DIR / "1_raw" / "student_performance.csv",
    "cleaned_data": DATA_DIR / "cleaned" / "student_performance_cleaned.csv",
    "dashboard_data": DATA_DIR / "dashboard_data"
}

# Dashboard styling
COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e", 
    "success": "#2ca02c",
    "warning": "#d62728",
    "info": "#9467bd"
}

# Performance thresholds
THRESHOLDS = {
    "excellent_score": 85,
    "good_score": 70,
    "good_attendance": 85,
    "adequate_study_hours": 5,
    "active_participation": 7
}

# Dashboard settings
DASHBOARD_CONFIG = {
    "title": "Student Performance Analytics Dashboard",
    "subtitle": "Interactive Analysis of Academic Performance Factors",
    "chart_height": 400,
    "chart_width": 600
}

print("⚙️ Dashboard configuration loaded!")
print(f"🏗️ Project root: {PROJECT_ROOT}")
print(f"📁 Data directory: {DATA_DIR}")
print(f"📊 Dashboard directory: {DASHBOARD_DIR}")
