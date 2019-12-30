import bs4 as bs
import urllib.request
import regex as re
import json

def scrape():
	source = urllib.request.urlopen('https://www.nytimes.com/puzzles/sudoku/medium').read()
	soup = bs.BeautifulSoup(source,'lxml')

	divTags = soup.find_all('div', {'class': 'pz-section'})
	script = soup.find_all('script')
	script_text = script[0].text.split(' = ')[1]

	# parse x:
	y = json.loads(script_text)
	# the result is a Python dictionary:
	puzzle = y["medium"]["puzzle_data"]["puzzle"]
	# print(script_text)
	n = 9
	board = [puzzle[i:i + 9] for i in range(0, len(puzzle), 9)]
	return board