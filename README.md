# CloudSync

A cloud-hosted task management app built during my Cloud Computing internship at Codtech IT Solutions Pvt. Ltd.

## Tech Stack
- Backend: Python (Flask) — hosted on AWS EC2
- Frontend: HTML, CSS, JavaScript — hosted on AWS S3
- Cloud Platform: AWS (EC2, S3)

## Features
- Add, edit, delete tasks
- Mark tasks as complete with an animated checkbox
- Search tasks
- Live progress tracking

## Architecture
The frontend is hosted as a static website on an AWS S3 bucket. It communicates with a Flask backend running on an AWS EC2 instance via REST API calls to manage tasks.

## Running the app
1. Log in to the AWS Management Console
2. Go to **EC2** and start the `task-manager-server` instance
3. Once running, note the instance's public IPv4 address (it may change on restart unless an Elastic IP is attached)
4. SSH into the instance and run the backend:
5. Update the `API` variable in `frontend/index.html` with the instance's current address if it changed
6. Open the S3-hosted frontend URL (or `frontend/index.html` directly) in a browser
