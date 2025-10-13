# 📊 Dashboard Visualization Components
"""
Reusable visualization components for Student Performance Dashboard
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class StudentPerformanceVisualizer:
    """
    Class for creating student performance visualizations
    """
    
    def __init__(self, df):
        """Initialize with student data"""
        self.df = df
        self.setup_style()
    
    def setup_style(self):
        """Setup visualization styling"""
        sns.set_style("whitegrid")
        plt.rcParams.update({
            'figure.figsize': (12, 8),
            'font.size': 11,
            'axes.titlesize': 14
        })
        
        # Color palette
        self.colors = {
            'primary': '#1f77b4',
            'secondary': '#ff7f0e', 
            'success': '#2ca02c',
            'warning': '#d62728'
        }
    
    def create_score_distribution(self, save_path=None):
        """Create score distribution visualization"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Histogram
        ax1.hist(self.df['total_score'], bins=20, color=self.colors['primary'], 
                alpha=0.7, edgecolor='black')
        ax1.set_xlabel('Total Score')
        ax1.set_ylabel('Frequency') 
        ax1.set_title('Distribution of Total Scores')
        ax1.grid(True, alpha=0.3)
        
        # Box plot by grade
        sns.boxplot(data=self.df, x='grade', y='total_score', ax=ax2)
        ax2.set_xlabel('Grade')
        ax2.set_ylabel('Total Score')
        ax2.set_title('Score Distribution by Grade')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def create_correlation_heatmap(self, save_path=None):
        """Create correlation heatmap"""
        numeric_cols = ['weekly_self_study_hours', 'attendance_percentage', 
                       'class_participation', 'total_score']
        
        correlation_matrix = self.df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
                   center=0, square=True, ax=ax, cbar_kws={'shrink': 0.8})
        
        ax.set_title('Correlation Matrix of Performance Factors', fontsize=16, pad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        return fig
    
    def create_factor_analysis(self, save_path=None):
        """Create multi-factor analysis visualization"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 1. Study hours vs Performance
        sns.scatterplot(data=self.df, x='weekly_self_study_hours', y='total_score', 
                       hue='grade', ax=ax1, s=100, alpha=0.7)
        sns.regplot(data=self.df, x='weekly_self_study_hours', y='total_score', 
                   ax=ax1, scatter=False, color='red')
        ax1.set_title('Study Hours vs Academic Performance')
        ax1.legend(title='Grade')
        
        # 2. Attendance vs Performance
        sns.scatterplot(data=self.df, x='attendance_percentage', y='total_score',
                       hue='grade', ax=ax2, s=100, alpha=0.7)
        sns.regplot(data=self.df, x='attendance_percentage', y='total_score',
                   ax=ax2, scatter=False, color='red')
        ax2.set_title('Attendance vs Academic Performance')
        ax2.legend(title='Grade')
        
        # 3. Participation vs Performance
        sns.scatterplot(data=self.df, x='class_participation', y='total_score',
                       hue='grade', ax=ax3, s=100, alpha=0.7)
        sns.regplot(data=self.df, x='class_participation', y='total_score',
                   ax=ax3, scatter=False, color='red')
        ax3.set_title('Participation vs Academic Performance')
        ax3.legend(title='Grade')
        
        # 4. Grade distribution
        grade_counts = self.df['grade'].value_counts()
        ax4.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%',
               startangle=90)
        ax4.set_title('Grade Distribution')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        return fig
    
    def create_summary_dashboard(self, save_path=None):
        """Create comprehensive summary dashboard"""
        fig = plt.figure(figsize=(20, 12))
        
        # Create grid layout
        gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
        
        # 1. Score histogram
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.hist(self.df['total_score'], bins=15, color=self.colors['primary'], alpha=0.7)
        ax1.set_title('Score Distribution')
        ax1.set_xlabel('Total Score')
        ax1.set_ylabel('Count')
        
        # 2. Grade pie chart
        ax2 = fig.add_subplot(gs[0, 1])
        grade_counts = self.df['grade'].value_counts()
        ax2.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%')
        ax2.set_title('Grade Distribution')
        
        # 3. Correlation heatmap
        ax3 = fig.add_subplot(gs[0, 2:])
        numeric_cols = ['weekly_self_study_hours', 'attendance_percentage', 
                       'class_participation', 'total_score']
        corr = self.df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax3)
        ax3.set_title('Correlation Matrix')
        
        # 4. Study hours vs score
        ax4 = fig.add_subplot(gs[1, :2])
        sns.scatterplot(data=self.df, x='weekly_self_study_hours', y='total_score', 
                       hue='grade', ax=ax4)
        ax4.set_title('Study Hours vs Performance')
        
        # 5. Attendance vs score
        ax5 = fig.add_subplot(gs[1, 2:])
        sns.scatterplot(data=self.df, x='attendance_percentage', y='total_score',
                       hue='grade', ax=ax5)
        ax5.set_title('Attendance vs Performance')
        
        # 6. Box plots by grade
        ax6 = fig.add_subplot(gs[2, :])
        factors = ['weekly_self_study_hours', 'attendance_percentage', 'class_participation']
        df_melted = self.df.melt(id_vars=['grade'], value_vars=factors,
                               var_name='Factor', value_name='Value')
        sns.boxplot(data=df_melted, x='Factor', y='Value', hue='grade', ax=ax6)
        ax6.set_title('Performance Factors by Grade')
        ax6.set_xticklabels(['Study Hours', 'Attendance %', 'Participation'])
        
        fig.suptitle('Student Performance Analysis Dashboard', fontsize=20, y=0.98)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        return fig

def calculate_summary_stats(df):
    """Calculate summary statistics"""
    stats = {
        'total_students': len(df),
        'avg_score': df['total_score'].mean(),
        'avg_attendance': df['attendance_percentage'].mean(),
        'avg_study_hours': df['weekly_self_study_hours'].mean(),
        'avg_participation': df['class_participation'].mean()
    }
    
    # Grade distribution
    grade_dist = df['grade'].value_counts().to_dict()
    stats['grade_distribution'] = grade_dist
    
    # Performance levels
    stats['excellent_performers'] = len(df[df['total_score'] >= 85])
    stats['good_performers'] = len(df[(df['total_score'] >= 70) & (df['total_score'] < 85)])
    stats['needs_improvement'] = len(df[df['total_score'] < 70])
    
    return stats

print("📊 Visualization components loaded!")
print("🎨 Available classes and functions:")
print("   - StudentPerformanceVisualizer")
print("   - calculate_summary_stats()")
