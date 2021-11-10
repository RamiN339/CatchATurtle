# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import time
import leaderboard as lb
#-----game configuration----
global score
score =0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
wn = trtl.Screen()
leader_names_list=[]
leader_scores_list=[]
player_name = wn.textinput('Start Screen', 'What is your name? ')

wn.bgcolor('red')
#-----initialize turtle-----
circle = trtl.Turtle()
circle.shape('circle')
circle.speed(0)
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
colors = ['blue', 'pink', 'green', 'yellow']
counter.hideturtle()
score_writer.hideturtle()
def manage_leaderboard():
  # load all the leaderboard records into the lists
  global leader_scores_list
  global leader_names_list
  global score
  global circleram
  lb.load_leaderboard('a122_leaderboard.txt', leader_names_list, leader_scores_list)
  print(leader_names_list)
  print(leader_scores_list)

  # TODO
  if (int(len(leader_scores_list)) < 5 or score > int(leader_scores_list[4])):
    lb.update_leaderboard('a122_leaderboard.txt', leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, circle, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, circle, score)

#-----game functions--------
while True:
  play = wn.textinput('Menu', 'Would you like to play the game? (yes or no)): ')
  try:
    if play.upper() == "YES":
      print('hi')
      break
  except ValueError:
    continue
def countdown():
        global timer, timer_up
        counter.clear()
        if timer <= 0:
          counter.write("Time's Up", font=font_setup)
          
          timer_up = True
          manage_leaderboard()
        else:
          counter.write("Timer: " + str(timer), font=font_setup)
          timer -= 1
          counter.getscreen().ontimer(countdown, counter_interval) 
          

def update_score():
          score_writer.penup()
          score_writer.goto(-100,200)
          score_writer.pendown()
          font_setup = ("Arial", 20, "normal")
          score_writer.clear()
          global score
          score = score + 1
          score_writer.write(score, font=font_setup)


def circle_clicked(x,y):
          if timer_up != True:
            x = random.randint(0,300)
            y = random.randint(0,200)
            circle.penup()
            circle.shapesize(random.randint(1,5))
            circle.color(colors[random.randint(0,3)])
            circle.goto(x,y)
            update_score()
    

  


#-----events----------------
circle.onclick(circle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
