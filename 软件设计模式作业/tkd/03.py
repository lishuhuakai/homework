from tkinter import *
from tkinter.font import *
import math

root = Tk()
root.minsize(750,502)
root.maxsize(750,502)
root.title("这是一段测试代码！")
#root.resizable(width=300, height=300)

def update_volumn_and_area(radius):
    global  string_volume, surface_area
    volume = round(radius * radius * radius * (4 / 3) * 3.1425, 2)
    surface_area = round(4 * 3.1415 * radius * radius, 2)
    string_volume.set(volume)
    string_area.set(surface_area)

def draw_with_radius(radius):
    global item, item2, item3
    canvas.delete(item)
    canvas.delete(item2)
    canvas.delete(item3)
    half_width = radius / 2
    item = canvas.create_oval(center[0] - radius, center[1] - radius,
                              center[0] + radius, center[1] + radius,
                              width=2)
    item2 = canvas.create_oval(center[0] - radius, center[1] - radius + half_width,
                              center[0] + radius, center[1] + radius - half_width,
                              width=2)
    item3 = canvas.create_oval(center[0] - radius + half_width, center[1] - radius,
                              center[0] + radius - half_width, center[1] + radius,
                              width=2)

def draw_circle(x, y):
    """
    这个函数的主要功能是画一个圆，应该不是很难，对吧！
    :return: null
    """
    global string_radius
    radius = round(math.sqrt((x - center[0]) * (x - center[0]) + (y - center[1]) * (y - center[1])), 2)
    string_radius.set(radius)
    update_volumn_and_area(radius)
    draw_with_radius(radius)

def handleInput(event):
    global string_radius
    radius = float(string_radius.get())
    draw_with_radius(radius)
    update_volumn_and_area(radius)

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    draw_circle(event.x, event.y)


frame = Frame(root, height = 180) # 框架什么的只是一个容器罢了。
label_font = Font(family='Monaco', size=12, weight='bold')

radius_frame = Frame(frame, height=30)
label_radius = Label(frame, text="radius =", font=label_font)
label_radius.grid(row=0, column=0, stick=S)
string_radius = StringVar(value="250.00")
entry_radius = Entry(frame, width=20, font=label_font, textvariable=string_radius) # The size of radius
entry_radius.grid(row=1, column=0, stick=W)


label_volume = Label(frame, text="Volume =", font=label_font)
label_volume.grid(row=2, column=0)
string_volume = StringVar()
label_volume_value = Label(frame,  font=label_font, textvariable=string_volume)
label_volume_value.grid(row=3, column=0, stick=W)

label_area = Label(frame, text="Surface Area =", font=label_font)
label_area.grid(row=4, column=0)
string_area = StringVar()
label_area_value = Label(frame, font=label_font, textvariable=string_area)
label_area_value.grid(row=5, column=0, stick=W)

update_volumn_and_area(250.00)

entry_radius.bind('<Return>', handleInput)

frame.grid(row = 0,column = 1, stick = W)
canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height)
center = (canvas_height/2, canvas_width/2) # 好吧，这就是圆心

item = canvas.create_oval(2, 2, canvas_width, canvas_height, width=2, outline='red')
item2 = canvas.create_oval(2, 152, canvas_width, canvas_height-152,
                           outline='blue', width=2)
item3 = canvas.create_oval(152, 2, canvas_width - 152, canvas_height,
                           outline='green', width=2)
canvas.bind("<B1-Motion>", callback)
canvas.grid(row=0, column = 2, stick=W)

root.mainloop()