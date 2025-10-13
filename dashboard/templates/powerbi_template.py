# 📊 Power BI Dashboard Template
"""
Template for creating Power BI dashboard for Student Performance Analysis
This script prepares data and creates exports suitable for Power BI import
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
from pathlib import Path

def prepare_powerbi_data():
    """
    Prepare and format data specifically for Power BI dashboard
    
    Returns:
        dict: Dictionary containing formatted datasets
    """
    # Load the student data
    try:
        # Adjust path based on current directory
        project_root = Path.cwd()
        
        # Navigate to project root if we're in a subdirectory
        while project_root.name != "capstone-student-performance" and project_root.parent != project_root:
            project_root = project_root.parent
            
        data_path = project_root / "Data" / "cleaned" / "student_performance_cleaned.csv"
        
        if not data_path.exists():
            # Try alternative path
            data_path = project_root / "Data" / "1_raw" / "student_performance.csv"
            
        df = pd.read_csv(data_path)
        print(f"✅ Loaded {len(df)} student records from {data_path}")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
    
    datasets = {}
    
    # 1. Main student dataset with enhanced columns
    main_df = df.copy()
    
    # Add calculated columns for Power BI
    main_df['Performance_Category'] = pd.cut(
        main_df['total_score'],
        bins=[0, 60, 70, 80, 90, 100],
        labels=['At Risk', 'Needs Improvement', 'Good', 'Very Good', 'Excellent']
    )
    
    main_df['Attendance_Category'] = pd.cut(
        main_df['attendance_percentage'],
        bins=[0, 70, 85, 95, 100],
        labels=['Poor', 'Average', 'Good', 'Excellent']
    )
    
    main_df['Study_Hours_Category'] = pd.cut(
        main_df['weekly_self_study_hours'],
        bins=[0, 3, 6, 10, np.inf],
        labels=['Low', 'Medium', 'High', 'Very High']
    )
    
    main_df['Participation_Category'] = pd.cut(
        main_df['class_participation'],
        bins=[0, 4, 6, 8, 10],
        labels=['Low', 'Moderate', 'Active', 'Very Active']
    )
    
    datasets['student_data'] = main_df
    
    # 2. KPI Summary Table
    kpi_df = pd.DataFrame({
        'KPI_Name': [
            'Total Students',
            'Average Score',
            'Students with Good Attendance (>85%)',
            'Students with Adequate Study Hours (>5hrs)',
            'Active Participants (>7)',
            'Excellent Performers (Score >85)'
        ],
        'KPI_Value': [
            len(main_df),
            round(main_df['total_score'].mean(), 1),
            len(main_df[main_df['attendance_percentage'] > 85]),
            len(main_df[main_df['weekly_self_study_hours'] > 5]),
            len(main_df[main_df['class_participation'] > 7]),
            len(main_df[main_df['total_score'] > 85])
        ]
    })
    
    # Calculate percentages
    kpi_df['KPI_Percentage'] = kpi_df['KPI_Value'].copy()
    kpi_df.loc[0, 'KPI_Percentage'] = 100  # Total students = 100%
    kpi_df.loc[1, 'KPI_Percentage'] = (main_df['total_score'].mean() / 100) * 100
    for i in range(2, len(kpi_df)):
        kpi_df.loc[i, 'KPI_Percentage'] = (kpi_df.loc[i, 'KPI_Value'] / len(main_df)) * 100
    
    datasets['kpi_summary'] = kpi_df
    
    # 3. Grade Distribution
    grade_dist = main_df['grade'].value_counts().reset_index()
    grade_dist.columns = ['Grade', 'Student_Count']
    grade_dist['Percentage'] = (grade_dist['Student_Count'] / len(main_df)) * 100
    
    datasets['grade_distribution'] = grade_dist
    
    return datasets

def export_powerbi_files(datasets=None, output_dir=None):
    """
    Export datasets to files suitable for Power BI import
    """
    if datasets is None:
        datasets = prepare_powerbi_data()
        if datasets is None:
            return None
    
    if output_dir is None:
        project_root = Path.cwd()
        while project_root.name != "capstone-student-performance" and project_root.parent != project_root:
            project_root = project_root.parent
        output_dir = project_root / "dashboard" / "data"
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    exported_files = {}
    
    # Export each dataset
    for dataset_name, df in datasets.items():
        # Export to CSV (primary format for Power BI)
        csv_path = output_dir / f"{dataset_name}_{timestamp}.csv"
        df.to_csv(csv_path, index=False)
        exported_files[f"{dataset_name}_csv"] = csv_path
        print(f"📄 Exported: {csv_path}")
    
    # Create consolidated Excel workbook
    consolidated_path = output_dir / f"student_performance_powerbi_{timestamp}.xlsx"
    with pd.ExcelWriter(consolidated_path, engine='openpyxl') as writer:
        for dataset_name, df in datasets.items():
            sheet_name = dataset_name.replace('_', ' ').title()[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    exported_files['consolidated_excel'] = consolidated_path
    print(f"📋 Consolidated Excel: {consolidated_path}")
    
    return exported_files

def main():
    """
    Main function to prepare and export Power BI dashboard data
    """
    print("🚀 Preparing Power BI Dashboard Data...")
    
    # Prepare datasets
    datasets = prepare_powerbi_data()
    if datasets is None:
        print("❌ Failed to prepare data")
        return None, None
    
    # Export files
    exported_files = export_powerbi_files(datasets)
    
    print("\n✅ Power BI Dashboard Data Prepared Successfully!")
    print(f"\n📊 Datasets created: {len(datasets)}")
    for name, df in datasets.items():
        print(f"   • {name}: {len(df)} rows, {len(df.columns)} columns")
    
    print("\n🎯 Next Steps for Power BI:")
    print("   1. Open Power BI Desktop")
    print("   2. Import the Excel file or CSV files")
    print("   3. Create visualizations")
    print("   4. Build your dashboard")
    
    return exported_files, datasets

if __name__ == "__main__":
    main()

print("📊 Power BI template loaded! Run main() to export data.")
