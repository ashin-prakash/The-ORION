print("Welcome to My First ever Hunt Game")
print("The ORION")

name = input("What is your Name? ")
age = input("What is your age? ")

print("Welcome ", name , "of age ",age, "to the Great ORION")

hp = 100

if int(age) >= 18:
  print("You are old enough to play! ", name)
  print("You have", hp,  "HP")

  w = input("Do you Wish to continue? (yes or no)").lower()
  if w == "yes":
    print("Lets Play!")
  
    left_or_right = input("First choice... Left or Right (left/right)")
    if left_or_right == "left":
      ans = input("Nice.... You followed one of the path and reached a lake.. Do you wish to swim or go through a bridge?(swim/bridge) ").lower()

      if ans == "swim":
        print("You Lost 10 HP and now your HP is 90")
        land_or_swimm = input("Now that was good, as you love swimming, whether you like to swim more or get onto land (swim more/land)").lower()

        if land_or_swimm == "land":
          ans_1 = input("As of now you are doing really good. As now you are on Land you can choose either Mountain route or Jungle route (mountain/jungle)").lower()

          if ans_1 == "mountain":
            print("You lost....hard luck")

          elif ans_1 == "jungle":
            print("Wow, You are on the Right Track So U got a bonus.")
            print("Extra 10 Hp as bonus, So your HP is 100 again.")
            print("Congratulations...!")

            q = input("As ur so long now, are you tired or enjoying the game?(enjoy/tired)").lower()
            if q == "enjoy":
              print("So you wish to continue right, Glad to hear it from you...")

              walk_swing = input("So as you are on the Jungle path, you can either be like wolf and walk or be like monkeys and swing (walk/swing)").lower()

              if walk_swing == "walk":
                print("So you love Walking right. Pretty Impressive")
                e = input("As now you are a walking dude, Would you like to walk fast or slow(fast/slow)").lower() 

                if e == "slow":
                  print("Damn, You are close..")
                  r = input("So now these are direct. choose one(underground/overground)").lower()

                  if r == "underground":
                    print("You are on the brim..")
                    t = input("Now this is like life and death, as you are ar underground what will you choose, through tunnel or without tunnel?(tunnel/withouttunnel)").lower()

                    if t == "withouttunnel":
                      print("As you where long though there stood a question life or death and you chose...")
                      print("You died, game over...")

                    elif t == "tunnel":
                      print("Finally you suceeded and came to the end")
                      print("Welcome to the ORION!!")
                      print("Congratulations......!")
                      print("You won...Congrats", name, "For completing ORION Do come For ORION 2")

                    else:
                      print("You lost..")
                    
                  elif r == "overground":
                    print("Close but not cigar, You lost....")
                  else:
                    print("You lost....")

                elif e == "fast":
                  print("Damn, You are close..")
                  y = input("So now these are direct. choose one(sun/moon").lower()

                  if y == "sun":
                    print("You Lost...")
                  elif y == "moon":
                    print("You are on the brim..")
                    t = input("Now this is like life and death, choose one(hot/cold)").lower()

                    if t == "hot":
                      print("You lost..")
                    else:
                      print("You lost")
                
                else:
                  print("You lost....!")

              elif walk_swing == "swing":
                print("So You like to swing like a monkey... Nice choice..")
                print("As you have swinged and reached the destination, the rest of the questions are based on your choice")
                u = input("Your choice will lead you..Choose(bread/butter)").lower()

                if u == "bread":
                  print("Your choice was not good at the moment")
                  print("So you lost!!")

                elif u == "butter":
                  print("You u have a good taste ", name)
                  i = input("As you love butter so much, would you love (chocochip/strawberry)").lower()

                  if i == "strawberry":
                    print("You lost")
                  elif i == "chocochip":
                    print("Great to go ahead, you might be close of winning the game.")
                    print("As now you are closer to winning, the next choices could lead you to victory!")
                    print("So play cautiosly...")
                    o = input("So now choices are different... choose one(bike/car)?").lower()

                    if o == "bike":
                      print("So..... I think you are a rider...Great choice...")
                      p = input("As your interest is bikes, what you love more long rides or short rides(long/short)").lower()

                      if p == "long":
                        print("As you love long rides, you would love different kindes of places.")
                        a = input("Which kind of place do you love (cities, villiages)").lower()

                        if a == "cities":
                          print("Wow You have taken cities routes, so basically you would be a busy guy.")
                          print("But unfortunately, You lost!")

                        elif a == "villiages":
                          print("As you came this much, you must be tired.")
                          s = input("Would like to drink something?(yes/no)").lower()
                          
                          if s == "yes":
                            print("So glad to hear that you want to drink something.")
                            d = input("What would you like to drink?(tea/pepsi)").lower()

                            if d == "tea":
                              print("Its good to drink tea, but something is not right.")
                              print("As you selected that you are tired, you are no longer fit for the game!")
                              print("Sorry, You Lost!")

                            elif d == "pepsi":
                              print("Where can you see pepsi in a villiage?")
                              print("Sorry You lost!")

                            else:
                              print("You Lost!")
                          
                          elif s == "no":
                            print("As you are not tired lets continue.")
                            print("Now as you are at villiage, and the time now is night")
                            f = input("Would you like to sleep or roam around the place?(sleep/roam)").lower()

                            if f == "sleep":
                              print("You lost!")

                            elif f == "roam":
                              print("Roaming at late is not good for a gentleman")
                              print("So.... ")
                              print(name, "You lost!")  

                            else:
                              print("You lost!")

                          else:
                            print("You Lost")

                        else:
                          print("You Lost")
                
                
                      elif p == "short":
                        print("Sorry you lost!")

                      else:
                        print("You lost..")

                    

                    else:
                      print("You lost!")

                  else:
                    print("You Lost!")

                else:
                  print("You lost!")    
                   
                
              else:
                print("Sorry you lost...")

            else:
              print("You Lost...")


          else:
            print("You lost, Game Over..")

        else:
          print("Sorry You lost....")

      
      elif ans == "bridge":
        print("So You love to walk rather than swimming right?")
        print("Then there will be a task for you..")
        print("The bridge you are travelling is not completed. You have 2 choices.")
        print("You have a bike and you can do a stunt and get onto next side.")
        print("Or you can just wait for the bridge to get completed.")
        g = input("so what will you choose?(bike/wait)").lower()
        
        if g == "bike":
          print("So now you got the bike, so you can now jump off the bridge to other side.")
          print("But wait! something is with the bike, what you will do?")
          print("You lost!")

        else:
          print("you lost...")

      else:
        print("You lost......")


    else:
      print("Game Over")



  else:
    print("bubyee.....")
else:
  print("You are not old enough to play....")



