import urllib.request
from bs4 import BeautifulSoup

score_board = urllib.request.urlopen('http://scoreboard.eks.centralqa.de/scoreboard').read()
soup = BeautifulSoup(score_board, 'html.parser')
print(soup.prettify())
