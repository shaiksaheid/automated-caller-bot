# 📞 AI Powered Automated Caller Bot

A full-stack web application that automates student attendance tracking and notifies parents through real-time voice calls. The system enhances academic monitoring by improving communication between institutions and parents using AI and cloud telephony.

---

## 🧩 Features

* 👥 Admin Dashboard for managing students and attendance
* 📝 Digital Attendance Management System
* 📞 Automated Voice Calls to parents for absenteeism
* 🔄 Real-time Call Triggering using Twilio API
* 📋 Call Logs with status, duration, and response tracking
* 📊 Analytics & Risk Analysis based on attendance patterns
* 📂 Bulk Calling Feature for multiple students
* 🎙️ Voice Response Recording and Transcription
* 🧠 AI-based Excuse Classification and Risk Detection
* 🗄️ PostgreSQL Integration for structured data management

---

## 🛠️ Tech Stack

| Component  | Technology                     |
| ---------- | ------------------------------ |
| Backend    | Python, FastAPI                |
| Frontend   | React.js                       |
| Database   | PostgreSQL                     |
| ORM        | SQLAlchemy                     |
| APIs       | Twilio (Voice & SMS)           |
| AI Modules | Speech-to-Text, Classification |
| Scheduler  | APScheduler                    |

---

## 📁 Project Structure

```
automated-caller-bot/
│
├── backend/
│   ├── app/
│   │   ├── api/routes/          # API routes (admin, calls, students, etc.)
│   │   ├── core/                # Config & security
│   │   ├── database/            # DB models and connection
│   │   ├── services/            # AI, Twilio, transcription, risk engine
│   │   ├── utils/               # Helper utilities
│   │   ├── workers/             # Background workers
│   │   └── main.py              # FastAPI entry point
│
├── assets/                      # Static assets (logo, etc.)
├── reports/                     # Generated reports
│
├── requirements.txt             # Dependencies
├── Procfile                     # Deployment config (optional)
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```
git clone https://github.com/shaiksaheid/automated_caller_bot.git
cd automated-caller-bot
```

---

### 2️⃣ Create and Activate Virtual Environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set Up PostgreSQL Database

* Create a PostgreSQL database
* Configure database credentials in your `.env` or config file
* Run migrations (if applicable)

---

### 5️⃣ Configure Twilio

* Create a Twilio account
* Get your **Account SID, Auth Token, and Phone Number**
* Add them in environment variables

---

### 6️⃣ Run the Application

```
uvicorn app.main:app --reload
```

---

### 7️⃣ Access the Application

Open your browser:
👉 http://localhost:8000

---

## 🧪 Key Functionalities

* Mark attendance and automatically trigger calls
* Record and store parent responses
* Convert voice to text using transcription
* Classify excuses using AI models
* Identify high-risk students based on attendance patterns
* Send SMS alerts for critical cases

---

## 🧠 Future Enhancements

* Multilingual voice support
* Real-time conversational AI (two-way calling)
* Predictive analytics for student performance
* Mobile app integration
* Advanced dashboard with visual analytics

---

## 📄 License

This project was developed as part of the **Mini Project (AI & ML)** coursework
CMR Technical Campus – Department of CSE (AI & ML)
Academic Year: 2025–2026

---

## 👨‍💻 Author

**Shaik Shaheid**
GitHub: https://github.com/shaiksaheid

---
