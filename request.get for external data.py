import requests
import json



# 拿世界盃的結果
r = requests.get('http://worldcup.sfg.io/matches/country?fifa_code=USA')
json.loads(r.text)[1]['winner_code']

# 拿 football 的結果1
r = requests.get('http://api.football-data.org/v1/teams/19/players')
json.loads(r.text)['players'][1]['dateOfBirth']

# 拿 football 的結果2
r = requests.get('http://api.football-data.org/v1/soccerseasons/354/fixtures/?matchday=22')
json.loads(r.text)['fixtures'][1]['result']['goalsAwayTeam']

# 拿外匯的結果1
r = requests.get('https://currency-api.appspot.com/api/USD/EUR.json')
json.loads(r.text)['rate']

# 拿外匯的結果2
r = requests.get('http://apilayer.net/api/historical?access_key=9b7ec6d18428b4e1fc5bf77194d90316&date=2005-02-01&format=1')
json.loads(r.text)['quotes']['USDEUR']

# 拿 NBA 的結果
r = requests.get('http://stats.nba.com/stats/playergamelog/?PlayerId=2544&Season=2015-16&SeasonType=Regular+Season&LeagueId=00')
json.loads(r.text)['resultSets'][0]['rowSet'][0][1]


help('requests.get')
help('dict')
help('list')
