import random as r

class Match:

  def __init__(self):
    # During the initialisation we get the names of both teams 
    # as input from the user and initialise other important variables.
    self.team1=input('Enter first team:')
    self.team2=input('Enter second team:')
    self.n=11
    self.overs=20
    
    self.player1=['MS Dhoni','Faf du Plessis','Ruturaj Gaikwad','Suresh Raina',
                  'Ambati Rayudu','Robin Uthappa','Ravindra Jadeja',
                  'Sam Curran','Dwayne Bravo','Mitchell Santner','Imran Tahir',
                  'Deepak Chahar','Shardul Thakur','Lungi Ngidi',
                  'Josh Hazlewood','Moeen Ali','Krishnappa Gowtham',
                  'Cheteshwar Pujara'
                  ]
    r.shuffle(self.player1)  
    self.player1=self.player1[:self.n]   # Selection of Playing 11.
    
    self.player2=['Rohit Sharma','Ishan Kishan','Suryakumar Yadav',
                  'Adam Milne','Aditya Tare','Chris Lynn','Dhawal Kulkarni',
                  'Hardik Pandya','Krunal Pandya','Jasprit Bumrah',
                  'James Neesham','Keiron Pollard','Nathan Counternile',
                  'Quinton Decock','Trent Boult','Piyush Chawla','Rahul Chahar',
                  'Arjun Tendulkar'
                  ]
    r.shuffle(self.player2)
    self.player2=self.player2[:self.n]
    
    # Creating a dictionary containing the team name as key and 
    # list of players as the value
    self.team={self.team1:self.player1,self.team2:self.player2}
    return 

  def toss(self):
    # This Function performs the toss between the two given teams
    # and also tells the team which has won the toss has chosen to
    # bat first or ball first. Both these operations are performed
    # using the random module.

    print('Toss is being done between '+self.team1+' and '+self.team2)
    winner=r.choice([self.team1,self.team2])
    print(winner+' won the toss!!')
    
    choose=r.choice(['bat','ball'])
    print(winner+' has chose to '+choose+' first!!')

    if choose=='bat':
      if winner==self.team1:
        return self.team1,self.team2
      else:
        return self.team2,self.team1
    
    else:
      if winner==self.team1:
        return self.team2,self.team1
      else:
        return self.team1,self.team2

  def innings(self,bat,ball,temp):
    # This Function takes the list of both the teams as input
    # Ball by Ball statistics are printed in the output 
    # It returns the score and wicket after the innings completion.
    score=0
    wicket=0
    
    batsman_scores={k:0 for k in bat}
    bowler_wickets={k:0 for k in ball}
    bowler_runs={k:0 for k in ball}
    bowler_overs={k:0 for k in ball}
    
    strike=bat[0]     # Batsman on strike
    non_strike=bat[1] # Batsman on Non_strikers end
    j=0
    k=0
    
    while j<(self.overs):
      
      if k==self.n-1:
        k=0
      else:
        k+=1
      
      bowler=ball[k]  
      i=0
      
      while i<6:
        # What has happened on the particular delivery will be stored
        # in 's' and it is calculated using random module, probability
        # list is passed along. 
        s=r.choices([0,1,2,3,4,6,'W','Wide','No Ball'],
                    [0.45,0.2,0.1,0.01,0.1,0.04,0.02,0.04,0.04])
        t=s[0]

        if str(t).isdigit():
          bowler_runs[bowler]+=t
          i+=1
          if t in [0,2,4,6]:
            # If even score strike is not changed
            batsman_scores[strike]+=t
          else:
            # if odd score strike will change
            batsman_scores[strike]+=t
            nons=strike
            strike=non_strike
            non_strike=nons
          score+=t
        
        elif t=='W':
          # When wicket is down
          i+=1
          bowler_wickets[bowler]+=1
          
          if wicket>=(self.n-2):
            # If all batsman get out
            print(strike,' OUT')
            wicket+=1
            print('ALL OUT!!')
            break
          else:
            print(strike,' OUT')
            strike=bat[wicket+2]
            wicket+=1
        
        else:
          # For the Wide and NoBall
          print(t)
          score+=1
          bowler_runs[bowler]+=1
  
        # Printing the statistics after each delivery
        print(j+i/10,' ',score,'/',wicket,' ',strike,'*',batsman_scores[strike],
              non_strike,batsman_scores[non_strike],' ',bowler,
              bowler_runs[bowler],'/',bowler_wickets[bowler])
        
        if score >temp:
          # If the second team score becomes greater than first team
          print('BOWLING STATS:')
          for bowl in ball:
            print(bowl,':',bowler_overs[bowl],'/',bowler_runs[bowl],'/',
                  bowler_wickets[bowl])
          print()
          print('BATTING STATS:')
          for bats in bat:
            print(bats,':',batsman_scores[bats])
          print()
          return score,wicket
      
      bowler_overs[bowler]+=1
      # Strike change after over completion
      ov=strike        
      strike=non_strike
      non_strike=ov
      print()
      j+=1
      if wicket>(self.n-2):
        # If all batsmen get out
        break
    
    print('Total Score:',score,'/',wicket)
    print()

    # Printing the Team's Performance after Innings Completion
    print('BOWLING STATS:')
    for bowl in ball:
      print(bowl,':',bowler_overs[bowl],'/',bowler_runs[bowl],'/',
            bowler_wickets[bowl])
    print()

    print('BATTING STATS')
    for bats in bat:
      print(bats,':',batsman_scores[bats])

    return score,wicket
  
  def play(self):
    # Getting which team will bat first
    first,second=self.toss()
     
    score1,wicket1=self.innings(self.team[first],self.team[second],99999999)
    print('Score of ',first,' after first innings: ',score1,'/',wicket1)

    score2,wicket2=self.innings(self.team[second],self.team[first],score1)
    print('Score of ',first,' after first innings: ',score1,'/',wicket1)
    print('Score of '+second+' after second innings: ',score2,'/',wicket2)
    
    # Printing the Final Match Results
    if score1==score2:
      print('Match Drawn!!')
    
    elif score1>score2:
      print(first+' won by '+str(score1 - score2)+' runs')
    
    else:
      print(second+' won by '+str(10-wicket2)+' wickets')    
m=Match()
m.play()