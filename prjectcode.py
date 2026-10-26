#python
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# ==========================================
# TRAVEL PLANNER MINI PROJECT
# Concepts: Dictionaries, Functions,
# File Handling and GUI
# ==========================================

FILE_NAME = "travel_plans.json"

# Dictionary containing destination information
destinations = {
    "Goa": {
        "transport": 2000,
        "hotel": 1500,
        "food": 700,
        "activities": 500,
        "places": "Baga Beach, Fort Aguada, Calangute Beach"
    },

    "Manali": {
        "transport": 3000,
        "hotel": 1800,
        "food": 800,
        "activities": 1000,
        "places": "Solang Valley, Rohtang Pass, Hadimba Temple"
    },

    "Jaipur": {
        "transport": 1500,
        "hotel": 1200,
        "food": 600,
        "activities": 400,
        "places": "Hawa Mahal, Amber Fort, City Palace"
    },

    "Mumbai": {
        "transport": 1000,
        "hotel": 2000,
        "food": 800,
        "activities": 700,
        "places": "Gateway of India, Marine Drive, Juhu Beach"
    },

    "Kerala": {
        "transport": 2500,
        "hotel": 1700,
        "food": 700,
        "activities": 800,
        "places": "Munnar, Alleppey, Kovalam Beach"
    },

    "Delhi": {
        "transport": 1200,
        "hotel": 1600,
        "food": 700,
        "activities": 500,
        "places": "India Gate, Red Fort, Qutub Minar"
    }
}


# ==========================================
# FILE HANDLING FUNCTIONS
# ==========================================

