import psutil
import time

def close_open_calc():
    calculator_count = 0
    for proc in psutil.process_iter():
        try:
            if "Calculadora" in proc.name():
                calculator_count += 1
                if calculator_count > 3:
                    proc.terminate()
        except psutil.NoSuchProcess:
            pass

while True:
    close_open_calc()
    time.sleep(1)
