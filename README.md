# Browser Security Demonstration

## Overview

This project demonstrates how web browsers request access to hardware (camera and microphone) and highlights the security implications of granting permissions.

It uses **Flask**, **OpenCV**, **HTML**, and **JavaScript** to:

- Display a landing page with group/student information
- Access the webcam and microphone after user permission
- Record video locally
- Display device information (browser, OS, screen resolution, timezone)
- Show a security warning about potential misuse of hardware access

> ⚠ Note: This project is purely for educational purposes.

---

## Folder Structure
browser-security-demo/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── README.md               # Project description for GitHub
├── recordings/             # Folder to store recorded videos
│
├── templates/
│     └── index.html        # Landing page HTML
│
└── static/                 # Optional: CSS/JS/images
      ├── style.css
      └── script.js
