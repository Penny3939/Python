#機器人的位置(x,y) &　判斷是否有走回原位
class Robot:
  
  def __init__(self,x,y,actions):
    self.x = x
    self.y = y
    self.origin_x = self.x
    self.origin_y = self.y
    
    for action in actions:
      if action =="U":
        self.up()
      elif action =="D":
        self.down()
      elif action =="L":
        self.left()
      else:
        self.right()

  def is_origin(self):
    return self.x ==self.origin_x and self.y==self.origin_y

  def up(self):
    self.y+=1

  def down(self):
    self.y-=1

  def left(self):
    self.x-=1

  def right(self):
    self.x+=1
    
  def __str__(self):
    return f"{self.x},{self.y}"

print(Robot(0,0,"UDRL"))
print(Robot(0,0,"UUUDD").is_origin())