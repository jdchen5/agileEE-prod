# app.py - Hugging Face Spaces entry point (renamed from run_agileee.py)
import os
import sys

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Set environment variables for production
os.environ['DEBUG'] = 'false'
os.environ['STREAMLIT_PRODUCTION'] = 'true'

# Import and run the main application directly
if __name__ == "__main__":
    from agileee.ui import main
    main()