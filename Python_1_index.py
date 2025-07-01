import filedialog
import pprint
from pprint import pprint
import requests
import json
from js import document

    



def find_file():
    file_path = filedialog.askopenfilename()
    return file_path
    # need to pass this result to the submit_api function >>print(file_path)
            
def load_photo(file_path):

def submit_api(file_path):
    #submits user photo to the Plantnet API
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"	# Your API_KEY here
    PROJECT = "all"; # try specific floras: "weurope", "canada"…
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    image_path_1 = "/Users/majid/Downloads/vaccinium-boreale-le-ahaines-a.jpg"
    image_data_1 = open(image_path_1, 'rb')

    #image_path_2 = "../data/image_2.jpeg"
    #image_data_2 = open(image_path_2, 'rb')

    data = { 'organs': ['flower', 'leaf'] }

    files = [
    ('images', (image_path_1, image_data_1)),
    #('images', (image_path_2, image_data_2))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    pprint(response.status_code)
    pprint(json_result)
       

if __name__ == '__main__':
    main()