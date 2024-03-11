# Note Taking Application 1.1

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)

## Introduction

The Note Taking Application is a Flask-based web application that allows users to create, edit, and manage their notes. It provides a simple and intuitive interface for organizing thoughts, tasks, and reminders.

## Features

- **User Authentication:** Secure login system to protect user data.
- **Note Management:** Add, edit, and delete notes with ease.
- **Session Timeout:** Automatic session timeout for enhanced security.
- **Error Handling:** Comprehensive error handling to ensure smooth user experience.
- **Responsive Design:** Mobile-friendly interface for seamless usage on various devices.

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- Flask library installed (`pip install Flask`).

### Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Running the Application

1. Run the Flask application by executing `python app.py` in your terminal.
2. Open a web browser and navigate to http://localhost:5000 to access the application.

## Usage

1. Log in or create an account to access the application.
2. Add new notes, edit existing ones, or delete unwanted notes.
3. Log out to securely end your session.


# Note Taking App v1

Forged with Flask and Python, this user-friendly note-taking application provides a convenient way for users to quickly capture notes and view them in an organized manner.

## Features:

- **User-friendly Interface:** The home route presents a text field and a button for adding notes.
- **Dynamic Note Addition:** Users can add notes by typing in the text field and clicking the button.
- **Real-time Display:** Added notes are instantly displayed as an unordered list below the text field.
- **Persistent Storage:** Notes are stored locally, ensuring they persist even after page refresh.

## Usage:

1. **Adding a Note:**
   - Type your note into the text field provided.
   - Click the "Add Note" button to append your note to the list below.
   
2. **Viewing Notes:**
   - All added notes are displayed as an unordered list below the text field.
   
3. **Editing or Deleting Notes:**
   - Currently, the application supports only adding notes. Editing or deleting functionality can be implemented in future updates.

## Development:

- **Technologies Used:** This application is built using Flask and Python.
- **Project Structure:** 
  - **app.py:** Contains the Flask application setup and route definitions.
  - **templates/:** Contains HTML templates for rendering the user interface.

## Future Improvements:

- **Editing and Deleting Notes:** Implement functionality to edit or delete existing notes.
- **User Authentication:** Add user authentication to allow multiple users to manage their own sets of notes.
- **Customization Options:** Provide options for users to customize the appearance or organization of their notes.

