import sys
import os

# 👇 Add parent directory to Python path so that 'app' can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 👇 Import the Flask app from your main app.py file
from app import app


def test_home_route():
    """Test that the home route ("/") loads successfully"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

