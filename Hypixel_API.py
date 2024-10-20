
import time
from turtle import done
import requests

player_ID = input ("ID: ")
player_info = requests.get("https://api.mojang.com/users/profiles/minecraft/"+player_ID)
player_info_json = player_info.json()

x = []
for test in player_info_json.keys():
    x.append (test)

if  ("id") not in x:
    print ("Incorrect ID.")
    done
else:
    player_UUID = player_info_json ["id"]

    #invalid key Sample (for testing purpose only): 7b6e32a6-0054-4e78-9801-6517b33c7d79

    #Valid Key Sample: b50a3ac6-83b7-4155-80f8-74bf9e83be04

    #print (recent_games_json)


    def API_detection ():
        Key = input ("Enter a Hypixel API Key: ")
        player_recent_games = requests.get("https://api.hypixel.net/status?key="+ Key + "&uuid="+ player_UUID)
        player_stats = requests.get("https://api.hypixel.net/player?key="+ Key + "&uuid="+ player_UUID)


        recent_games_json = player_recent_games.json()
        player_stats_json = player_stats.json()
        while recent_games_json['success'] == False:
            if recent_games_json['cause'] and player_stats_json ['cause']== "Invalid API key":
                print ("Error: Invalid API key.")
                time.sleep (1)
                New_Key = input("Input a valid hypixel API key: ")
                player_recent_games = requests.get("https://api.hypixel.net/status?key="+ New_Key + "&uuid="+player_UUID)
                player_stats = requests.get('https://api.hypixel.net/player?key='+ New_Key + '&uuid='+player_UUID)
                recent_games_json = player_recent_games.json()
                player_stats_json = player_stats.json()
            else: 
                print ("Error: The player has his/her API disabled.")


        

        if recent_games_json['success'] == True:
            #print (player_stats_json)
            if player_stats_json['player'] == None:
                print ("Player has never logged in Hypixel.")
            else:
                player_stats_name = (player_stats_json['player']['displayname'])
                if recent_games_json['session']['online'] == True:
                    #print ("The player has been online.")
                    #Test statement
            
                    recent_game_type = recent_games_json['session']['gameType']
                    if recent_game_type == "WALLS3":
                        recent_game_type = "mega walls"
            
                    mode = recent_games_json['session']['mode']
                    if mode == ("lobby") or "LOBBY":

                        mode = mode.lower()
                        
                        recent_game_type = recent_game_type.lower()
                        print (player_stats_name + " is currently in the "+ recent_game_type +" lobby.")
            
                    else:
                        map = recent_games_json['session']['map']
                            #print (recent_game_type)
                        if recent_game_type == "mega walls":
                            mw_class = player_stats_json['player']['stats']['Walls3']['chosen_class']
                            class_skin = player_stats_json ['player']['stats']["Walls3"]['chosen_skin_'+mw_class]
                    
                        
                            #if class_skin == mw_class:
                        
                                #print (player_stats_name + " is currently playing "+ mode +" mode mega walls on the map "+ map + ".\nChosen Class: "+ mw_class + "\nChosen Skin: Default")
                                #Fxn not currently working needs troubleshoot
                    
                            if mode == "face_off":
                                map = map.replace(" ", "")
                                print (player_stats_name + " is currently playing face off mode mega walls on the map "+ map + ".\nChosen Class: "+ mw_class + "\nChosen Skin: "+ class_skin)
                            else: 
                                print (player_stats_name + " is currently playing "+ mode + " mode mega walls on the map "+ map + ".\nChosen Class: "+ mw_class + "\nChosen Skin: "+ class_skin)
                        else:
                            recent_game_type = recent_game_type.lower()
                            print (player_stats_name +" is currently playing "+ recent_game_type + " on the map "+ map + ".")
                elif recent_games_json['session']['online'] == False:
                    print (player_stats_name + " is currently offline.")
                    #Add more fxn here.
                    #if recent_games_json['mostRecentGameType'] == "WALLS3":
                        #print (player_name + "is currently playing mega walls.")
            
                else: 
                    print ("Something is wrong, please contact the dev. ")



    API_detection()
