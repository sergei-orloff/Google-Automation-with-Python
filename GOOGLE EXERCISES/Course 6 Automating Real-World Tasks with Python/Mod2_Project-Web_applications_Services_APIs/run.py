#!/usr/bin/env python3
import os
import requests
import json


def read_feedback_file(file_path):
    """Read a feedback file and return a dictionary with the content."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove any trailing newlines and whitespace
        lines = [line.strip() for line in lines]

        return {
            "title": lines[0],
            "name": lines[1],
            "date": lines[2],
            "feedback": lines[3]
        }


def upload_feedback(feedback_dict):
    """Upload feedback dictionary to the web server."""
    url = "http://35.202.8.234/feedback/"  # Added trailing slash

    # Set proper headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        # Convert dictionary to JSON string
        json_data = json.dumps(feedback_dict)

        # Make the POST request
        response = requests.post(url, data=json_data, headers=headers)

        # Print detailed debug information
        print(f"\nUploading: {feedback_dict['title']}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")

        if response.status_code in [201, 200]:  # Accept both 201 and 200 as success
            print(f"Successfully uploaded feedback: {feedback_dict['title']}")
            return True
        else:
            print(f"Failed to upload feedback: {feedback_dict['title']}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        return False


def main():
    # Directory containing feedback files
    feedback_dir = "/data/feedback"

    # Get a list of all .txt files in the feedback directory
    try:
        feedback_files = [
            os.path.join(feedback_dir, f)
            for f in os.listdir(feedback_dir)
            if f.endswith('.txt')
        ]
    except Exception as e:
        print(f"Error accessing directory {feedback_dir}: {str(e)}")
        return

    if not feedback_files:
        print(f"No .txt files found in {feedback_dir}")
        return

    # Process each feedback file
    successful_uploads = 0
    total_files = len(feedback_files)

    print(f"Found {total_files} feedback files to process...")

    for file_path in feedback_files:
        try:
            print(f"\nProcessing file: {os.path.basename(file_path)}")

            # Read the feedback file into a dictionary
            feedback_dict = read_feedback_file(file_path)

            # Print the dictionary content for debugging
            print("Feedback content:")
            for key, value in feedback_dict.items():
                print(f"{key}: {value}")

            # Upload the feedback
            if upload_feedback(feedback_dict):
                successful_uploads += 1

        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    # Print summary
    print(f"\nUpload Summary:")
    print(f"Total files processed: {total_files}")
    print(f"Successful uploads: {successful_uploads}")
    print(f"Failed uploads: {total_files - successful_uploads}")


if __name__ == "__main__":
    main()
