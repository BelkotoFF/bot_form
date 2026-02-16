import requests

def send_form():
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScXqDwCbQCElrXOWXjbRt9nBXPswlC8J3-gxE6WTQ2p7c6gtQ/formResponse'

    # Використовуємо словник з точними значеннями
    # Переконайтеся, що у формі варіант "Чоловіча" написаний саме так
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
        'entry.1728072201': '5'
    }

    # Додаємо заголовки, щоб імітувати браузер (це часто вирішує помилку 400)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        # Відправляємо запит як справжня форма
        response = requests.post(url, data=data, headers=headers)
        
        print(f"Статус код: {response.status_code}")
        
        if response.status_code == 200:
            print("Успішно відправлено! ✅")
        elif response.status_code == 302:
            print("Google намагається перенаправити, зазвичай це теж успіх. Перевірте форму.")
        else:
            print(f"Помилка {response.status_code}. Можливо, у формі увімкнено 'Обмежити до 1 відповіді'?")
            
    except Exception as e:
        print(f"Критична помилка: {e}")

if __name__ == "__main__":
    send_form()
