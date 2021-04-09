import requests
from bs4 import BeautifulSoup


# Function: recordStatsOfEntireTeam
# Parameters:
# Description: Reads from list of teams and finds the teams in the input array (clicks on the ones in the list or all)
# from there, it will read the playerStats of each player on those teams
# Return:
def recordStatsOfEntireTeam(url):
	return

# Function: readPlayerStatsByTeams
# Parameters:
# Description: Reads from list of teams and finds the teams in the input array (clicks on the ones in the list or all)
# from there, it will read the playerStats of each player on those teams
# Return:
def recordStatsOfAllActivePlayers(url):

	# read the page contents using BeautifulSoup
	soup = BeautifulSoup(requests.get(url).content, features='lxml')

	# I am looking at all of the table containers, thei first of whicall of thh contains all of the active teams as hyperlinks.
	rows = soup.findAll('div', class_="table_container")

	# all of the team names are hyperlinks, the only ones in that particular table element
	teams_data = [item for item in rows[0].findAll('a')]
	print(teams_data)
	#team_names = [item.getText() for item in rows[0].findAll('a')]

	# outer loop that goes through each of the teams to be selected and navigates to the team roster
	for team in [team_data for team_data in teams_data]:
		print("TEAM searching for ", team.getText(), "...")
		soup = BeautifulSoup(requests.get("https://www.basketball-reference.com"+team['href']).content, features='lxml')
		soup = BeautifulSoup(requests.get("https://www.basketball-reference.com"+soup.findAll('a',  text = "2020-21")[0]['href']).content, features='lxml')

		# grab the list of players then iterate over it
		rows = ([item for item in soup.findAll("div", class_= "table_container")[0].findAll(attrs={"data-stat":"player"})])
		for player_data in rows:
			print("TEAM searching for ", player_data.getText(), "...")
			if player_data.findAll('a'):
				readPlayerStats("https://www.basketball-reference.com"+player_data.findAll('a')[0]['href'])

# Function: readPlayerStats
# Parameters: driver - web driver used that contains the url data
# Description: grabs all of the average stats for each season the player has played
# Return: 2D dictionary, each dictionary instance contains a row of stats from the table
def readPlayerStats(url):

	# read the page contents using BeautifulSoup
	soup = BeautifulSoup(requests.get(url).content, features='lxml')
	rows = soup.findAll('tr', class_="full_table")
	items = [[item.getText() for item in rows[i].findAll('td')] for i in range(len(rows))]
	stat_table = {}

	# loop over each row of the stats table and grab the players average stats for each season
	for index, item in enumerate(items):
	    season = rows[index].findAll('a')[0].getText()
	    stat_table[index] = {'season': season, 'team': item[1], 'league': item[2], 'position': item[3], 'games': item[4], 'games_started': item[5], 'minutes_played': item[6], 'fgm': item[7], 'fga': item[8], 'fgp': item[9], '3pm': item[10], '3pa': item[11], '3pp': item[12], '2pm': item[13]  }

	print(stat_table[0])
	return stat_table

#recordStatsOfAllActivePlayers("https://www.basketball-reference.com/teams/")


#("https://www.basketball-reference.com/players/h/harrijo01.html")