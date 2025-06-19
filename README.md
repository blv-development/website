
# BLV Developers Website

> The official source code for [blvdevelopers.org](https://blvdevelopers.org), our community's home on the web.

## Welcome!

This repository contains everything needed to build, run, and deploy the BLV Developers website. This project is a living application, built by the community, for the community. It serves as our main platform for sharing resources, showcasing projects, and connecting with new members.

While our `docs-and-learning` repository is the place to learn the ropes, this is where we put those skills into practice. We're excited to have you contribute!

## Tech Stack at a Glance

We've chosen a modern, robust, and scalable tech stack. This allows us to build a feature-rich platform while also providing a great learning experience for contributors working with industry-standard tools.

*   **Backend**: **Django** & **Django REST Framework**. A powerful Python framework that provides a solid foundation for our API, user management, and business logic.
*   **Frontend**: **React**. A leading JavaScript library for building dynamic and accessible user interfaces. We use **Vite** for a fast and modern development experience.
*   **Database**: **PostgreSQL**. A battle-tested, open-source relational database known for its reliability and data integrity.
*   **Containerization**: **Docker** & **Docker Compose**. We use Docker to containerize our applications, ensuring a consistent and reproducible development environment for every contributor, regardless of their local machine setup.
*   **Web Server / Proxy**: **Nginx**. A high-performance web server that will act as a reverse proxy in production, serving our static frontend assets and routing API traffic to the Django application.
*   **Application Server**: **Gunicorn**. A production-grade WSGI server to run our Django application.
*   **CI/CD**: **GitHub Actions**. For automating our testing, building, and deployment pipeline directly from our repository.

## Getting Started: Running Locally

Thanks to Docker, getting a full local development environment running is straightforward. You won't need to install Python, Node, or PostgreSQL on your machine directly—Docker handles it all.

### Prerequisites

1.  **Git**: To clone the repository.
2.  **Docker** and **Docker Compose**: Please follow the official installation guides for your operating system.

### Setup Instructions

1.  **Clone the Repository**
    First, get a copy of the code on your local machine.
    ```bash
    git clone https://github.com/blv-devs/website.git
    cd website
    ```

2.  **Configure Environment Variables**
    We use environment variables to manage secret keys and settings. We've provided an example file to get you started.
    ```bash
    # For the backend
    cp backend/.env.example backend/.env

    # For the frontend
    cp frontend/.env.example frontend/.env
    ```
    Now, open `backend/.env` and `frontend/.env` in your editor. The example files contain sensible defaults for local development. For the backend, you'll need to generate a new `SECRET_KEY`.

3.  **Build and Run the Containers**
    This one command tells Docker Compose to build the images for our frontend and backend services (if they don't exist yet) and start them up.
    ```bash
    docker-compose up --build
    ```
    Grab a coffee, as the first build can take a few minutes. Subsequent builds will be much faster.

4.  **Run Initial Database Migrations**
    With the containers running, open a **new terminal window** and run the initial Django database migrations to set up your PostgreSQL database schema.
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

5.  **Create a Superuser (Optional)**
    If you want to access the Django admin panel, you'll need to create a superuser.
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```

You're all set! The application is now running:
*   **React Frontend**: [http://localhost:3000](http://localhost:3000)
*   **Django API**: [http://localhost:8000](http://localhost:8000)

## Project Structure

This repository is a "monorepo" containing both our frontend and backend projects.

```
/
+-- backend/         # All Django-related code, APIs, and models.
+-- frontend/        # All React-related code, components, and pages.
+-- .github/         # CI/CD workflows for GitHub Actions.
+-- docker-compose.yml # Defines our multi-container Docker application.
+-- README.md        # You are here!
```

## Deployment Architecture

Our goal is a portable, scalable, and easily managed production environment.

*   **Provider**: We will be deploying to a **DigitalOcean Droplet**.
*   **CI/CD Pipeline**: A GitHub Actions workflow is configured to trigger on merges to the `main` branch. It will:
    1.  Run all backend and frontend tests to ensure code quality.
    2.  Build optimized production Docker images for the Django and React apps.
    3.  Push the new images to a container registry (e.g., DigitalOcean Container Registry).
    4.  Securely connect to our DigitalOcean Droplet, pull the latest images, and restart the services with zero downtime.
*   **Database & Backups**: To ensure data safety and portability, the PostgreSQL database will **not** be run on the same Droplet as the application. We will use a **DigitalOcean Managed PostgreSQL Database**. This separates our application's state from its logic, simplifies backups (with point-in-time recovery), and makes scaling or migrating our application server much easier in the future.

## How to Contribute

We follow the same collaborative workflow used across the BLV Devs organization. Please refer to our main `git.md` guide in the `docs-and-learning` repository for a full breakdown.

The short version:
1.  Create an issue to discuss a new feature or bug.
2.  Create a new branch from `main` for your work.
3.  Do your magic!
4.  Open a Pull Request for review.

We're incredibly excited to build this platform with you. Let's make something amazing.