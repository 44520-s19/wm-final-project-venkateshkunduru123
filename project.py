# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:48:17 2019

@author: S534845
"""

def switch_demo(argument):
    switcher = {
        2011: "https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/points-table",
        2012: "https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/points-table",
        2013: "https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/points-table",
        2014: "https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/points-table",
        2015: "https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/points-table",
        2016: "https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/points-table",
        2017: "https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/points-table",
        2018: "https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table",
        2019: "https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/points-table"
    }
    return switcher.get(argument, "nothing") 

import requests
from bs4 import BeautifulSoup

pune_match_count = pune_win_count = pune_loss_count =0
kochi_match_count = kochi_win_count = kochi_loss_count =0
mumbai_match_count = mumbai_win_count = mumbai_loss_count = 0
csk_match_count = csk_win_count = csk_loss_count = 0
deccan_match_count = deccan_win_count = deccan_loss_count = 0
rr_match_count = rr_win_count = rr_loss_count = 0
rising_match_count = rising_win_count = rising_loss_count = 0
rcb_match_count = rcb_win_count =rcb_loss_count = 0
punjab_match_count = punjab_win_count = punjab_loss_count = 0
gujarat_match_count = gujarat_win_count = gujarat_loss_count = 0
kkr_match_count = kkr_win_count = kkr_loss_count = 0
delhi_match_count = delhi_win_count = delhi_loss_count = 0
srh_match_count = srh_win_count = srh_loss_count = 0


all_teams = list()
total_info_dict = dict()

for year in range(2011,2020):
    #print(switch_demo(year))
    #print('\n' + str(year) + '\n')
    URL = switch_demo(year)
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html5lib')
    table = soup.find('table', {'class':'table cb-srs-pnts'})
    table_body = table.find('tbody')
    team_titles = table_body.find_all('a', {'class':'cb-text-link', 'title':''})
    title = list() # storing the team titles in the list
    for title1 in team_titles:
        title.append(title1.text)
        all_teams.append(title1.text)
    #print(title)
    #print(table_body.prettify())
    data =[]
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td', {'class':'cb-srs-pnts-td'})
        data.append([ele.text for ele in cols])
    
    points_data = list(i for i in data if i!=[])

    points_dict = {}
    for i in range(len(title)):
        points_dict.update({title[i]:points_data[i]})
    #print(points_dict)
    # storing the win and loss dictionaries
    win_dict = {}
    loss_dict = {}
    matches_played_dict = {}
    for i in range(len(points_dict)):
        matches_played_dict.update({title[i]:points_data[i][0]})
        win_dict.update({title[i]:points_data[i][1]})
        loss_dict.update({title[i]:points_data[i][2]})
    #print(matches_played_dict)
    #print(win_dict)
    #print(loss_dict)
    #rcb_match_count += int(matches_played_dict['Pune Warriors'])
    if 'Pune Warriors' in matches_played_dict:
        pune_match_count += int(matches_played_dict['Pune Warriors'])
        pune_win_count += int(win_dict['Pune Warriors'])
        pune_loss_count += int(loss_dict['Pune Warriors'])
        total_info_dict.update({'Pune Warriors':[pune_match_count, pune_win_count, pune_loss_count]})
    if 'Kochi Tuskers Kerala' in matches_played_dict:
        kochi_match_count += int(matches_played_dict['Kochi Tuskers Kerala'])
        kochi_win_count += int(win_dict['Kochi Tuskers Kerala'])
        kochi_loss_count += int(loss_dict['Kochi Tuskers Kerala'])
        total_info_dict.update({'Kochi Tuskers Kerala':[kochi_match_count, kochi_win_count, kochi_loss_count]})
    if 'Mumbai Indians' in matches_played_dict:
        mumbai_match_count += int(matches_played_dict['Mumbai Indians'])
        mumbai_win_count += int(win_dict['Mumbai Indians'])
        mumbai_loss_count += int(loss_dict['Mumbai Indians'])
        total_info_dict.update({'Mumbai Indians':[mumbai_match_count, mumbai_win_count, mumbai_loss_count]})
    if 'Chennai Super Kings' in matches_played_dict:
        csk_match_count += int(matches_played_dict['Chennai Super Kings'])
        csk_win_count += int(win_dict['Chennai Super Kings'])
        csk_loss_count += int(loss_dict['Chennai Super Kings'])
        total_info_dict.update({'Chennai Super Kings':[csk_match_count, csk_win_count, csk_loss_count]})
    if 'Deccan Chargers' in matches_played_dict:
        deccan_match_count += int(matches_played_dict['Deccan Chargers'])
        deccan_win_count += int(win_dict['Deccan Chargers'])
        deccan_loss_count += int(loss_dict['Deccan Chargers'])
        total_info_dict.update({'Deccan Chargers':[deccan_match_count, deccan_win_count, deccan_loss_count]})
    if 'Rajasthan Royals' in matches_played_dict:
        rr_match_count += int(matches_played_dict['Rajasthan Royals'])
        rr_win_count += int(win_dict['Rajasthan Royals'])
        rr_loss_count += int(loss_dict['Rajasthan Royals'])
        total_info_dict.update({'Rajasthan Royals':[rr_match_count, rr_win_count, rr_loss_count]})
    if 'Rising Pune Supergiant' in matches_played_dict:
        rising_match_count += int(matches_played_dict['Rising Pune Supergiant'])
        rising_win_count += int(win_dict['Rising Pune Supergiant'])
        rising_loss_count += int(loss_dict['Rising Pune Supergiant'])
        total_info_dict.update({'Rising Pune Supergiant':[rising_match_count, rising_win_count, rising_loss_count]})
    if 'Royal Challengers Bangalore' in matches_played_dict:
        rcb_match_count += int(matches_played_dict['Royal Challengers Bangalore'])
        rcb_win_count += int(win_dict['Royal Challengers Bangalore'])
        rcb_loss_count += int(loss_dict['Royal Challengers Bangalore'])
        total_info_dict.update({'Royal Challengers Bangalore':[rcb_match_count, rcb_win_count, rcb_loss_count]})
    if 'Kings XI Punjab' in matches_played_dict:
        punjab_match_count += int(matches_played_dict['Kings XI Punjab'])
        punjab_win_count += int(win_dict['Kings XI Punjab'])
        punjab_loss_count += int(loss_dict['Kings XI Punjab'])
        total_info_dict.update({'Kings XI Punjab':[punjab_match_count, punjab_win_count, punjab_loss_count]})
    if 'Gujarat Lions' in matches_played_dict:
        gujarat_match_count += int(matches_played_dict['Gujarat Lions'])
        gujarat_win_count += int(win_dict['Gujarat Lions'])
        gujarat_loss_count += int(loss_dict['Gujarat Lions'])
        total_info_dict.update({'Gujarat Lions':[gujarat_match_count, gujarat_win_count, gujarat_loss_count]})
    if 'Kolkata Knight Riders' in matches_played_dict:
        kkr_match_count += int(matches_played_dict['Kolkata Knight Riders'])
        kkr_win_count += int(win_dict['Kolkata Knight Riders'])
        kkr_loss_count += int(loss_dict['Kolkata Knight Riders'])
        total_info_dict.update({'Kolkata Knight Riders':[kkr_match_count, kkr_win_count, kkr_loss_count]})
    if 'Delhi Capitals' in matches_played_dict:
        delhi_match_count += int(matches_played_dict['Delhi Capitals'])
        delhi_win_count += int(win_dict['Delhi Capitals'])
        delhi_loss_count += int(loss_dict['Delhi Capitals'])
        total_info_dict.update({'Delhi Capitals':[delhi_match_count, delhi_win_count, delhi_loss_count]})
    if 'Sunrisers Hyderabad' in matches_played_dict:
        srh_match_count += int(matches_played_dict['Sunrisers Hyderabad'])
        srh_win_count += int(win_dict['Sunrisers Hyderabad'])
        srh_loss_count += int(loss_dict['Sunrisers Hyderabad'])
        total_info_dict.update({'Sunrisers Hyderabad':[srh_match_count, srh_win_count, srh_loss_count]})
    
        

#print()
#print(total_info_dict)

# second snippet

# win and lose percentage
win_percent = dict()
lose_percent = dict()
tie_percent = dict()
for i in (total_info_dict):
    win_percent[i] = round((total_info_dict[i][1]/total_info_dict[i][0]) * 100, 2)
    lose_percent[i] = round((total_info_dict[i][2]/total_info_dict[i][0]) * 100, 2)
    tie_percent[i] = round(100 - win_percent[i] - lose_percent[i], 2)
#print(win_percent)
#print()
#print(lose_percent)
#print()
#print(tie_percent)

# third snippet
'''
# visualization
import matplotlib.pyplot as plt
import matplotlib.style as style3
style3.use('default')
#style3.use('seaborn-dark')
style3.use('seaborn-talk')
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
team = win_percent.keys()
wins = win_percent.values()
loses = lose_percent.values()
ties = tie_percent.values()
team_tuple = tuple(team)
win_tuple = tuple(wins)
lose_tuple = tuple(loses)
tie_tuple = tuple(ties)
#print(team_tuple)
#print(win_tuple)
#print(lose_tuple)

y_pos = np.arange(len(team_tuple))

ax.barh(y_pos, win_tuple, color="green")
ax.set_yticks(y_pos)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticklabels(team_tuple,fontweight='bold')
for i, v in enumerate(win_tuple):
    ax.text(v + 1, i + 0.17, str(v)+' % (Won: ' + str(total_info_dict[team_tuple[i]][1]) + ' out of ' + str(total_info_dict[team_tuple[i]][0]) + ' matches)', color='black', fontweight='bold')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage',fontweight='bold')
ax.set_ylabel('IPL Teams',fontweight='bold')
ax.set_title('IPL Teams Win Percentage chart',fontweight='bold')

plt.show()

# forth snippet

# IPL Teams lose Percentage chart
import matplotlib.pyplot as plt
import matplotlib.style as style2
style2.use('default')
style2.use('seaborn-talk')

import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(y_pos, lose_tuple, color="red")
ax.set_yticks(y_pos)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticklabels(team_tuple,fontweight='bold')
for i, v in enumerate(lose_tuple):
    ax.text(v + 1, i + 0.17, str(v)+' % (Lost: ' + str(total_info_dict[team_tuple[i]][2]) + ' out of ' + str(total_info_dict[team_tuple[i]][0]) + ' matches)', color='black', fontweight='bold')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage',fontweight='bold')
ax.set_ylabel('IPL Teams',fontweight='bold')
ax.set_title('IPL Teams Lose Percentage chart',fontweight='bold')

plt.show()

# fifth snippet

# IPL Teams tie Percentage chart
import matplotlib.pyplot as plt
import matplotlib.style as style1
style1.use('default')
style1.use('seaborn-talk')

import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(y_pos, tie_tuple, color="yellow")
ax.set_yticks(y_pos)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticklabels(team_tuple,fontweight='bold')
for i, v in enumerate(tie_tuple):
    ax.text(v + 1, i + 0.17, str(v)+' %', color='black', fontweight='bold')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage',fontweight='bold')
ax.set_ylabel('IPL Teams',fontweight='bold')
ax.set_title('IPL Teams Tie Percentage chart',fontweight='bold')

plt.show()
'''

# sixth snippet
# Three results in one chart
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('default')
style.use('seaborn-poster')

# Example data
team = win_percent.keys()
wins = win_percent.values()
loses = lose_percent.values()
ties = tie_percent.values()
team_tuple = tuple(team)
win_tuple = tuple(wins)
lose_tuple = tuple(loses)
tie_tuple = tuple(ties)
#print(team_tuple)
#print(win_tuple)
#print(lose_tuple)

N = len(team_tuple)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, win_tuple, width, color='g')
rects2 = ax.bar(ind+width, lose_tuple, width, color='r')
rects3 = ax.bar(ind+width*2, tie_tuple, width, color='y')


ax.set_ylabel('Percentage',fontweight='bold')
ax.set_xlabel('Teams',fontweight='bold')
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_xticks(ind+width)
ax.set_xticklabels(team_tuple, rotation=20, ha='right', va='top',fontweight='bold')
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Won %', 'Lose %', 'Tie %') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%.2f'%(h),
                ha='center', va='bottom', rotation = 90, fontweight='bold')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.title('IPL Teams Result Chart',fontweight='bold')
plt.show()
