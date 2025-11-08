# 🛠️ RESTful Authentication API with JWT & Email OTP Verification

This project provides a secure **RESTful Authentication System** built with **JWT (JSON Web Token)** and **Email OTP verification**.  
Users can **register**, **verify email via OTP**, **log in/log out**, and **manage their profile** securely.

---

## 🚀 Features

- 🔐 **JWT-based Authentication**
  - Login & Logout endpoints using JWT access and refresh tokens.
- 📧 **Email OTP Verification**
  - When a user registers, an OTP is sent to their email.
  - User verifies OTP using `/email-verify/` endpoint to activate the account.
- 👥 **Users Endpoint**
  - `/users/` endpoint lists **only active users**.
  - Protected by authentication (JWT token required).
- 🧑‍💻 **Profile Management**
  - Authenticated users can update **only their own profile**.
  - Other users’ profiles are **read-only**.

---

## ⚙️ Tech Stack

- **Backend:** Django / Django REST Framework
- **Authentication:** JWT (SimpleJWT or similar)
- **Email Verification:** Django’s `EmailMessage` with SMTP backend
- **Database:** SQLite
- **Environment Variables:** `.env` file for sensitive info

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd user_authentication
   ```
2. **Create and Activate Virtual Environment**
    ```
    Windows:

    python -m venv .venv
    venv\Scripts\activate
    ```
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Setup**
   Create a `.env` file in the root directory with the following configurations:

   ```env
   SECRET_KEY =Your-project-secret-key
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   DEFAULT_FROM_EMAIL=your-email@gmail.com
   ```

   Replace the email credentials with your own.

5. **Database Setup**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
