import RPi.GPIO as GPIO
import time

PIN = 16
LED = 17

def main():
    # GPIO 설정
    GPIO.setmode(GPIO.BCM)  # 핀 번호는 BCM 모드를 사용
    GPIO.setup(PIN, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)

    try:
        for i in range(50):
            touch = GPIO.input(PIN)
            if touch == GPIO.HIGH:  # 1이면 누름 상태
                print("Pressed")
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)  # 1초 대기
                GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)  # 0.1초 대기

    except KeyboardInterrupt:
        print("종료합니다.")
    finally:
        GPIO.cleanup()  # 사용한 핀 정리

if __name__ == "__main__":
    main()
