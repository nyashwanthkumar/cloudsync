# Cloud Task Manager

A simple cloud-hosted task management web app built during my Cloud Computing internship at Codtech IT Solutions Pvt. Ltd.

## Tech Stack
- Backend: Python (Flask) — hosted on AWS EC2
- Frontend: HTML, CSS, JavaScript — hosted on AWS S3
- Cloud Platform: AWS (EC2, S3)

## Features
- Add, edit, delete tasks
- Mark tasks as complete
- Search tasks

## Architecture
The frontend (HTML/CSS/JS) is hosted as a static website on an AWS S3 bucket. It communicates with a Flask backend running on an AWS EC2 instance via REST API calls to manage tasks.

## Run locally
1. `pip install -r requirements.txt`
2. `python backend/app.py`
3. Open `frontend/index.html` in your browser
