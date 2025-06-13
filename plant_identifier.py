from graphics import Canvas
import requests
    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BUTTON_WIDTH = 110
BUTTON_HEIGHT = 20
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def main():
    draw_button()
    canvas.clear()
    load_image()
    submit_API()
    canvas.clear()
    return_results()

#User submits a photo by clicking a button and uploading a photo
#Draw button with text
def draw_button():
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2)
    Start_Y = (CANVAS_HEIGHT/2) - (BUTTON_HEIGHT/2)
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE )
    canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2), "UPLOAD A PLANT", anchor = "center")
#Waits for user to click on the button    
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            break
        else:
            canvas.clear()
            draw_button()

def load_image():
    image = "/Users/majid/Downloads/vaccinium-boreale-le-ahaines-a.jpg"
    canvas.create_image_with_size(
    (CANVAS_WIDTH/2 - 200),
    (0),
    400,
    400,
    image
)   
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2)
    Start_Y = CANVAS_HEIGHT*.8
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE )
    canvas.create_text(Start_X+5, (Start_Y+BUTTON_HEIGHT*.25), "CLICK TO SUBMIT")
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
    
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            break
        else:
            canvas.clear()
            load_image()

def submit_api()
#submits user photo to the Plantnet API
    image = "/Users/majid/Downloads/vaccinium-boreale-le-ahaines-a.jpg"
    #my personal API KEy
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"
#The base URL for posting a query to the API for identification
    API_BASE_URL = https://my-api.plantnet.org/v2/identify/all
image = 

def search_articles(search_term):
    params = {
        "q" : search_term,
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params)
    requests.get(API_BASE_URL, params)
        return response.json()

def display_results(search_results)
    docs = search_results["response"]["docs"]

    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]

        print(articl_headline + " (" + article_we_url + ")")

search_term = input("Your search term")
search_results = search_articles(search_term)
display_results(search_results)

"""service: https://my-api.plantnet.org/v2/

image_1: images=/data/media/image_1.jpeg
image_2: images=/data/media/image_2.jpeg
organ_1: organs=flower
organ_2: organs=leaf
"""
def return_results():
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.103), "Your plant is vaccinium-boreale")
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.133), "Here is a link to more information")
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.163), "https://en.wikipedia.org/wiki/Vaccinium_formosum")
    canvas.create_image_with_size((CANVAS_WIDTH/2) - 150, (CANVAS_HEIGHT*.35), 300, 300, 'vaccinium-boreale-le-ahaines-a.jpg'
 )
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2 + 25)
    Start_Y = (CANVAS_HEIGHT/2) - (BUTTON_HEIGHT/2 + 115 )
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH + 50, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE)
    canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2) - 114, "UPLOAD ANOTHER PLANT", anchor = "center")
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            canvas.clear()
            main()
        else:
            canvas.clear()
            return_results()

#prints the plant name, and a link to the wikipedia page for that plant
if __name__ == '__main__':
    main()