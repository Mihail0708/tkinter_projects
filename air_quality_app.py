from tkinter import *
import json
import requests

root = Tk()
root.title('Air Quality')
root.geometry('500x200')


def zip_lookup():
    global my_label
    global info
    global api

    if info:
        my_label.destroy()
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_code.get() + "&distance=10&API_KEY=0E518ABA-0972-4871-BC67-2AEFC4981F8B")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = "#0C0"
        elif category == 'Moderate':
            weather_color = "#FFFF00"
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = "#ff9900"
        elif category == 'Unhealthy':
            weather_color = "#FF0000"
        elif category == 'Very Unhealthy':
            weather_color = "#990066"
        elif category == 'Hazardous':
            weather_color = "#660000"

        root.configure(background=weather_color)
        my_label = Label(root, text=city + ', Air Quality: ' + str(quality) + ', Category: ' + category,
                         font=('Arial', 15), background=weather_color, pady=15)
        my_label.pack()
        info = city

    except Exception:
        api = 'Error...'


info = ''
zip_code = Entry(root)
zip_code.pack(pady=15)

zip_btn = Button(root, text='Enter zipcode', command=zip_lookup)
zip_btn.pack(pady=5)

root.mainloop()
