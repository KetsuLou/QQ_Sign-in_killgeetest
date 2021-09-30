import time

def waitalert(driver, timeout, poll_frequency):
    endtime = time.time() + timeout
    while True:
        try: alert = driver.switch_to_alert(); return alert
        except: pass
        time.sleep(poll_frequency)
        if time.time() > endtime: raise
        
if __name__ == "__main__":
    waitalert('', 3, 0.1)
    