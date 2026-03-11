# Library Management API

A Django REST API for managing a library’s books, members, and borrowing process. It allows librarians to manage inventory and members, and provides endpoints for tracking loans, returns, and overdue items.

## Table of Contents

- Overview
- Features
- Tech Stack
- Project Structure
- Getting Started
- Running Migrations and Tests
- API Endpoints (Examples)
- Original/Advanced Features
- Future Improvements
- License

## Overview

This project is my capstone project for [INSTITUTION / PROGRAM NAME]. It solves the problem of manually tracking library records by providing a centralized, API‑driven system.

The API is designed for:
- Librarians who manage books and members.
- Other systems (e.g. a frontend, mobile app, or admin dashboard) that consume the API.

## Features

Core features:
- Manage books (create, list, update, delete).
- Manage members (registration, update details, deactivate).
- Borrow and return books.
- Track availability and prevent double‑issuing of the same copy.

Extra/original features:
- Automatic fine calculation for overdue books.
- Simple analytics endpoints (e.g. most borrowed books, total active loans).

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development)

## Project Structure

Main folders:

- `config/` – Django project configuration (settings, URLs, WSGI/ASGI).
- `library/` – Main app with models, serializers, views, and URLs for the library domain.
- `requirements.txt` – Python dependencies.
- `manage.py` – Django management script.

You can adjust this section if your actual app name or structure is different.

## Getting Started

### Prerequisites

- Python 3.x
- Git
- Virtual environment tool (e.g. `venv`)

### Installation

```bash
# Clone the repository
git clone https://github.com/Grace-254/library-management-api.git
cd library-management-api

# Create and activate a virtual environment (example for Linux/Mac)
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
