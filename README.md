# 🐾 Flask Cat-Dog Voting App — CI/CD Automation Project

This project demonstrates a complete **CI/CD pipeline** built around a simple Flask voting app. It showcases how DevOps automation works using tools like **Jenkins, Docker, Docker Hub**, and **NGINX** — focusing on the process more than the code.

> ⚠️ **Note:** This project emphasizes automation and CI/CD practices — not complex application logic. It's designed to reflect real-world DevOps workflows.

---

## 📌 Project Overview

This repo contains a basic Flask web app where users can vote between a **cat** and a **dog**.  
The highlight of the project is its **automated deployment pipeline**, not the application code itself.

---

## 🔧 Tools & Technologies Used

- **Jenkins** – for CI/CD orchestration  
- **Docker** – to containerize the application  
- **Docker Hub** – for image storage (`soniya06/flask-project`)  
- **NGINX** – as a reverse proxy (ports not exposed)  
- **GitHub** – for source code and webhook integration  

---

## 🔄 CI/CD Pipeline Flow

1. Jenkins pulls the latest code from GitHub  
2. Builds a Docker image using the `Dockerfile`  
3. Pushes the image to Docker Hub  
4. Runs the container securely behind NGINX using container IP  

---

## Author

**Soniya Kothari**  
📧 [soniyakothari06@gmail.com](mailto:soniyakothari06@gmail.com)
