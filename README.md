The aim of the repo is to run pipeline on pi and create a webpage which can automatically be triggered by actions(maybe?), 
also more can be added :)

Things It can do 
1. Host a API server on PI.
2. API endpoints at <ip>/docs.
3. current endpoints shows IP, temps, cpu, and disk usage.

Things planned to add.
1. Dashboard for the above endpoints using react.
2. CI/CD Pipeline set up for any code push and deployment.


Install pip

# To set up local environment
python3 -m venv venv 

# To enter venv
source venv/bin/activate

# Install library
pip install -r requirement.txt

# To run the backend
cd backend
uvicorn main:app --host 0.0.0.0 --reload 
