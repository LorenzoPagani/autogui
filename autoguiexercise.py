import pyautogui
import time

def keep_active():
    start_time = time.time()
    counter = 0
    print(f"script started at: {time.ctime(start_time)}")
    try:
        while True:
            pyautogui.press('shift')
            print("Shift pressed")
            counter += 1
            time.sleep(200) 
    except KeyboardInterrupt:
        end_time = time.time()
        print(f"script ended at: {time.ctime(end_time)}")
        elapsed_time = end_time - start_time
        elapsed_hours = elapsed_time / 3600
        elapsed_minutes = elapsed_time / 60
        hours = int(elapsed_hours)
        minutes = int(elapsed_minutes)  
        seconds = (elapsed_minutes - minutes) * 60 
        print(f"Elapsed time:{hours} hours, {minutes} minutes and {seconds:.0f} seconds")
        print(f"shift key pressed {counter} times. great job!")


  



if __name__ == "__main__":
    keep_active()
