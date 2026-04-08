import requests


def hae_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])  # Tulostetaan vain vitsin teksti
    else:
        print("Vitsin hakeminen epäonnistui.")


if __name__ == "__main__":
    hae_vitsi()