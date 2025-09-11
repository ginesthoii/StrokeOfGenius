import pandas as pd
import os
from datetime import datetime

# Filename for the logbook
LOG_FILE = 'swimming_log.csv'

def initialize_log():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=[
            'Date', 'Location', 'Total_Distance(m)', 'Duration(min)',
            'Workout_Type', 'Stroke', 'Notes'
        ])
        df.to_csv(LOG_FILE, index=False)
        print(f"Created new logbook file: {LOG_FILE}")

def add_entry():
    """Prompt the user for workout details and add a new row to the logbook."""
    print("\n--- Add a New Swimming Entry ---")
    date = input(f"Date (YYYY-MM-DD, default: {datetime.now().strftime('%Y-%m-%d')}): ") or datetime.now().strftime('%Y-%m-%d')
    location = input("Location: ")
    try:
        distance = int(input("Total Distance (meters): "))
        duration = int(input("Duration (minutes): "))
    except ValueError:
        print("Invalid input for distance or duration. Please enter a number.")
        return
    workout_type = input("Workout Type (e.g., Endurance, Sprint): ")
    stroke = input("Main Stroke (e.g., Freestyle, Mix): ")
    notes = input("Notes: ")

    # Create a new DataFrame row
    new_entry = pd.DataFrame([{
        'Date': date,
        'Location': location,
        'Total_Distance(m)': distance,
        'Duration(min)': duration,
        'Workout_Type': workout_type,
        'Stroke': stroke,
        'Notes': notes
    }])

    # Append the new entry to the CSV
    new_entry.to_csv(LOG_FILE, mode='a', header=False, index=False)
    print("Entry added successfully!")

def view_stats():
    """Calculate and display basic statistics from the logbook."""
    if not os.path.exists(LOG_FILE):
        print("No logbook found. Please add an entry first.")
        return

    df = pd.read_csv(LOG_FILE)

    if df.empty:
        print("Logbook is empty. No stats to display.")
        return

    total_swims = len(df)
    total_distance = df['Total_Distance(m)'].sum()
    avg_distance = df['Total_Distance(m)'].mean()
    total_time = df['Duration(min)'].sum()
    avg_time = df['Duration(min)'].mean()

    print("\n--- Swimming Statistics ---")
    print(f"Total swims logged: {total_swims}")
    print(f"Total distance swum: {total_distance} meters")
    print(f"Average distance per swim: {avg_distance:.2f} meters")
    print(f"Total time spent swimming: {total_time} minutes")
    print(f"Average time per swim: {avg_time:.2f} minutes")

    # You can add more analysis, like favorite stroke or location
    print("\nMost frequent stroke:", df['Stroke'].mode()[0])
    print("Most frequent location:", df['Location'].mode()[0])

def main():
    initialize_log()

    while True:
        print("\n--- Swimming Log Manager ---")
        print("1. Add a new swimming entry")
        print("2. View basic statistics")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_stats()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()