import requests

def send_form():
    # URL для відправки (змінено на formResponse)
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSfdxStsy5Twu5PfNyhIWgD0X3_VXgycUeulWZCfYAEIZx_9xA/formResponse'

    # Ваші дані
    data = {
        'entry.989579441': 'Білецький Костянтин Олександрович',
        'entry.1397610976': '44',
        'entry.137561573': 'Чоловіча',
        # Сім чекбоксів зі значенням "5"
        'entry.660933792': '5',
        'entry.1402637491': '5',
        'entry.1281485910': '5',
        'entry.1833081246': '5',
        'entry.2000936683': '5',
        'entry.119197893': '5',
        'entry.1341819021': '5',
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
