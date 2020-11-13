#!/usr/bin/env python3

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/mewtwo",verify=False).json()

    print(f"URL: {pokeapi.get('sprites').get('front_default')}")
    print(len(pokeapi["game_indices"]))
    for move in pokeapi["moves"]:
        print(move["move"]["name"])
    #print(pokeapi["sprites"]["front_default"])

main()

