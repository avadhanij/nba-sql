"""
Constants used in the application.
"""

"""
List of seasons.
"""
season_list = [
	'1996-97',
	'1997-98',
	'1998-99',
	'1999-00',
	'2000-01',
	'2001-02',
	'2002-03',
	'2003-04',
	'2004-05',
	'2005-06',
	'2006-07',
	'2007-08',
	'2008-09',
	'2009-10',
	'2010-11',
	'2011-12',
	'2012-13',
	'2013-14',
	'2014-15',
	'2015-16',
	'2016-17',
	'2017-18',
	'2018-19',
	'2019-20',
    '2020-21'
]

"""
Headers.
"""
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:86.0) Gecko/20100101 Firefox/86.0',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

"""
Team IDs. (Thank you nba-api).
"""
team_ids = [
    1610612737, #'ATL'
    1610612738, #'BOS'
    1610612739, #'CLE'
    1610612740, #'NOP'
    1610612741, #'CHI'
    1610612742, #'DAL'
    1610612743, #'DEN'
    1610612744, #'GSW'
    1610612745, #'HOU'
    1610612746, #'LAC'
    1610612747, #'LAL'
    1610612748, #'MIA'
    1610612749, #'MIL'
    1610612750, #'MIN'
    1610612751, #'BKN'
    1610612752, #'NYK'
    1610612753, #'ORL'
    1610612754, #'IND'
    1610612755, #'PHI'
    1610612756, #'PHX'
    1610612757, #'POR'
    1610612758, #'SAC'
    1610612759, #'SAS'
    1610612760, #'OKC'
    1610612761, #'TOR'
    1610612762, #'UTA'
    1610612763, #'MEM'
    1610612764, #'WAS'
    1610612765, #'DET'
    1610612766, #'CHA'
]
