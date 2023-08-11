import camera

import os

import serial
import requests
import time
import yt_dlp as youtube_dl 
import telegram


def collect_classes_from_files(directory_path):

    classes_list = []

    for filename in os.listdir(directory_path):

        if filename.endswith(".txt"):

            with open(os.path.join(directory_path, filename), 'r') as file:

                lines = file.readlines()

                for line in lines:

                    class_id = int(line.split()[0])

                    classes_list.append(class_id)

    return classes_list



class_number_to_english = {

    0: 'Chicken',

    1: 'Corn',

    2: 'Egg',

    3: 'Enoki Mushroom',

    4: 'Garlic',

    5: 'Green Onion',

    6: 'Bell Pepper',

    7: 'Kimchi',

    8: 'Minced Garlic',

    9: 'Mushroom',

    10: 'Onion',

    11: 'Pork',

    12: 'Potato',

    13: 'Radish',

    14: 'Red Chili Pepper',

    15: 'Soybean Paste',

    16: 'Spam',

    17: 'Pumpkin',

    18: 'Tofu',

    19: 'Tomato',

    20: 'Tuna'
}


def send_telegram_message(chat_id, text):
    bot_token = "6555412120:AAF0UpkBofcs5cMffaSCy-xK1e8FvmuBYQM"
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}'
    
    response = requests.get(send_text)

    return response.json()

def convert_to_korean(class_numbers):

    return [class_number_to_english.get(class_num, class_num) for class_num in class_numbers]

def fetch_youtube_link(query):
    ydl_opts = {
        'default_search': 'ytsearch',
        'quiet': True,
        'format': 'bestaudio/best',
        'noplaylist': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
    
    # 여기에서 video['id']를 사용하여 표준 YouTube 링크를 생성합니다.
    video_url = f"https://www.youtube.com/watch?v={video['id']}"
    return video_url, video['title']


if __name__ == "__main__":

    directory = "/home/pi/yolov5ss/result/exp/labels"

    collected_classes = collect_classes_from_files(directory)

    unique_classes = list(set(collected_classes))

    korean_names = convert_to_korean(unique_classes)

    

    # Convert korean_names list to string

    data_string = ",".join(korean_names)

    

    # Serial communication setup

    ser = serial.Serial('/dev/serial0', 9600, timeout=1)

    ser.flush()

    

    # Send the data to Pico via UART

    ser.write(data_string.encode())
    
    time.sleep(20)
    if ser.in_waiting >0:
        received_data = ser.readline().decode().strip()
        received_data = received_data+"recipe"
        print(f"Received from Pico : {received_data}")
        

    url, title = fetch_youtube_link(received_data)
    
    message_text = f"{title}\n{url}"
    send_telegram_message("5795970252", message_text)
    #telegram
  
    # Optional: Close the serial connection

    #ser.close()
