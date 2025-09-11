import csv
import os
from datetime import datetime

# The name of the CSV file where logs will be stored
FILENAME = 'swimming_log.csv'

# Define the headers for the CSV file
HEADERS = ['Date', 'Duration (minutes)', 'Total Distance (meters)', 'Workout Details', 'Notes']

def initialize_logbook():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def add_log_entry():
    """Prompt the user for workout details and add a new entry."""
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    try:
        duration = float(input("Enter duration in minutes: "))
        distance = float(input("Enter total distance in meters: "))
        workout_details = input("Enter workout details (e.g., 5x100m freestyle, 4x50m kick): ")
        notes = input("Enter any notes for the session: ")

        with open(FILENAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, duration, distance, workout_details, notes])
        print("Log entry added successfully!")

    except ValueError:
        print("Invalid input. Please enter a number for duration and distance.")

def view_logbook():
    """Print all entries from the logbook."""
    if not os.path.exists(FILENAME):
        print("No logbook found. Add an entry first.")
        return

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))

def get_summary_stats():
    """Calculate and display basic summary statistics."""
    if not os.path.exists(FILENAME):
        print("No logbook found. Add an entry first.")
        return

    total_distance = 0
    total_duration = 0
    workout_count = 0

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)
        
        for row in reader:
            try:
                total_duration += float(row[1])
                total_distance += float(row[2])
                workout_count += 1
            except (ValueError, IndexError):
                # Handle potential malformed rows gracefully
                continue

    if workout_count == 0:
        print("No workouts logged yet.")
        return

    print("\n--- Swimming Summary ---")
    print(f"Total workouts logged: {workout_count}")
    print(f"Total distance swum: {total_distance:.2f} meters")
    print(f"Total time spent swimming: {total_duration:.2f} minutes")
    
    avg_distance_per_workout = total_distance / workout_count
    avg_duration_per_workout = total_duration / workout_count
    avg_speed_m_per_min = (total_distance / total_duration) if total_duration > 0 else 0

    print(f"Average distance per workout: {avg_distance_per_workout:.2f} meters")
    print(f"Average duration per workout: {avg_duration_per_workout:.2f} minutes")
    print(f"Average speed: {avg_speed_m_per_min:.2f} meters per minute")
    print("------------------------\n")

def main():
    """Main function to run the logbook application."""
    initialize_logbook()
    while True:
        print("\nSwimming Logbook Menu:")
        print("1. Add a new log entry")
        print("2. View all logs")
        print("3. Get summary statistics")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_log_entry()
        elif choice == '2':
            view_logbook()
        elif choice == '3':
            get_summary_stats()
        elif choice == '4':
            print("Exiting. Happy swimming!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
