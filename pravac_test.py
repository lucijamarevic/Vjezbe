import matplotlib.pyplot as plt
import pravac as p

p1 = p.line()

p1.init(2,2,3,3)
p1.find_the_equation()
plt.title("pravac 1")
p1.plot_the_line(0,5)
p1.does_it_pass(6,6)
p1.does_it_pass(3,2)
p1.reset()

p2 = p.line()

p2.init(2,4,5,2)
p2.find_the_equation()
plt.title("pravac 2")
p2.plot_the_line(0,3)
p2.does_it_pass(6,6)