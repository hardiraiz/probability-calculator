# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
import copy
from unittest import main


# prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "green": 1},
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)

hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print("Probability:", probability)


# balls = {"blue": 2, "green": 1}
# a = [True, False]
# if False in a and len(a) == len(balls):
#     print("fack")
# b = copy.deepcopy(hat.draw(5))
# c = copy.deepcopy(hat.contents)
# b = dict((i, c.count(i)) for i in c)
# print(b)

# Run unit tests automatically
main(module='test_module', exit=False)
