# laptime-analyzer

`python -m venv venv`
`.\venv\Scripts\activate`

`pip install django psycopg2-binary`
`pip install gunicorn django-heroku`

`django-admin startproject PKB`

`echo "venv/" > .gitignore`
`echo "*.pyc" >> .gitignore`
`echo "__pycache__/" >> .gitignore`
`echo "*.sqlite3" >> .gitignore`

```
# Access PostgreSQL
psql

# In the PostgreSQL shell, run these commands:
CREATE DATABASE pkb_db;
CREATE USER pkb_user WITH PASSWORD 'your_password';
ALTER ROLE pkb_user SET client_encoding TO 'utf8';
ALTER ROLE pkb_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pkb_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pkb_db TO pkb_user;
\q
```

`echo "web: gunicorn PKB.wsgi" > Procfile`
`echo "python-3.12.6" > runtime.txt`
`pip freeze > requirements.txt`

heroku login



# Roadmap for Implementation
## 1. Set Up the Base Project

- Start by creating your Django project and setting up the basic apps (`home`, `accounts`).
```
django-admin startproject PKB .
python manage.py startapp home
python manage.py startapp accounts
```

- Home app: Create a simple home page view that displays information about you and your services.

- Accounts app: Set up user registration, login, and profile management. Use Django’s authentication system.

## 2. User Authentication & Account Management
- Install django-allauth to handle account creation, login, social logins, etc.

    `pip install django-allauth`

- Set up user registration and login pages, and create user profiles. You can extend Django's default user model to store additional information like driver roles (e.g., Coach or Driver).

    - For example:
    - is_coach (boolean): to distinguish between coaches and drivers.
    - drivers: Coaches can see and leave feedback for specific drivers.

## 3. Coaching Sessions & Lap Time Uploads
- Sessions App: Create a sessions app where coaches can upload an XLSX file with driver names and lap times.

    `python manage.py startapp sessions`
- Use libraries like pandas or openpyxl to parse the uploaded Excel files and store lap time data in your database.

    `pip install pandas openpyxl`
- Create models to store session data:

    - Session: Date, track, conditions, etc.
    - LapTime: ForeignKey to Session, driver, lap times, etc.


## 4. Display Session Data and Interactive Graphs
- Metrics/Analysis App: Create the metrics app for analyzing driver data and displaying it in graphs.
    `python manage.py startapp metrics`
- Use Plotly or Chart.js for interactive graphs to visualize performance over time.

    `pip install django-plotly-dash`
- Features:

    - Show all driver sessions.
    - Drill down into individual sessions.
    - Visualize lap time consistency, best lap, averages, etc.
    - Compare performance with other drivers.

## 5. Feedback System for Coaches
- Feedback App: Create the feedback app where coaches can leave personalized feedback for each driver after a session.

    `python manage.py startapp feedback`
- Link feedback to individual Session objects, and display it to the relevant driver.

## 6. Subscription and Payments
- Payments App: Integrate payment processing to offer subscription plans for drivers using Stripe or PayPal.
    `pip install django-stripe`
- Handle different tiers of subscriptions (e.g., basic vs. premium features like detailed performance analysis).

## 7. News Feed for Updates
- News App: Create the news app where you can post updates, news, and events for drivers.

    `python manage.py startapp news`
- Simple news post model with title, content, and publication date. Create a view to list all posts.

## 8. Bookings (bookings):

- Allows drivers to book private coaching sessions by selecting available dates, times, and prices.
- Manages session availability, pricing, and reminders for upcoming sessions.
- Sends notifications (email or in-app) to remind users of upcoming coaching sessions.

## 9. Groups (groups):

- Organizes drivers into groups (e.g., beginners, advanced, or specific training teams).
- Tracks participation in sessions based on groups.

## 10. Calendar (calendar):

- Provides an interactive calendar for both coaches and drivers to manage, plan, and view upcoming coaching sessions.
- Allows the coach to block out available time slots for private coaching sessions.


## 11. A personalized dashboard 
- Drivers can view their sessions, graphs, feedback, and compare their performance with others.

## 12. Coach Dashboard:

- Admin-like interface where you can easily manage sessions, upload new data, and leave feedback for drivers.

## Performance Alerts:

- Send drivers notifications or emails when their performance improves or drops significantly.
Leaderboard:

- Show leaderboards for lap times, consistency, or other metrics to encourage competition.



Roadmap Summary:
Initial Setup:

Base project with home and accounts apps for landing page and authentication.
User Management:

Set up user registration, login, and profile management.
Coaching Sessions:

Build session and lap time upload features (using pandas to parse Excel data).
Driver Metrics & Graphs:

Display interactive graphs for performance data and comparisons.
Feedback & News:

Allow coaches to leave feedback and manage a news feed for updates.
Subscription and Payments:

Add payment functionality with Stripe for subscription-based access to advanced features.
Driver/Coach Dashboards:

Create personalized dashboards for both drivers and coaches to track sessions and performance.