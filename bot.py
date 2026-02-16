import requests

def send_form():
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScXqDwCbQCElrXOWXjbRt9nBXPswlC8J3-gxE6WTQ2p7c6gtQ/formResponse'

    data = {
        'entry.404296076': 'Білецький Костянтин Олександрович',
        'entry.471758851': '44',
        'entry.630045100': 'Чоловіча'
    }

    try:
        response = requests.post(url, data=data)
        print(f"Статус код: {response.status_code}")
        if response.status_code == 200:
            print("Успішно відправлено! Перевіряйте таблицю. ✅")
        else:
            print(f"Помилка сервера: {response.status_code}")
            # Це допоможе побачити, на що саме скаржиться Google
            print(f"Текст помилки: {response.text[:200]}") 
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    send_form()
