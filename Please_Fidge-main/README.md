## 1. Introduction  
To reduce food waste and promote various cooking activities by recognizing the contents of the user's refrigerator, recommending possible cooking menus and providing related cooking videos.\

**Expected Benefits**  
- Reduces food waste by efficiently utilizing the remaining ingredients in the refrigerator.
- Helps users easily try different dishes, adding interest and enjoyment to cooking.

---

## 2. Components  
**Raspberry Pi and the Pi Camera**    
Capture the contents of the refrigerator and use object recognition to identify ingredients.  

**Object recognition system**  
Use YOLOv5 to accurately recognize ingredients from images.  

**OpenAI API**   
Recommend possible dishes based on the recognized ingredients.  

**YouTube crawling module**  
Automatically search and fetch YouTube links to cooking videos related to the suggested menu.  

**Telegram notification system**  
Sends menu recommendations and YouTube video links to users in Telegram messages.  

---

## **3. HardWare Setting**

#### Respberry PI 

We utilized Raspberry Pi to power our AI model and create data.  

From the Raspberry homepage, you can save the Raspbian OS to an SD card, boot it, and install the necessary modules.  

#### Camera Module Setting  

You can install the camera module by following the link above.  

**Hardware connection**  

Enable the serial interface: Run sudo raspi-config and select 'Interfacing Options' > 'Serial' to enable hardware serial. 
Write Python code or other code that can send and receive data through the serial port.    


#### Raspberry PI Pico (W5100S-EVB-Pico)  


Pico communicates and receives the data inferred by Raspberry Pi 4, and utilizes Ethernet communication to make menu recommendations using chatGPT.  

Connect Ethernet, power and set up the UART to communicate with the Raspberry 4.  

 

#### Hardware connections  

> Connect GPIO pin 14 (TX) of the Raspberry Pi 4 to the UART RX pin of the Pico.  
> Connect GPIO pin 15 (RX) of the Raspberry Pi 4 to the UART TX pin of the Pico.  
> Connect the GND pins of both boards to each other.


![IMG_5684](https://github.com/jh941213/Please_Fidge/assets/112835087/32ccc049-8ac5-4dee-af10-b46ad5c551d8)

## **4. Software Setting**
  
### YOLOv5  
![splash (1)](https://github.com/jh941213/Please_Fidge/assets/112835087/7c2910a7-38ec-4fe8-bcc9-8b1586c422fd)
**The trained weight file is total.pt and I've written the code in main.py to detect.py and set it up as a webcam.**  

```python
!git clone https://github.com/jh941213/Please_Fidge.git
cd RasberryPI4
!git clone https://github.com/ultralytics/yolov5.git
```
```python
#terminal
python camera.py
```
Open a terminal and run camera.py to detect objects. Once detected, press Ctrl + C to exit the terminal.


### PICO
Configure Thony micropython, plug in an Ethernet connection, and run the file.

### RaspberryPI
After establishing a physical connection with PICO, run main.py on RaspbianOS.  

```python
#terminal
python main.py
```

The code should work fine, so feel free to adapt it to your environment. You just need to make them communicate.  

## **Telegram Setting**
First, sign up for Telegram and add 'BotFather' as a friend. and /newbot to create a bot and receive a token.  
![627693803_1691758738](https://github.com/jh941213/Please_Fidge/assets/112835087/6559f339-4e1b-4483-872b-d5c5712378bd)
![627693803_1691758957](https://github.com/jh941213/Please_Fidge/assets/112835087/3af30342-af90-4eb8-9227-11cb2ac3cf26)

If you see a token like that, your bot has been created. We send the bot a message "hello"
<img width="768" alt="627693803_1691759164" src="https://github.com/jh941213/Please_Fidge/assets/112835087/a69bb6ae-4733-4e7b-bda4-47559d7390b2">
> api.telegram.org/bot{"your_tokens"}/getUpdates

If you go to the webpage above, you'll see a JSON file of the message you sent and your information. From there, you can save your ID and check to see if the message was sent successfully.  

That's it, you're ready for Telegram. Now it's time to implement it in code!  

[Python Telemgram Docs](https://docs.python-telegram-bot.org/en/stable/index.html)  

If you're not sure, check out the link above!🔥  

## **5. Result**
The results of the project. Prepare delicious dishes with ingredients from your fridge!

![1](https://github.com/jh941213/Please_Fidge/assets/112835087/3cfe625e-ef46-4538-bcb1-d52355038684)
![2](https://github.com/jh941213/Please_Fidge/assets/112835087/0028767b-6a96-4c81-abf7-c4a195cbcf5f)
![RPReplay_Final1691731367_MP4_AdobeExpress](https://github.com/jh941213/Please_Fidge/assets/112835087/f1814748-7009-412a-bde9-f2b2b4c5ca88)

