import csv 
import os
from utility import uprint

def extract_stat_names(dict_of_stats):
    """ Extracts all the names of the statistics

    Args:
        dict_of_stats (dict): Dictionary containing key-alue pair of stats
    """
    stat_names = []
    for key, val in dict_of_stats.items():
        stat_names += [key]
    return stat_names

def parse_players(list_of_players, base_filename):
    stat_names = extract_stat_names(list_of_players[0])
    filename = base_filename + 'players_raw.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    f = open(filename, 'w+', encoding='utf8', newline='')
    w = csv.DictWriter(f, sorted(stat_names))
    w.writeheader()
    for player in list_of_players:
            w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in player.items()})

def parse_teams(list_of_teams, base_filename):
    stat_names = extract_stat_names(list_of_teams[0])
    filename = base_filename + 'teams_raw.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    f = open(filename, 'w+', encoding='utf8', newline='')
    w = csv.DictWriter(f, sorted(stat_names))
    w.writeheader()
    for team in list_of_teams:
            w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in team.items()})

def parse_element_types(list_of_element_types, base_filename):
    stat_names = extract_stat_names(list_of_element_types[0])
    filename = base_filename + 'element_types_raw.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    f = open(filename, 'w+', encoding='utf8', newline='')
    w = csv.DictWriter(f, sorted(stat_names))
    w.writeheader()
    for element_type in list_of_element_types:
            w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in element_type.items()})



def parse_player_history(list_of_histories, base_filename, player_name, Id):
    if len(list_of_histories) > 0:
        stat_names = extract_stat_names(list_of_histories[0])
        filename = base_filename + player_name + '_' + str(Id) + '/history.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, 'w+', encoding='utf8', newline='')
        w = csv.DictWriter(f, sorted(stat_names))
        w.writeheader()
        for history in list_of_histories:
            w.writerow(history)

def parse_player_gw_history(list_of_gw, base_filename, player_name, Id):
    if len(list_of_gw) > 0:
        stat_names = extract_stat_names(list_of_gw[0])
        filename = base_filename + player_name + '_' + str(Id) + '/gw.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, 'w+', encoding='utf8', newline='')
        w = csv.DictWriter(f, sorted(stat_names))
        w.writeheader()
        for gw in list_of_gw:
            w.writerow(gw)
