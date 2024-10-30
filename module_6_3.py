class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance

    def get(self):
        print(f"x: {self.x_distance}")

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance

    def get(self):
        print(f"y: {self.y_distance}")

class Pegasus(Horse, Eagle):
    # pass

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        # pass
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)



# p1 = Pegasus()
# # h = Horse()
# # e = Eagle()
# p1.run(10)
# p1.fly(38)
# p1.get()
# # e.get()
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()