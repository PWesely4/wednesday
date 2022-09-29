# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
fill_color = ("green")
size = 2
shape = ("turtle")
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
# leaderboard variables
leaderboard_file_name = "leaderboard.txt"
player_name = input ("Please enter your name:")
#-----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(shape)
turtle.shapesize(size)
turtle.fillcolor(fill_color)
turtle.penup()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
counter.penup()
score_writer.penup()
#-----game functions--------
def change_position():
  (new_xpos) = rand.randint(-200,200)
  (new_ypos) = rand.randint(-200,200)
  turtle.goto(new_xpos,new_ypos)

def turtle_clicked(x,y):
    if timer_up == False:
        score_writer.clear()
        update_score()
        change_position()
    else:
        turtle.goto(1000,1000)
    
def update_score():
  global score
  score = score + 1
  score_writer.write(score, font=font_setup)

def position_score_writer():
  score_writer.penup()
  score_writer.goto(200,200)

def position_counter():
  counter.penup()
  counter.goto(-200,200)

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

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global turtle

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, turtle, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, turtle, score)
#-----events----------------
turtle.onclick(turtle_clicked)
position_score_writer()
position_counter()
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()