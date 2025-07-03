from js import document
from pyodide import to_js
import requests
import json

def main():
    submit_api()

def submit_api():
    #get the file input element
    file_input = document.getElementById("my_file")
    files = file_input.files

    #check if files are selected
    if len(files) == 0:
        output = document.getElementById("output")
        output.innerHTML = "No files selected"
        return
    
    #Prepare files for API request
    api_files = []
    for file in files:
        python_file = to_js(file)
        api_files.append(('images', (file.name, file)))
        output = document.getElementById("output")

    #Prepare API request
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"	# Your API_KEY here
    PROJECT = "all"; # try specific floras: "weurope", "canada"…
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
    data = { 'organs': ['flower', 'leaf'] }

    #files = [
    #('images', (file.name, file)),
    #('images', (image_path_2, image_data_2))
    #]

    try:
        #Send API request
        response = requests.post(api_endpoint, files=api_files, data=data)
        #Raise an error for HTTP issues
        response.raise_for_status()
        json_result = response.json()

        #Display API response in browser
        output = document.getElementById("output")
        output.innerHTML = f"API Response: {json.dumps(json_result, indent=4)}"
    except requests.RequestException as e:
        output = document.getElementById("output")
        output.innerHTML = f"Error during API request: {e}"
    except json.JSONDecodeError:
        output = document.getElementById("output")
        output.innerHTML = "Error decoding API response."
    #req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    #prepared = req.prepare()

    #s = requests.Session()
    #response = s.send(prepared)
    #json_result = json.loads(response.text)

    #pprint(response.status_code)
    #pprint(json_result)
       

if __name__ == '__main__':
    main()