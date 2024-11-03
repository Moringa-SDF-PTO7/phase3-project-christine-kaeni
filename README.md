# phase3-project-christine-kaeni
# Behavior Tracker CLI Application

## Project Overview
The Behavior Tracker is a Command Line Interface (CLI) application built using Python. Its purpose is to help users track behaviors over time, log progress, and monitor patterns. This tool is ideal for anyone looking to build positive habits or monitor particular behaviors.

## Features
- **User Management**: Create and manage user profiles for tracking behaviors.
- **Behavior Tracking**: Define behaviors to track and log observations.
- **Progress Monitoring**: View and analyze behavior trends.

## Requirements
- Python 3.8+
- Pipenv (for managing dependencies)

## Installation
1. Clone the repository:
2. Move into the directory
Install dependencies:

pipenv install
Activate the virtual environment:

pipenv shell
Usage
Run the application:

python cli.py
Navigate through the menu to:
Add users and behaviors.
Track behaviors.
View progress reports.
File Structure
cli.py: Main CLI logic for user interaction.
models:
user.py: Manages user profiles.
behavior.py: Manages behaviors and logs.
database.py: Manages database connection and setup.
Pipfile: Dependency file for setting up the environment.
Database Structure
The application uses SQLAlchemy ORM to interact with a SQLite database.

User Model: Stores user information.
Behavior Model: Stores behaviors with attributes like name and frequency.
Logs Model: Stores log entries linked to users and behaviors for tracking history.
Examples
Creating a User:
Follow the prompts to add a new user.
Adding a Behavior:
After creating a user, add a behavior to track.
Logging a Behavior:
Log entries over time to observe trends.
Future Enhancements
Implement data visualization to make progress reports more intuitive.
Add a summary report feature for quick insights.
Contributors
Christine Kaeni
License
This project is licensed under the MIT License.





