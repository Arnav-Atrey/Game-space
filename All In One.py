import turtle                                                                          
import random
import time
import math

wn=turtle.Screen()
wn.setup(width=1180,height=852)
entry=turtle.Turtle()
wn.register_shape("entry1.gif")
entry.shape("entry1.gif")
start=input('Do you wish to start GAME SPACE: (Y/N) ')

if start=='Y' or start=='y':
    
    entry.clear()
    entry.shape('blank')
    

while True:
    
    print("1.SPACE INVADERS")
    print("2.DODGE")
    print("3.SUBWAY SURFER")
    print("4.WORD GAME")
    print("5.MASTERMIND")
    print("6.Quit")
    
    print()
    

    x=input("Choose your game: ")
    ############################################################
    if x=='1':
        
        wn.reset()
        wn=turtle.Screen()
        wn.bgcolor('black')
        wn.register_shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\space2.gif")
        wn.register_shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\ENEMY.gif")
        wn.register_shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\HERO.gif")
        wn.bgpic(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\space2.gif")
        wn.title('Space Invaders')
        count=0

        border_pen=turtle.Turtle()
        border_pen.speed(0)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300,-300)
        border_pen.pendown()
        border_pen.pensize(3)
        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)
        border_pen.hideturtle()

        score=turtle.Turtle()
        score.speed(0)
        score.penup()
        score.hideturtle()
        score.color('white')
        score.setpos(-290,300)
        score.write('Score: {}'.format(count),font=('Arial',20,'bold'))


        player=turtle.Turtle()
        player.color("blue")
        player.shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\HERO.gif")
        player.penup()
        player.speed(0)
        player.setposition(0,-250)
        player.setheading(90)
        playerspeed=30

        enemy1=turtle.Turtle()
        enemy1.color("red")
        enemy1.shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\ENEMY.gif")
        enemy1.penup()
        enemy1.speed(6)
        enemy1.setposition(-80,200)
        enemy1speed=20

        enemy2=turtle.Turtle()
        enemy2.color("red")
        enemy2.shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\ENEMY.gif")
        enemy2.penup()
        enemy2.speed(6)
        enemy2.setposition(-200,280)
        enemy2speed=20

        enemy3=turtle.Turtle()
        enemy3.color("red")
        enemy3.shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\ENEMY.gif")
        enemy3.penup()
        enemy3.speed(6)
        enemy3.setposition(0,200)
        enemy3speed=20

        enemy4=turtle.Turtle()
        enemy4.color("red")
        enemy4.shape(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\ENEMY.gif")
        enemy4.penup()
        enemy4.speed(6)
        enemy4.setposition(180,280)
        enemy4speed=20

        bullet=turtle.Turtle()
        bullet.color("cyan")
        bullet.shape("square")
        bullet.penup()
        bullet.speed(0)
        bullet.shapesize(stretch_wid=1,stretch_len=0.2)
        bullet.hideturtle()
        bulletspeed=25

        def move_left():
            x=player.xcor()
            x-=playerspeed
            if x<-280:
                x=-280
            player.setx(x)

        def move_right():
            x=player.xcor()
            x+=playerspeed
            if x>280:
                x=280
            player.setx(x)

        def isCollision(t1, t2):
            distance= math.sqrt((t1.xcor()-t2.xcor())**2+(t1.ycor()-t2.ycor())**2)
            if distance<15:
                return True
            else:
                return False

        def fire_bullet():
            
            x=player.xcor()
            y=player.ycor()+10
            bullet.setposition(x,y)
            bullet.showturtle()
            
        
            

        turtle.listen()
        turtle.onkey(move_left,"Left")
        turtle.onkey(move_right,"Right")
        turtle.onkey(fire_bullet,"space")
        #turtle.onkey(Quit,"q")

        
        while True:
            

      

            x=enemy1.xcor()
            x+=enemy1speed
            enemy1.setx(x)

            x=enemy2.xcor()
            x+=enemy2speed
            enemy2.setx(x)

            x=enemy3.xcor()
            x+=enemy3speed
            enemy3.setx(x)

            x=enemy4.xcor()
            x+=enemy4speed
            enemy4.setx(x)
           
            if enemy1.xcor()>280:
                y=enemy1.ycor()
                y-=40
                enemy1speed*=-1
                enemy1.sety(y)

            if enemy1.xcor()<-280:
                y=enemy1.ycor()
                y-=40
                enemy1speed*=-1
                enemy1.sety(y)

            if enemy2.xcor()>280:
                y=enemy2.ycor()
                y-=40
                enemy2speed*=-1
                enemy2.sety(y)

            if enemy2.xcor()<-280:
                y=enemy2.ycor()
                y-=40
                enemy2speed*=-1
                enemy2.sety(y)

            if enemy3.xcor()>280:
                y=enemy3.ycor()
                y-=40
                enemy3speed*=-1
                enemy3.sety(y)

            if enemy3.xcor()<-280:
                y=enemy3.ycor()
                y-=40
                enemy3speed*=-1
                enemy3.sety(y)

            if enemy4.xcor()>280:
                y=enemy4.ycor()
                y-=40
                enemy4speed*=-1
                enemy4.sety(y)

            if enemy4.xcor()<-280:
                y=enemy4.ycor()
                y-=40
                enemy4speed*=-1
                enemy4.sety(y)

            if isCollision(player, enemy1):
                player.hideturtle()
                enemy1.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                print("Score: ",count)
                break
           
            if isCollision(player, enemy2):
                player.hideturtle()
                enemy2.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                print("Score: ",count)
                break
           
            if isCollision(player, enemy3):
                player.hideturtle()
                enemy3.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                print("Score: ",count)
                break

            if isCollision(player, enemy4):
                player.hideturtle()
                enemy4.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                print("Score: ",count)
                break
           
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

            if isCollision(bullet,enemy1):
                bullet.hideturtle()
                enemy1.setposition(-280,280)
                count+=10
                score.clear()
                score.write('Score: {}'.format(count),font=('Arial',20,'bold'))
               
            if isCollision(bullet,enemy2):
                bullet.hideturtle()
                enemy2.setposition(-280,280)
                count+=10
                score.clear()
                score.write('Score: {}'.format(count),font=('Arial',20,'bold'))
               
            if isCollision(bullet,enemy3):
                bullet.hideturtle()
                enemy3.setposition(-280,280)
                count+=10
                score.clear()
                score.write('Score: {}'.format(count),font=('Arial',20,'bold'))
               
            if isCollision(bullet,enemy4):
                bullet.hideturtle()
                enemy4.setposition(-280,280)
                count+=10
                score.clear()
                score.write('Score: {}'.format(count),font=('Arial',20,'bold'))

           
        
        border_pen.hideturtle()
        enemy1.shape('blank')
        enemy2.shape('blank')
        enemy3.shape('blank')
        enemy4.shape('blank')
        player.shape('blank')
        wn.bgpic(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\black.gif")
        border_pen.clear()
        score.clear()
        
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        player.hideturtle()
        score.hideturtle()
        wn.reset()
        wn.bgcolor('black')
        
            
    #########################################################################
    if x=='2':
        wn.reset()
        
        #SCREEN
        wn=turtle.Screen()
        wn.bgcolor("black")
        wn.title("DODGE THE OBSTACLES")



        #PLAYER
        player=turtle.Turtle()
        player.color("blue")
        player.shape('triangle')
        player.penup()
        player.speed(1)
        player.setposition(0,-250)
        player.setheading(90)

        playerspeed=30

        #ENEMY
        enemy1=turtle.Turtle()
        enemy1.color("red")
        enemy1.shape("circle")
        enemy1.penup()
        enemy1.speed(0)
        enemy1.setposition(-100,765)

        enemy1speed=30

        enemy2=turtle.Turtle()
        enemy2.color("red")
        enemy2.shape("circle")
        enemy2.penup()
        enemy2.speed(0)
        enemy2.setposition(0,600)

        enemy2speed=30+random.randint(0,5)

        enemy3=turtle.Turtle()
        enemy3.color("red")
        enemy3.shape("circle")
        enemy3.penup()
        enemy3.speed(0)
        enemy3.setposition(328,875)

        enemy3speed=30+random.randint(0,5)

        enemy4=turtle.Turtle()
        enemy4.color("red")
        enemy4.shape("circle")
        enemy4.penup()
        enemy4.speed(0)
        enemy4.setposition(265,1090)

        enemy4speed=30+random.randint(0,5)

        enemy5=turtle.Turtle()
        enemy5.color("red")
        enemy5.shape("circle")
        enemy5.penup()
        enemy5.speed(0)
        enemy5.setposition(-123,987)

        enemy5speed=30+random.randint(0,5)

        enemy6=turtle.Turtle()
        enemy6.color("red")
        enemy6.shape("circle")
        enemy6.penup()
        enemy6.speed(0)
        enemy6.setposition(200,1600)

        enemy6speed=30+random.randint(0,5)

        enemy7=turtle.Turtle()
        enemy7.color("red")
        enemy7.shape("circle")
        enemy7.penup()
        enemy7.speed(0)
        enemy7.setposition(36,1035)

        enemy7speed=30+random.randint(0,5)

        enemy8=turtle.Turtle()
        enemy8.color("red")
        enemy8.shape("circle")
        enemy8.penup()
        enemy8.speed(0)
        enemy8.setposition(-34,1099)

        enemy8speed=30+random.randint(0,5)

        enemy9=turtle.Turtle()
        enemy9.color("red")
        enemy9.shape("circle")
        enemy9.penup()
        enemy9.speed(0)
        enemy9.setposition(-153,1111)

        enemy9speed=30+random.randint(0,5)

        enemy10=turtle.Turtle()
        enemy10.color("red")
        enemy10.shape("circle")
        enemy10.penup()
        enemy10.speed(0)
        enemy10.setposition(0,1253)

        enemy10speed=30+random.randint(0,5)

        enemy11=turtle.Turtle()
        enemy11.color("red")
        enemy11.shape("circle")
        enemy11.penup()
        enemy11.speed(0)
        enemy11.setposition(244,1444)

        enemy11speed=30+random.randint(0,5)

        enemy12=turtle.Turtle()
        enemy12.color("red")
        enemy12.shape("circle")
        enemy12.penup()
        enemy12.speed(0)
        enemy12.setposition(-265,1234)

        enemy12speed=30+random.randint(0,5)

        enemy13=turtle.Turtle()
        enemy13.color("red")
        enemy13.shape("circle")
        enemy13.penup()
        enemy13.speed(0)
        enemy13.setposition(-71,999)

        enemy13speed=30+random.randint(0,5)

        enemy14=turtle.Turtle()
        enemy14.color("red")
        enemy14.shape("circle")
        enemy14.penup()
        enemy14.speed(0)
        enemy14.setposition(90,1000)

        enemy14speed=30+random.randint(0,5)

        enemy15=turtle.Turtle()
        enemy15.color("red")
        enemy15.shape("circle")
        enemy15.penup()
        enemy15.speed(0)
        enemy15.setposition(-99,888)

        enemy15speed=30+random.randint(0,5)

        enemy16=turtle.Turtle()
        enemy16.color("red")
        enemy16.shape("circle")
        enemy16.penup()
        enemy16.speed(0)
        enemy16.setposition(-87,1567)

        enemy16speed=30+random.randint(0,5)

        def move_left():
            x=player.xcor()
            x-=playerspeed
            if x<-350:
                x=-350
            player.setx(x)

        def move_right():
            x=player.xcor()
            x+=playerspeed
            if x>350:
                x=350
            player.setx(x)

        def isCollision(t1, t2):
            distance= math.sqrt((t1.xcor()-t2.xcor())**2+(t1.ycor()-t2.ycor())**2)
            if distance<15:
                return True
            else:
                return False

        


        #KEYBOARD
        turtle.listen()
        turtle.onkey(move_left,"Left")
        turtle.onkey(move_right,"Right")
        

        while True:
            
            y=enemy1.ycor()
            y-=enemy1speed
            enemy1.sety(y)
           
            y=enemy2.ycor()
            y-=enemy2speed
            enemy2.sety(y)
           
            y=enemy3.ycor()
            y-=enemy3speed
            enemy3.sety(y)

            y=enemy4.ycor()
            y-=enemy4speed
            enemy4.sety(y)

            y=enemy5.ycor()
            y-=enemy5speed
            enemy5.sety(y)
           
            y=enemy6.ycor()
            y-=enemy6speed
            enemy6.sety(y)
           
            y=enemy7.ycor()
            y-=enemy7speed
            enemy7.sety(y)

            y=enemy8.ycor()
            y-=enemy8speed
            enemy8.sety(y)

            y=enemy9.ycor()
            y-=enemy9speed
            enemy9.sety(y)
           
            y=enemy10.ycor()
            y-=enemy10speed
            enemy10.sety(y)
           
            y=enemy11.ycor()
            y-=enemy11speed
            enemy11.sety(y)

            y=enemy12.ycor()
            y-=enemy12speed
            enemy12.sety(y)

            y=enemy13.ycor()
            y-=enemy13speed
            enemy13.sety(y)
           
            y=enemy14.ycor()
            y-=enemy14speed
            enemy14.sety(y)
           
            y=enemy15.ycor()
            y-=enemy15speed
            enemy15.sety(y)

            y=enemy16.ycor()
            y-=enemy16speed
            enemy16.sety(y)

            if isCollision(player, enemy1):
                player.hideturtle()
                enemy1.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy2):
                player.hideturtle()
                enemy2.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy3):
                player.hideturtle()
                enemy3.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy4):
                player.hideturtle()
                enemy4.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy5):
                player.hideturtle()
                enemy5.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy6):
                player.hideturtle()
                enemy6.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy7):
                player.hideturtle()
                enemy7.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy8):
                player.hideturtle()
                enemy8.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy9):
                player.hideturtle()
                enemy9.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy10):
                player.hideturtle()
                enemy10.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy11):
                player.hideturtle()
                enemy11.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy12):
                player.hideturtle()
                enemy12.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if isCollision(player, enemy13):
                player.hideturtle()
                enemy13.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n      :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy14):
                player.hideturtle()
                enemy14.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.hideturtle()
                text.write('YOU LOSE\n     :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy15):
                player.hideturtle()
                enemy15.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.write('YOU LOSE\n    :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()

            if isCollision(player, enemy16):
                player.hideturtle()
                enemy16.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE\n    :(',align='center',font=('Arial',30,'bold'))
                break
                wn.reset()
           
            if enemy1.ycor()<-400:
                enemy1.sety(400)
                enemy1.setx(player.xcor())

            if enemy2.ycor()<-400:
                 enemy2.sety(400)
             
            if enemy3.ycor()<-400:
                enemy3.sety(400)

            if enemy4.ycor()<-400:
                 enemy4.sety(400)
             
            if enemy5.ycor()<-400:
                 enemy5.sety(400)

            if enemy6.ycor()<-400:
                 enemy6.sety(400)
             
            if enemy7.ycor()<-400:
                enemy7.sety(400)

            if enemy8.ycor()<-400:
                 enemy8.sety(400)
                 
            if enemy9.ycor()<-400:
                enemy9.sety(400)

            if enemy10.ycor()<-400:
                 enemy10.sety(400)
                 enemy10.setx(player.xcor())
             
            if enemy11.ycor()<-400:
                enemy11.sety(400)

            if enemy12.ycor()<-400:
                 enemy12.sety(400)
             
            if enemy13.ycor()<-400:
                 enemy13.sety(400)

            if enemy14.ycor()<-400:
                 enemy14.sety(400)
             
            if enemy15.ycor()<-400:
                enemy15.sety(400)

            if enemy16.ycor()<-400:
                 enemy16.sety(400)
        enemy1.clear()
        enemy2.clear()
        enemy3.clear()
        enemy4.clear()
        enemy5.clear()
        enemy6.clear()
        enemy7.clear()
        enemy8.clear()
        enemy9.clear()
        enemy10.clear()
        enemy11.clear()
        enemy12.clear()
        enemy13.clear()
        enemy14.clear()
        enemy15.clear()
        enemy16.clear()
        player.clear()
            
            
    ################################################################################
    if x=='3':
        wn.reset()
        
                #SCREEN
        wn=turtle.Screen()
        wn.bgcolor('black')
        wn.bgpic(r"C:\Users\Arnav\Desktop\PES STUFF\PYTHON PROJECTS\GAME-11\black.gif")
        wn.title('lane game')
        
        wn.setup(width=600,height=600)
        wn.tracer(0)



        #Border
        lane1=turtle.Turtle()
        lane1.speed(0)
        lane1.shape("square")
        lane1.color("white")
        lane1.shapesize(stretch_wid=600,stretch_len=0.5)
        lane1.penup()
        lane1.goto(-105,0)

        lane2=turtle.Turtle()
        lane2.speed(0)
        lane2.shape("square")
        lane2.color("white")
        lane2.shapesize(stretch_wid=600,stretch_len=0.5)
        lane2.penup()
        lane2.goto(105,0)

        #PLAYER
        player=turtle.Turtle()
        player.color("blue")
        player.shape('triangle')
        player.shapesize(5)
        player.penup()
        player.speed(1)
        player.setposition(0,-200)
        player.setheading(90)


        #ENEMY
        enemy1=turtle.Turtle()
        enemy1.color("red")
        enemy1.shape("circle")
        enemy1.shapesize(5)
        enemy1.penup()
        enemy1.speed(0)
        enemy1.setposition(-200,250)
        enemy1speed=1.37

        enemy2=turtle.Turtle()
        enemy2.color("red")
        enemy2.shape("circle")
        enemy2.shapesize(5)
        enemy2.penup()
        enemy2.speed(0)
        enemy2.setposition(200,250)
        enemy2speed=1.37

        def move_left():
            x=player.xcor()
            if x!=-200:
                x-=200
            player.setx(x)

        def move_right():
            x=player.xcor()
            if x!=200:
                x+=200
            player.setx(x)

        def isCollision(t1, t2):
            distance= math.sqrt((t1.xcor()-t2.xcor())**2+(t1.ycor()-t2.ycor())**2)
            if distance<80:
                return True
            else:
                return False
        

        turtle.listen()
        turtle.onkey(move_left,"Left")
        turtle.onkey(move_right,"Right")

        time.sleep(10)
        start=time.time()

        while True:
            wn.update()
            L=list([0,200,-200])
            
            y=enemy1.ycor()
            y-=enemy1speed
            enemy1.sety(y)
           
            y=enemy2.ycor()
            y-=enemy2speed
            enemy2.sety(y)
           
            if isCollision(player, enemy1):
                player.hideturtle()
                enemy1.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                out=time.time()
                diff=int(out-start)
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE :(\n {} sec'.format(diff),align='center',font=('Arial',30,'bold'))
                break
           
            if isCollision(player, enemy2):
                player.hideturtle()
                enemy2.hideturtle()
                print("GAME OVER")
                print("YOU LOST  :(")
                out=time.time()
                diff=int(out-start)
                wn.reset()
                text=turtle.Turtle()
                text.color('white')
                text.hideturtle()
                text.write('YOU LOSE :(\n {} sec'.format(diff),align='center',font=('Arial',30,'bold'))
                
                break
            x=random.choice(L)

            if enemy1.ycor()<-300:
                
                enemy1.setpos(x,250)

            L.remove(x)

            if enemy2.ycor()<-300:
                x=random.choice(L)
                enemy2.setpos(x,250)
     

        
    ###################################################################################
    if x=='5':
        wn.reset()
        
        colors=['red','yellow','blue','green','orange','violet']
        print("colors used : red yellow blue green white indigo orange violet']\n")
        series=[]
        for i in range(4):
            series.append(random.choice(colors))
        count=7
        y=0
        ini=True


        while True:
            ask=input('Enter your 4 color series:')
            L=ask.split()
            if L!=series:
                display=[]
                for z in range(len(series)):
                    if L[z]==series[z]:
                        display.append('red')
                    elif L[z] in series:
                        display.append('white')
                    else:
                        display.append('blue')
                count-=1
                y-=40
                print('Number of chances left:',count)
                print()
                
            elif L==series:
                print('Congradulations your guessed it right :)')
                print('The sequence is shown on the screen')
                display=series
                a=input("Press any key to continue: ")
                ini=False
    
            if count==0:
                print('You lose :(')
                print('The sequence is shown on the screen')
                display=series
                ini=False

            wn=turtle.Screen()
            wn.setup(width=600,height=700)
            wn.bgcolor('black')
            wn.title('MasterMind')
            wn.tracer(0)

            c1=turtle.Turtle()
            c1.speed(0)
            c1.shape('circle')
            c1.shapesize(1)
            c1.color(display[0])
            c1.penup()
            c1.goto(-90,300+y)

            c2=turtle.Turtle()
            c2.speed(0)
            c2.shape('circle')
            c2.shapesize(1)
            c2.color(display[1])
            c2.penup()
            c2.goto(-30,300+y)

            c3=turtle.Turtle()
            c3.speed(0)
            c3.shape('circle')
            c3.shapesize(1)
            c3.color(display[2])
            c3.penup()
            c3.goto(40,300+y)
            
            c4=turtle.Turtle()
            c4.speed(0)
            c4.shape('circle')
            c4.shapesize(1)
            c4.color(display[3])
            c4.penup()
            c4.goto(90,300+y)
            
            text=turtle.Turtle()
            text.speed(0)
            text.hideturtle()
            text.color('white')
            text.penup()
            text.goto(0,-300)
            text.write('red: right colour right position\nwhite: right colour wrong position\nblue: wrong colour wrong position ',align='center',font=('Arial',15,'bold'))
            
            wn.update()      

            if ini==False:
                break
        wn.reset()
    #############################################################################
    if x=='4':
        wn.reset()
        L = ['ATRFC','MOUSE','DULCO']
        while True:
            d=1
            
            jword = random.choice(L)
            if d!= 1:
                break

            if jword == 'ATRFC':
                words = ['FAT','ART', 'CAT', 'RAT', 'CAR', 'AFT', 'TAR','FAR', 'CRAFT']
                dash = ['_ _ _', '_ _ _', '_ _ _', '_ _ _', '_ _ _', '_ _ _ _ _']
                while True:
                    print('  ', jword[1], '  ')
                    print(jword[0], '   ', jword[2])  # This print the hexagonal jumble letters
                    print(' ' + jword[3], ' ', jword[4])
                    print()
                    
                    for z in dash:       #prints dash
                        print(z)
                    print()
                        
                    win = 0    
                    for c in dash:
                        if c.isalpha() == True:                             #Its counting whether all elements are guessed or not
                            win += 1
                    if win == 6:
                        print('You win :)')
                        break
                    
                    x = input('Enter the word (All Caps): ')
                    con= input('would you like to continue:')
                    if con != 'Y':
                        d=0
                        break
                    
                    print()

                    if x in words:
                        if len(x) == 5:
                            dash[5] = x
                            words.remove(x)
                        else:
                            for i in range(len(dash)):
                                ini = False
                                if dash[i][0]=='_':
                                    dash[i]=x
                                    words.remove(x)
                                    ini=True
                                if ini==True:
                                    break
                                

                        print('Correct')
                        print()

                    elif x not in words:
                        print('Try Again')
                        print()
                                    ##############################################################
            if jword == 'MOUSE':
                words = ['USE', 'SUE','SUM', 'MOUSE', 'MUSE', 'SOME']
                dash = ['_ _ _', '_ _ _ _', '_ _ _ _', '_ _ _ _ _']
                while True:

                    print('  ', jword[1], '  ')
                    print(jword[0], '   ', jword[2])  # This print the hexagonal jumble letters
                    print(' ' + jword[3], ' ', jword[4])
                    print()
                    
                    for z in dash:       #prints dash
                        print(z)
                    print()
                        
                    win = 0    
                    for c in dash:
                        if c.isalpha() == True:                             #Its counting whether all elements are guessed or not
                            win += 1
                    if win == 4:
                        print('You win :)')
                        break
                    
                    x = input('Enter the word (All Caps): ')
                    print()

                    if x in words:
                        if len(x) == 5:
                            dash[3] = x
                            words.remove(x)

                        elif len(x) == 3:
                            dash[0] = x
                            words.remove(x)
                            
                        elif len(x)==4:
                            if dash[1][0]=='_':
                                dash[1]=x
                                words.remove(x)
                            else:
                                dash[2]=x
                                words.remove(x)
                                

                        print('Correct')
                        print()

                    elif x not in words:
                        print('Try Again')
                        print()
                                    ############################################################
            if jword == 'DULCO':
                words = ["DUO", "OLD", 'COD', "COLD", 'DOC',"LOUD","CLOUD","COULD"]
                dash = ['_ _ _', '_ _ _', '_ _ _ _','_ _ _ _','_ _ _ _ _', '_ _ _ _ _']
                while True:

                    print('  ', jword[1], '  ')
                    print(jword[0], '   ', jword[2])  # This print the hexagonal jumble letters
                    print(' ' + jword[3], ' ', jword[4])
                    print()
                    
                    for z in dash:       #prints dash
                        print(z)
                    print()
                        
                    win = 0    
                    for c in dash:
                        if c.isalpha() == True:                             #Its counting whether all elements are guessed or not
                            win += 1
                    if win == 6:
                        print('You win :)')
                        break
                    
                    x = input('Enter the word (All Caps): ')
                    print()

                    if x in words:
                        if len(x)==3:
                            if dash[0][0]=='_':
                                dash[0]=x
                                words.remove(x)
                            else:
                                dash[1]=x
                                words.remove(x)
                                
                        elif len(x)==4:
                            if dash[2][0]=='_':
                                dash[2]=x
                                words.remove(x)
                            else:
                                dash[3]=x
                                words.remove(x)
                            
                        elif len(x)==5:
                            if dash[4][0]=='_':
                                dash[4]=x
                                words.remove(x)
                            else:
                                dash[5]=x
                                words.remove(x)
                                

                        print('Correct')
                        print()

                    elif x not in words:
                        print('Try Again')
                        print()


            if x=='6':
                break
            

wn.reset()