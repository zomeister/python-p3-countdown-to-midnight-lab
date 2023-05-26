import time
def countdown(int_sec):
    while int_sec >= 0:
        if int_sec == 0:
            print("HAPPY NEW YEAR!")
            break
        print(f'{int_sec} SECOND(S)!')
        int_sec -= 1
def countdown_with_sleep(int_sec):
    time.sleep(1)
    while int_sec >= 0:
        if int_sec == 0:
            print("HAPPY NEW YEAR!")
            break
        print(f'{int_sec} SECOND(S)!')
        int_sec -= 1