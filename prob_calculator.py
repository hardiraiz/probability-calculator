import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = list()

    def __repr__(self):
        return "Hat()"

    def __str__(self) -> str:
        return "Content:{}".format(self.contents)

    def __init__(self, **kwargs):
        if kwargs:
            contents = list()
            for key, value in kwargs.items():
                contents += value * [key]
            self.contents = contents
    
    def draw(self, num):
        # if num is not None and len(self.contents) >= num:
        if len(self.contents) > num:
            draw_list = list()
            while num > 0:
                random_choice = random.choice(self.contents)
                draw_list.append(random_choice)
                self.contents.remove(random_choice)
                num -= 1
            return draw_list
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = int()
    count_match = int()
    hat_copy = copy.deepcopy(hat)
    while num_experiments > count:
        draw = hat_copy.draw(num_balls_drawn)
        draw = dict((i, draw.count(i)) for i in draw)
        match = list()
        for k, v in expected_balls.items():
            try:
                if expected_balls[k] <= draw[k]:
                    match.append(True)
            except KeyError:
                break
        if False not in match and len(match) == len(expected_balls):
            count_match += 1
        # print("Draw:", draw)
        count += 1
        hat_copy = copy.deepcopy(hat)

    return count_match/num_experiments
