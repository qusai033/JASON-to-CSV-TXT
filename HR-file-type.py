'''''
import json

# Open the JSON file for reading
with open('training-session....json', 'r') as f: #make sure to past the full path. this is only an example
    # Load the JSON data from the file
    data = json.load(f)

# Open a file for writing the output
with open('output.txt', 'w') as out_file:
    # Write some information about the exercise to the file
    out_file.write("Exercise name: " + str(data['name']) + "\n")
    out_file.write("Start time: " + str(data['startTime']) + "\n")
    out_file.write("Stop time: " + str(data['stopTime']) + "\n")
    out_file.write("Duration: " + str(data['duration']) + "\n")
    out_file.write("Calories burned: " + str(data['kiloCalories']) + "\n\n")

    # Write the heart rate samples to the file
    out_file.write("Heart rate samples:\n")
    for sample in data['exercises'][0]['samples']['heartRate']:
        out_file.write(str(sample['dateTime']) + "," + str(sample['value']) + "\n")
'''

import json
import csv

# Open the JSON file for reading
with open('training-session....json', 'r') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Extract the required information from the JSON object
name = data['name']
start_time = data['startTime']
stop_time = data['stopTime']
duration = data['duration']
calories_burned = data['kiloCalories']

heart_rate_samples = data['exercises'][0]['samples']['heartRate']
heart_rate_values = [str(sample['value']) for sample in heart_rate_samples]
heart_rate_datetimes = [str(sample['dateTime']) for sample in heart_rate_samples]

# Write the data to a CSV file
with open('data.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Start Time', 'Stop Time', 'Duration', 'Calories Burned', 'Heart Rate Values', 'Heart Rate Datetimes'])
    writer.writerow([name, start_time, stop_time, duration, calories_burned, heart_rate_values, heart_rate_datetimes])
