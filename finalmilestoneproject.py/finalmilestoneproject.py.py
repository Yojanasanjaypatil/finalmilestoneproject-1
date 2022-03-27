game_list =[0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)
     position_choice():
    
    
    choice ='Wrong'
    while choice not in ['0','1','2']:
        
        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            
            print("Sorry,invalid choice! ")
            
    return int(choice)        
    def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at the position")
     
    game_list[position] = user_placement
    return game_list
     gameon_choice():
    
    def
    choice ='Wrong'
    while choice not in ['Y','N']:
        
        
        choice = input("Keep playing?(Y or N) ")
        
        if choice not in ['Y','N']:
            
            print("Sorry,I dont understand,please choose Y or N ")
            
    if  choice =="Y":
        return True 
    else:
        return False
        game_list = [0,1,2]

while game_on:
     game_on = True
  
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()