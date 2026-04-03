#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Attendees must be a list of dictionaries")
        return
    if template.strip() == "":
        raise ValueError("Template cannot be empty")
        return
    
    if len(attendees) == 0:
        raise ValueError("Attendees list cannot be empty")
        return
    
    fields = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        output_text = template
        
        for field in fields:
            value = attendee.get(field)

            if value is None:
                value = "N/A"

            output_text = output_text.replace(f"{{{field}}}", str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output_text)
        except Exception as e:
            print(f"Error occurred while writing to {filename}: {e}")
