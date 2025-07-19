from setuptools import setup, find_packages

setup(
    name="agileee",
    version="0.1.0",
    description="AgileEE - Agile Effort Estimator",
    author="Jing Chen",
    author_email="j.chen34@unimail.derby.ac.uk",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "plotly>=5.15.0",
        "seaborn>=0.12.0",
        "openpyxl>=3.1.0",
        "joblib>=1.3.0",
        "scikit-learn>=1.4.0",
        "pycaret==3.3.2",
        "pyyaml>=6.0",
        "shap>=0.47.0"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "agileee-app=agileee.main:main",
        ],
    },
)