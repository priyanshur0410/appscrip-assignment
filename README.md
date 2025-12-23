Trade Opportunities API
A FastAPI service that analyzes market data and provides trade opportunity insights for specific sectors in India.

🌟 Features
Sector Analysis: Analyze specific Indian sectors (pharmaceuticals, technology, agriculture, etc.)

AI-Powered Insights: Uses Google Gemini AI for market analysis

Real-time Data: Collects current market data and news using web search

Structured Reports: Generates markdown reports with trade opportunities

Security: JWT authentication with rate limiting

Session Management: Track API usage per user

RESTful API: Well-documented endpoints with OpenAPI support

🚀 Quick Start
Prerequisites
Python 3.8 or higher

Google Gemini API key (free from Google AI Studio)

Installation
Clone the repository

bash
git clone https://github.com/yourusername/trade-opportunities-api.git
cd trade-opportunities-api
Create virtual environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Configure environment variables

bash
# Copy example environment file
cp .env.example .env

# Edit .env file and add your Gemini API key
# GEMINI_API_KEY=your_actual_gemini_api_key_here
Run the application

bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The API will be available at http://localhost:8000

📚 API Documentation
Once the server is running, you can access:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

OpenAPI JSON: http://localhost:8000/openapi.json
