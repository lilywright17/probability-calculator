import copy
import random

class Hat:
  #class should take a variable number of arguments that specify the number of balls of each color that are in the hat 
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
  
  def draw(self, num):
    if num>len(self.contents):
      return self.contents
    else:
      #create array for removed balls
      self.removed = []
      for i in range(num):
        #use random to choose a random index at which to to remove a ball
        remove_index = random.randint(0, (len(self.contents) - 1))
        self.removed.append(self.contents.pop(remove_index))
      return self.removed
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct = 0
    for i in range(num_experiments):
        #copy the class hat, so hat is not modified with each experiment - we draw from a new copy each time
        hat_copy = copy.deepcopy(hat)
        expected_balls_copy = copy.deepcopy(expected_balls)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        count = 0 
        for colour in balls_drawn:
          if colour in expected_balls_copy:
            expected_balls_copy[colour] -= 1 #remove 1 from expected balls colour if balls drawn colour matches
        for colour in expected_balls_copy.values():
          if colour <= 0:
            count +=1 #count each time the value of an expected colour reaches 0
        if count == len(expected_balls_copy):
          correct +=1 #if each colour has reached 0, this is a successful experiment
        
        
    probability = correct / num_experiments
  
    return probability
