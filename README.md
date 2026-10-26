# ✈️ Travel Planner – Python Mini Project

## 📌 Project Overview

The **Travel Planner** is a Python-based mini project designed to help users plan their trips, explore destinations, estimate travel expenses, and manage their travel plans through a simple Graphical User Interface (GUI).

This project demonstrates the practical implementation of four fundamental Python concepts: **Dictionaries, Functions, File Handling, and GUI Development using Tkinter**.

Users can select a destination, enter the number of travellers and travel days, calculate the estimated trip budget, view recommended tourist attractions, and save or delete their travel plans.

## 🎯 Objectives

- Develop a simple and user-friendly travel planning application.
- Apply Python dictionaries to store destination information.
- Use functions to organize and simplify the program.
- Implement file handling to store and retrieve travel plans.
- Create a graphical interface using Tkinter.
- Calculate estimated travel expenses based on the destination, duration, and number of travellers.

## ✨ Features

- **Destination Selection:** Choose from predefined destinations, including Goa, Manali, Jaipur, Mumbai, Kerala, and Delhi.
- **Budget Calculation:** Calculate the estimated travel expenses based on the selected destination, trip duration, and number of travellers.
- **Destination Information:** View recommended tourist attractions and estimated expenses.
- **Save Travel Plans:** Store travel plans in a JSON file.
- **View Saved Trips:** Display saved travel plans in a table.
- **Delete Travel Plans:** Remove previously saved trips.
- **Input Validation:** Handle invalid inputs and missing information.
- **User-Friendly GUI:** Interact with the application through buttons, input fields, and tables.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Dictionaries | Store destination and travel information |
| Functions | Organize program operations |
| File Handling | Read and write travel plan data |
| JSON | Store travel plans in a structured format |
| Tkinter | Develop the graphical user interface |
| Treeview | Display saved travel plans in a table |

## 📚 Python Concepts Implemented

### 1. Dictionaries
Dictionaries store destination details such as transportation costs, hotel expenses, food costs, activity expenses, and recommended tourist attractions.

### 2. Functions
Functions are used to calculate budgets, create travel plans, save and retrieve data, display destination details, delete trips, and clear input fields.

### 3. File Handling
The application uses Python's file handling capabilities to save and retrieve travel plans from `travel_plans.json`. Saved data remains available when the application is restarted, provided the file is retained.

### 4. GUI Development
Tkinter is used to create the graphical interface. The application includes labels, text fields, a destination dropdown, buttons, message boxes, and a table for displaying saved travel plans.

## 💰 Budget Calculation

The application estimates the travel budget using the following formula:

**Total Budget = Number of Travellers × [Transport Cost + Number of Days × (Hotel Cost per Day + Food Cost per Day + Activity Cost per Day)]**

The budget is calculated using predefined sample costs for each destination.

**Note:** The displayed costs are estimates for demonstration purposes and are not live travel prices.

## 📂 Project Structure

```text
Travel_Planner/
│
├── travel_planner.py
├── travel_plans.json
└── README.md
```

- `travel_planner.py` – Contains the main Python program and GUI.
- `travel_plans.json` – Stores saved travel plans and is created automatically when the first plan is saved.
- `README.md` – Provides project documentation and setup instructions.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your computer.
- Tkinter available in your Python installation.
- A Python editor such as IDLE, Visual Studio Code, or PyCharm.

### Step 1: Download or Clone the Project

If the project is hosted on GitHub, clone the repository:

```bash
git clone <your-repository-url>
```

Alternatively, download the project files and extract them into a folder.

### Step 2: Open the Project Folder

Open the folder containing `travel_planner.py` in your preferred Python editor.

### Step 3: Run the Application

Open a terminal in the project folder and execute:

```bash
python travel_planner.py
```

On some Windows systems, use:

```bash
py travel_planner.py
```

### Step 4: Start Planning Your Trip

Once the application opens:

1. Enter your name.
2. Select a destination from the dropdown menu.
3. Enter the number of travel days.
4. Enter the number of travellers.
5. Click **Create Travel Plan**.
6. View the estimated budget and recommended tourist attractions.
7. Find your saved trip in the travel plans
