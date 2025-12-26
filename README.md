# QPS Solutions Private Limited – Flask Website

This project is a Flask-based web application for the QPS Solutions Private Limited website. It serves a multi-page responsive site built using Bootstrap templates, custom styling, and static assets. The application provides dedicated routes for key website sections and renders corresponding HTML templates.

---

## Overview

The application is designed as a simple web server that delivers static and templated pages. It uses Flask for routing and template rendering, Bootstrap for layout and styling, and a small custom stylesheet for additional UI enhancements.

The site currently includes:

* Home page with carousel section
* About page
* Services page
* FAQ page
* Contact page
* Shared base layout with navigation bar, footer, and styling

---

## Features

* Flask application with clear route structure
* Modular HTML templates using Jinja2 and base layout inheritance
* Static asset handling for CSS and images
* Bootstrap-based responsive design
* Custom date formatting filter included in the application
* Ready for deployment with Gunicorn support

---

## Tech Stack

* **Backend Framework:** Flask
* **Template Engine:** Jinja2
* **Frontend:** HTML, CSS, Bootstrap
* **Server (optional deployment):** Gunicorn

Dependencies are listed in `requirements.txt`.

---

## Project Structure

```
Project-main/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom stylesheet
│   └── images/
│       └── logo.png           # Site logo
│
└── templates/
    ├── base.html              # Base layout
    ├── home.html              # Home page
    ├── about.html             # About page
    ├── services.html          # Services page
    ├── faq.html               # FAQ page
    └── contact.html           # Contact page
```

---

## Installation

1. Ensure Python is installed.
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the Flask application using:

```bash
python app.py
```

The application starts in development mode and will typically be available at:

```
http://127.0.0.1:5000/
```

Routes available in the project:

* `/` – Home
* `/about` – About
* `/services` – Services
* `/faq` – FAQ
* `/contact` – Contact

---

## Deployment

Gunicorn is included in the dependencies, allowing the application to run in a production-oriented environment such as Linux servers or container setups. Use a command similar to:

```bash
gunicorn app:app
```

(Adjust as needed based on hosting environment.)

---

## Notes

* The project uses Bootstrap CDN references inside templates.
* Static assets are served via Flask’s `static` directory.
* Page content is rendered using template inheritance from the shared `base.html`.

---

## Author / Credits

The project credits, organization name, and branding are included within the template files as part of the website content for QPS Solutions Private Limited.

---
