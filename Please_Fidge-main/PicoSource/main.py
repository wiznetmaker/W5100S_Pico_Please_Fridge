from machine import Pin, SPI, UART
import network
import utime
import urequests
import json
import re

# ChatGPT Configuration
api_key = "your_api_token"
chatgpt_url = "https://api.openai.com/v1/chat/completions"
chatgpt_ver= "gpt-3.5-turbo"

def send_prompt_to_chatGPT(prompt):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": f"{chatgpt_ver}",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = urequests.post(chatgpt_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = json.loads(response.text)
        body = response_data["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API error ({response.status_code}): {response.text}")
        
    return body

def extract_starred_section(response):
    match = re.search(r'\*([^*]+)\*', response)
    return match.group(1) if match else None

# W5x00 init
def init_ethernet(timeout=10):
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))   # spi, cs, reset pin
    # DHCP
    nic.active(True)
    start_time = utime.ticks_ms()
    while not nic.isconnected():
        utime.sleep(1)
        if utime.ticks_ms() - start_time > timeout * 1000:
            raise Exception("Ethernet connection timed out.")
        print('Connecting ethernet...')
    print(f'Ethernet connected. IP: {nic.ifconfig()}')

def main():
    init_ethernet()
    uart = UART(0, 9600)
    
    while True:
        if uart.any():
            data = uart.readline().decode("utf-8").strip()  # Read data and decode to string
            prompt = f"{data} Can you recommend a menu I can make with the above ingredients Add a * before and after the suggested menu korean name(No need to add an English name description,Print only the first category)? "
            print(prompt)
            response = send_prompt_to_chatGPT(prompt)
            print(f"Received from UART: {data}")
            print(f"ChatGPT Response: {response}")
            
            
            starred_section = extract_starred_section(response)
            if starred_section:
                uart.write(starred_section.encode("utf-8")) 
                print(f"Sent to Raspberry Pi 4: {starred_section}")

                
        utime.sleep(0.1)


if __name__ == "__main__":
    main()
