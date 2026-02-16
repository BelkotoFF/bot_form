import requests

def send_form():
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScXqDwCbQCElrXOWXjbRt9nBXPswlC8J3-gxE6WTQ2p7c6gtQ/formResponse'

    # Пробуємо відправити ВСІ поля, щоб виключити помилку "Обов'язкове поле порожнє"
    data = {
        'entry.404296076': 'Білецький Костянтин Олександрович',
        'entry.471758851': '44',
        'entry.630045100': 'Чоловіча',
        'entry.1837420053': '5',
        'entry.1999428519': '5',
        'entry.900161138': '5',
        'entry.653386262': '5',
        'entry.1630851971': '5',
        'entry.729886983': '5',
        'entry.1728072201': '5',
    }

    try:
        response = requests.post(url, data=data)
        print(f"Статус код: {response.status_code}")
        
        if response.status_code == 200:
            print("Успішно відправлено! ✅")
        else:
            print("Помилка 400. Шукаю причину...")
            # Перевіряємо, чи немає в тексті назви ID, яке викликало помилку
            for key in data.keys():
                if key in response.text:
                    print(f"⚠️ Здається, проблема в полі: {key}")
            
            # Якщо хочете побачити більше, роздрукуємо шматок тексту, де зазвичай пишуть про помилки
            if "freebirdFormviewerViewResponseError" in response.text:
                print("Знайдено блок помилок у відповіді Google.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    send_form()
