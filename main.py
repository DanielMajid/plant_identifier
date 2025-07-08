from js import FormData, document, FileReader, fetch, Blob
import json
import asyncio

def submit_api(event=None):
    print("submit_api function called")  # Debugging output

    # Get the file input element
    file_input = document.getElementById("my_file")
    files = file_input.files

    # Check if files are selected
    if len(files) == 0:
        output = document.getElementById("output")
        output.innerHTML = "No files selected"
        return

    # Prepare files for API request
    api_files = []
    for file in files:
        # Use FileReader to read the file content
        reader = FileReader.new()

        def onload(event):
            python_file = event.target.result  # File content as a string
            api_files.append((file.name, python_file))

            # If all files are processed, send the API request
            if len(api_files) == len(files):
                # Schedule the async function
                asyncio.create_task(send_api_request(api_files))

        reader.onload = onload
        reader.readAsBinaryString(file)

async def send_api_request(api_files):
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"
    PROJECT = "all"
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    # Prepare the form data
    form_data = FormData.new()
    for filename, content in api_files:
        # Set organs to "auto" for all images
        blob = Blob.new([content])
        form_data.append("organs", "auto")
        form_data.append("images", blob, filename)
        print(f"Appending file: {filename} with organ: auto")

    try:
        # Use fetch to send the API request
        response = await fetch(api_endpoint, {
            "method": "POST",
            "body": form_data
        })

        if not response.ok:
            # Log the response text for debugging
            error_text = await response.text()
            print(f"Response Status: {response.status}")
            print(f"Response Text: {error_text}")
            raise Exception(f"HTTP error: {response.status}")

        json_result = await response.json()

        # Display API response in browser
        output = document.getElementById("output")
        output.innerHTML = f"API Response: {json.dumps(json_result, indent=4)}"
    except Exception as e:
        # Log the error to the output div
        output = document.getElementById("output")
        output.innerHTML = f"Error during API request: {e}"
        print(f"Error: {e}")