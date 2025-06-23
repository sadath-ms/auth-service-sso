# 🔐 SSO Authentication Microservice

A production-ready Single Sign-On (SSO) microservice built with **Flask + SQLAlchemy**, designed to provide secure authentication and authorization for multiple client applications using:

- ✅ Email/Password Auth
- 🌐 OAuth2 Social Login (e.g., Google, GitHub)
- 📦 JWT Access & Refresh Tokens
- 👥 Role-Based Access Control (RBAC)
- 🧭 Session and Audit Tracking

---

## 📁 Project Structure

auth_service/
├── app/
│ ├── models/
│ │ ├── user.py
│ │ ├── identity.py
│ │ ├── application.py
│ │ ├── role.py
│ │ ├── session.py
│ │ └── token.py
│ ├── config.py
│ ├── extensions.py
│ └── init.py
├── templates/
│ └── swagger.html
├── openapi.json
├── run.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/sso-auth-service.git
cd sso-auth-service


flask db init
flask db migrate -m "initial"
flask db upgrade

🧩 Core Models Overview

🧑‍💼 User
Basic account info.

id, email, password_hash, is_active, created_at, updated_at

🌐 Identity
External OAuth identities.

provider, provider_uid, email, user_id

🏢 Application
Client applications (e.g., Eduvate, OpenText).

name, client_id, client_secret, redirect_uris

🛡️ Role / UserRole
RBAC system.

role_id, user_id, application_id

📲 Session
Login metadata (IP, device, time).

user_id, user_agent, ip_address, login_time, logout_time

🔁 RefreshToken
Refresh JWT tokens securely.

user_id, token, issued_at, expires_at, is_revoked

 Sample Endpoints (Planned)
Endpoint	Method	Description
/auth/register	POST	Register new user
/auth/login	POST	Login with credentials
/auth/google	GET	Google OAuth login
/auth/refresh	POST	Refresh JWT
/users/<id>/roles	POST	Assign user roles
/sessions	GET	View login history



docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Initial migration"
docker-compose exec web flask db upgrade
docker-compose exec web flask shell