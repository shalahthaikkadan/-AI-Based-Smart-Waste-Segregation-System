import os
from ultralytics import YOLO
import cv2
from picamera2 import Picamera2
from gtts import gTTS
import RPi.GPIO as GPIO
import time
import telepot

TRIG = 17
ECHO = 18
servo_pin = 22

buzz = 20

IR_ORGANIC = 23
IR_INORGANIC = 24

step_pin = 2
dir_pin = 3
steps_per_revolution = 200


steps_90 = int(90 * steps_per_revolution / 360)
steps_180 = int(180 * steps_per_revolution / 360)
steps_270 = int(270 * steps_per_revolution / 360)
steps_360 = steps_per_revolution

from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', '')
chat_id = int(os.environ.get('TELEGRAM_CHAT_ID', '0'))
bot = telepot.Bot(bot_token)
command = 0

picam = Picamera2()
picam.preview_configuration.main.size = (480, 480)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.main.align()
picam.configure("preview")
picam.start()

model_path = os.path.join('/home/pi/WASTE_SORTER', 'runs', 'detect', 'train', 'weights', 'best.pt')
model = YOLO(model_path)
threshold = 0.5

global organic_alert_sent
global inorganic_alert_sent

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buzz, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(IR_ORGANIC, GPIO.IN)
GPIO.setup(IR_INORGANIC, GPIO.IN)

#GPIO.output(dir_pin, GPIO.HIGH)
 
def rotate_steps(steps, direction):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.01)

def detect():
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(0)
    
    start_time = time.time()
    while time.time() - start_time < 5:
        frame = picam.capture_array()
        cv2.imshow('Live Detection', frame)
        cv2.waitKey(1)
        
    cv2.imwrite("captured_image.jpg", frame)
    cv2.destroyAllWindows()
    
    frame = cv2.imread("captured_image.jpg")
    results = model(frame)[0]

    detected_objects = 0
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            detected_objects += 1
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            res = results.names[int(class_id)]

    if detected_objects > 0:
        count_text = f"{res} detected."
        print(count_text)
        tts = gTTS(text=count_text, lang='en', slow=False)
        tts.save('count.mp3')
        os.system('mpg321 count.mp3')
        
        if res=="paper"or res=="apple" or res=="orange" or res=="watermelon" or res=="banana":
            print("Organic")
            pwm.ChangeDutyCycle(12.5)
            time.sleep(1)
            pwm.ChangeDutyCycle(2.5)
            time.sleep(1)
            pwm.stop()
        elif res=="bottle" or res=="pen" or res=="coin" or res=="spoon":
            print("In-Organic")
            rotate_steps(steps_180, GPIO.HIGH)
            time.sleep(1)
            pwm.ChangeDutyCycle(12.5)
            time.sleep(1)
            pwm.ChangeDutyCycle(2.5)
            time.sleep(1)
            pwm.stop()
            time.sleep(1)
            rotate_steps(steps_180, GPIO.LOW)

    cv2.imwrite("annotated_image.jpg", frame)

def main():
    global bot
    global chat_id
    bot.message_loop(handle)
    print('Start')
    bot.sendMessage(chat_id, 'WELCOME')
    while True:
        if GPIO.input(IR_ORGANIC) == 0 and organic_alert_sent == False:
            print("Organic tank full")
            bot.sendMessage(chat_id, 'Organic tank full')
            organic_alert_sent = True

        elif GPIO.input(IR_ORGANIC) == 1:
            organic_alert_sent = False


        if GPIO.input(IR_INORGANIC) == 0 and inorganic_alert_sent == False:
            print("Inorganic tank full")
            bot.sendMessage(chat_id, 'Inorganic tank full')
            inorganic_alert_sent = True

        elif GPIO.input(IR_INORGANIC) == 1:
            inorganic_alert_sent = False

        
        GPIO.output(TRIG, False)
        time.sleep(0.00001)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        pulse_start = time.time()
        pulse_end = time.time()
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print(distance)
        time.sleep(0.2)
        if distance <= 9:
            GPIO.output(buzz,True)
            time.sleep(1)
            GPIO.output(buzz,False)
            time.sleep(1)
            detect()

def handle(msg):
    global chat_id
    global command
    global bot
    chat_id = msg['chat']['id']
    command = msg['text']
    print(chat_id)
    print(command)

if __name__ == "__main__":
    main()
