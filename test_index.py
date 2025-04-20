from bs4 import BeautifulSoup

def test_hola_mundo():
    with open("index.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        h1 = soup.find("h1")
        assert h1 is not None
        assert "Hola Mundo" in h1.text