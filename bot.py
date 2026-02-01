import requests

def send_form():
    # URL для відправки (змінено на formResponse)
    url = 'https:/docs.google.com/forms/d/e/1FAIpQLScXqDwCbQCElrXOWXjbRt9nBXPswlC8J3-gxE6WTQ2p7c6gtQ/formResponse'

    # Ваші дані
    data = {
        'entry.404296076': 'Білецький Костянтин Олександрович',
        'entry.471758851': '44',
        'entry.135272180': 'Чоловіча',
        # Сім чекбоксів зі значенням "5"
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
        if response.status_code == 200:
            print("Успішно відправлено! ✅")
        else:
            print(f"Помилка сервера: {response.status_code}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    send_form()