def load_trips():
    """Load saved travel plans from a JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        messagebox.showerror(
            "File Error",
            "Could not read the travel plans file."
        )
        return []


def save_trips(trips):
    """Save all travel plans to a JSON file."""

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(trips, file, indent=4)

        return True

    except OSError as error:
        messagebox.showerror(
            "File Error",
            f"Could not save travel plans:\n{error}"
        )
        return False


# ==========================================
# TRAVEL PLANNING FUNCTIONS
# ==========================================

def calculate_budget(destination, travellers, days):
    """Calculate the estimated total trip cost."""

    details = destinations[destination]

    cost_per_person = (
        details["transport"]
        + days * (
            details["hotel"]
            + details["food"]
            + details["activities"]
        )
    )

    total_cost = cost_per_person * travellers

    return total_cost


def create_trip():
    """Collect user input and create a travel plan."""

    name = name_entry.get().strip()
    destination = destination_box.get()
    days_text = days_entry.get().strip()
    travellers_text = travellers_entry.get().strip()

    # Validate user input
    if not name:
        messagebox.showwarning(
            "Missing Information",
            "Please enter your name."
        )
        return

    if destination not in destinations:
        messagebox.showwarning(
            "Missing Information",
            "Please select a destination."
        )
        return

    try:
        days = int(days_text)
        travellers = int(travellers_text)

        if days <= 0 or travellers <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Days and travellers must be positive integers."
        )
        return

    # Calculate estimated budget
    budget = calculate_budget(destination, travellers, days)

    # Store trip details in a dictionary
    trip = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "name": name,
        "destination": destination,
        "days": days,
        "travellers": travellers,
        "budget": budget,
        "places": destinations[destination]["places"]
    }

    # Load existing trips and add the new trip
    trips = load_trips()
    trips.append(trip)

    if not save_trips(trips):
        return

    refresh_trips()

    # Display trip summary
    summary = (
        f"TRAVEL PLAN CREATED SUCCESSFULLY!\n\n"
        f"Name: {name}\n"
        f"Destination: {destination}\n"
        f"Duration: {days} days\n"
        f"Travellers: {travellers}\n\n"
        f"Estimated Budget: Rs. {budget:,}\n\n"
        f"Recommended Places:\n"
        f"{trip['places']}\n\n"
        f"Your travel plan has been saved."
    )

    messagebox.showinfo("Travel Plan Summary", summary)


def refresh_trips():
    """Display saved travel plans in the table."""

    for item in trip_table.get_children():
        trip_table.delete(item)

    trips = load_trips()

    for trip in trips:
        trip_table.insert(
            "",
            "end",
            iid=trip["id"],
            values=(
                trip["name"],
                trip["destination"],
                trip["days"],
                trip["travellers"],
                f"Rs. {trip['budget']:,}"
            )
        )


def delete_trip():
    """Delete the selected travel plan."""

    selected = trip_table.selection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a travel plan to delete."
        )
        return

    trip_id = selected[0]

    confirm = messagebox.askyesno(
        "Confirm Deletion",
        "Are you sure you want to delete this travel plan?"
    )

    if not confirm:
        return

    trips = load_trips()

    updated_trips = [
        trip for trip in trips
        if trip["id"] != trip_id
    ]

    if save_trips(updated_trips):
        refresh_trips()

        messagebox.showinfo(
            "Success",
            "Travel plan deleted successfully."
        )


def show_destination_details():
    """Display details of the selected destination."""

    destination = destination_box.get()

    if destination not in destinations:
        messagebox.showwarning(
            "Select Destination",
            "Please select a destination first."
        )
        return

    details = destinations[destination]

    information = (
        f"DESTINATION: {destination}\n\n"
        f"Recommended Places:\n{details['places']}\n\n"
        f"Estimated Cost Per Person:\n\n"
        f"Transport: Rs. {details['transport']:,}\n"
        f"Hotel per day: Rs. {details['hotel']:,}\n"
        f"Food per day: Rs. {details['food']:,}\n"
        f"Activities per day: Rs. {details['activities']:,}\n\n"
        f"Note: These are sample estimates."
    )

    messagebox.showinfo("Destination Details", information)


def clear_fields():
    """Clear all input fields."""

    name_entry.delete(0, tk.END)
    destination_box.set("")
    days_entry.delete(0, tk.END)
    travellers_entry.delete(0, tk.END)


# ==========================================
# GUI DESIGN USING TKINTER
# ==========================================

root = tk.Tk()

root.title("Travel Planner - Python Mini Project")
root.geometry("1000x700")
root.minsize(850, 600)

# Main heading
title_label = tk.Label(
    root,
    text="TRAVEL PLANNER",
    font=("Arial", 24, "bold"),
    fg="#154360"
)

title_label.pack(pady=(15, 5))

subtitle_label = tk.Label(
    root,
    text="Plan your journey, explore destinations and manage your budget!",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 15))


# ==========================================
# INPUT FORM
# ==========================================

form_frame = ttk.LabelFrame(
    root,
    text="Create Your Travel Plan",
    padding=15
)

form_frame.pack(fill="x", padx=20, pady=5)

# Name
ttk.Label(
    form_frame,
    text="Your Name:"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

name_entry = ttk.Entry(form_frame, width=28)
name_entry.grid(row=0, column=1, padx=10, pady=8)


# Destination
ttk.Label(
    form_frame,
    text="Destination:"
).grid(row=0, column=2, padx=10, pady=8, sticky="w")

destination_box = ttk.Combobox(
    form_frame,
    values=list(destinations.keys()),
    state="readonly",
    width=25
)

destination_box.grid(row=0, column=3, padx=10, pady=8)


# Number of days
ttk.Label(
    form_frame,
    text="Number of Days:"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

days_entry = ttk.Entry(form_frame, width=28)
days_entry.grid(row=1, column=1, padx=10, pady=8)


# Number of travellers
ttk.Label(
    form_frame,
    text="Number of Travellers:"
).grid(row=1, column=2, padx=10, pady=8, sticky="w")

travellers_entry = ttk.Entry(form_frame, width=28)
travellers_entry.grid(row=1, column=3, padx=10, pady=8)


# ==========================================
# BUTTONS
# ==========================================

button_frame = ttk.Frame(root)
button_frame.pack(pady=12)

ttk.Button(
    button_frame,
    text="Create Travel Plan",
    command=create_trip
).grid(row=0, column=0, padx=6)

ttk.Button(
    button_frame,
    text="Destination Details",
    command=show_destination_details
).grid(row=0, column=1, padx=6)

ttk.Button(
    button_frame,
    text="Clear Fields",
    command=clear_fields
).grid(row=0, column=2, padx=6)

ttk.Button(
    button_frame,
    text="Delete Selected Trip",
    command=delete_trip
).grid(row=0, column=3, padx=6)


# ==========================================
# SAVED TRIPS TABLE
# ==========================================

table_frame = ttk.LabelFrame(
    root,
    text="Your Saved Travel Plans",
    padding=10
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

columns = (
    "Name",
    "Destination",
    "Days",
    "Travellers",
    "Budget"
)

trip_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=10
)

trip_table.heading("Name", text="Name")
trip_table.heading("Destination", text="Destination")
trip_table.heading("Days", text="Days")
trip_table.heading("Travellers", text="Travellers")
trip_table.heading("Budget", text="Estimated Budget")

trip_table.column("Name", width=170, anchor="center")
trip_table.column("Destination", width=150, anchor="center")
trip_table.column("Days", width=90, anchor="center")
trip_table.column("Travellers", width=110, anchor="center")
trip_table.column("Budget", width=180, anchor="center")

# Add vertical scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=trip_table.yview
)

trip_table.configure(yscrollcommand=scrollbar.set)

trip_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# Footer
footer_label = ttk.Label(
    root,
    text="Python Mini Project | Dictionaries | Functions | File Handling | Tkinter",
    font=("Arial", 9)
)

footer_label.pack(pady=8)


# Load saved trips when the application starts
refresh_trips()

# Start the GUI event loop
root.mainloop()
