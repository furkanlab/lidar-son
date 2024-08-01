from selenium import webdriver
import time

# Tarayıcıyı başlatın
driver = webdriver.Chrome()  # veya webdriver.Firefox()

try:
    while True:
        # Sayfayı yükle
        driver.get("http://192.168.1.39:9000")

        # 3 saniye bekle
        time.sleep(1)

except KeyboardInterrupt:
    # Programı elle durdurduğunuzda tarayıcıyı kapatın
    print("Bot durduruldu.")

finally:
    driver.quit()