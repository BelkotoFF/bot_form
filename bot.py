import requests

def send_form():
    # ВИПРАВЛЕНО: додано подвійний слеш //
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScXqDwCbQCElrXOWXjbRt9nBXPswlC8J3-gxE6WTQ2p7c6gtQ/formResponse'

    data = {
        'entry.404296076': 'Білецький Костянтин Олександрович',
        'entry.471758851': '44',
        'entry.135272180': 'Чоловіча',
        #'entry.1837420053': '5',
        #'entry.1999428519': '5',
        #'entry.900161138': '5',
        #'entry.653386262': '5',
        #'entry.1630851971': '5',
        #'entry.729886983': '5',
        #'entry.1728072201': '5',
    }

    try:
        response = requests.post(url, data=data)
        # Перевіряємо, чи є в тексті відповіді підтвердження від Google
        if response.status_code == 200:
            if "Відповідь записано" in response.text or "Your response has been recorded" in response.text:
                print("Успішно відправлено і записано в таблицю! ✅")
            else:
                print("Сервер повернув 200, але підтвердження запису не знайдено. Перевірте ID.")
        else:
            print(f"Помилка сервера: {response.status_code}")
    except Exception as e:
        print(f"Сталася помилка при відправці: {e}")

if __name__ == "__main__":
    send_form()
