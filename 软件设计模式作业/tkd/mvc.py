# 用MVC的形式实现
from tkinter import *
from tkinter.font import *
from tkinter.messagebox import showerror
import math
import functools

root = Tk()
root.minsize(750,502)
root.maxsize(750,502)
root.title("MVC！")

class GraphicsView:
    canvas_height = 500
    canvas_width = 500
    center=(canvas_height / 2, canvas_width / 2)

    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.registerObserver(self) # 注册成为观察者
        self.create_canvas()
        self.create_ovals()

    def create_canvas(self):
        self.__canvas = Canvas(root, width=GraphicsView.canvas_width, height=GraphicsView.canvas_height)
        self.__canvas.grid(row=0, column = 2, stick=W) # 构建一块画布
        self.__canvas.bind("<B1-Motion>",
                         functools.partial(GraphicsView.callback, view=self)) # 注册回调函数

    @staticmethod
    def callback(event, view):
        """回调函数,当鼠标在画布上移动的时候会调用这个函数,我们调用controller的setRadius方法"""
        x = event.x
        y = event.y
        # 下面是用于计算出半径
        radius = round(math.sqrt((x - GraphicsView.center[0]) * (x - GraphicsView.center[0]) +
                                 (y - GraphicsView.center[1]) * (y - GraphicsView.center[1])), 2)
        # 也就是说，现在半径发生了改变,我们应该怎么玩呢？
        view.__controller.setRadius(radius)

    def create_ovals(self):
        """这个函数主要用于绘制所有的椭圆"""
        self.__item1 = self.__canvas.create_oval(2, 2, self.canvas_width,
                                  self.canvas_height, width=2)
        self.__item2 = self.__canvas.create_oval(2, 152, self.canvas_width,
                                        self.canvas_height-152, width=2)
        self.__item3 = self.__canvas.create_oval(152, 2, self.canvas_width - 152,
                                        self.canvas_height, width=2)

    def draw_with_radius(self, radius):
        """通过圆心和半径来画圆"""
        self.__canvas.delete(self.__item1)
        self.__canvas.delete(self.__item2)
        self.__canvas.delete(self.__item3)
        half_width = radius / 2
        self.__item1 = self.__canvas.create_oval(GraphicsView.center[0] - radius, GraphicsView.center[1] - radius,
                                  GraphicsView.center[0] + radius, GraphicsView.center[1] + radius,
                                  width=2)
        self.__item2 = self.__canvas.create_oval(GraphicsView.center[0] - radius, GraphicsView.center[1] - radius + half_width,
                                  GraphicsView.center[0] + radius, GraphicsView.center[1] + radius - half_width,
                                  width=2)
        self.__item3 = self.__canvas.create_oval(GraphicsView.center[0] - radius + half_width, GraphicsView.center[1] - radius,
                                  GraphicsView.center[0] + radius - half_width, GraphicsView.center[1] + radius,
                                  width=2)
    def updateView(self):
        # 获取半径和圆心的消息
        radius = self.__model.getRadius()
        # 重新绘制图形
        self.draw_with_radius(radius)

class TextView:
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.registerObserver(self) # 将这个view注册成为观察者
        self.createView()

    @staticmethod
    def callback(event, view):
        # 一旦发生了这种事情，怎么办呢？
        try:
            radius = float(view.__string_radius.get())
        except ValueError:
            showerror(title="错误", message="输入值包含非数字", parent=root) # 代码不能包含非数字
            view.updateView()
        else:
            if radius < 0:
                showerror(title="错误", message="不合法的值", parent=root) # 不能允许输入负值
                view.updateView()
            else:
                view.__controller.setRadius(radius)

    @staticmethod
    def calc_self_area(radius):
        """计算球体的表面积"""
        return 4 * 3.14 * math.pow(radius, 2)

    @staticmethod
    def calc_volumn(radius):
        """计算球体的体积"""
        return (4 / 3) * 3.14 * math.pow(radius, 3)


    def createView(self):
        """用于创建view"""
        self.__frame = Frame(root, height = 180) # 框架什么的只是一个容器罢了。
        self.label_font = Font(family='Monaco', size=12, weight='bold')
        self.__frame.grid(row = 0,column = 1, stick = W)
        # 关于radius的输入框和label
        self.__radius_frame = Frame(self.__frame, height=30)
        self.__label_radius = Label(self.__frame, text="radius =", font=self.label_font)
        self.__label_radius.grid(row=0, column=0, stick=S)
        self.__string_radius = StringVar(value="250.00")
        self.__entry_radius = Entry(self.__frame, width=20, font=self.label_font,
                                  textvariable=self.__string_radius) # The size of radius
        self.__entry_radius.grid(row=1, column=0, stick=W)
        self.__entry_radius.bind('<Return>',
                               functools.partial(TextView.callback, view=self))


        # 关于volume的label
        self.__label_volume = Label(self.__frame, text="Volume =", font=self.label_font)
        self.__label_volume.grid(row=2, column=0)
        self.__string_volume = StringVar()
        self.__label_volume_value = Label(self.__frame,  font=self.label_font,
                                   textvariable=self.__string_volume)
        self.__label_volume_value.grid(row=3, column=0, stick=W)
        # 关于surface_area的label
        self.__label_area = Label(self.__frame, text="Surface Area =", font=self.label_font)
        self.__label_area.grid(row=4, column=0)
        self.__string_area = StringVar()
        self.__label_area_value = Label(self.__frame, font=self.label_font,
                                      textvariable=self.__string_area)
        self.__label_area_value.grid(row=5, column=0, stick=W)

    def update_volume_and_surface_area(self, radius):
        """这个函数主要用于更新volume和surface_area的值"""
        volume = round(TextView.calc_volumn(radius), 2)
        surface_area = round(TextView.calc_self_area(radius), 2)
        self.__string_radius.set(radius)
        self.__string_volume.set(volume)
        self.__string_area.set(surface_area)

    def getRadius(self):
        self.__string_radius.get() # 得到输入框内的radius的值

    def updateView(self):
        radius = self.__model.getRadius() # 获取半径的信息
        self.update_volume_and_surface_area(radius)

class TextController:
    def __init__(self, model):
        self.__model = model
        self.__text_view = TextView(self, model) # 初始化的时候创建view
        self.__text_view.updateView()

    def setRadius(self, radius):
        self.__model.setRadius(radius)

class GraphicsController:
    def __init__(self, model): # controller的话，只需要model就行了
        self.__model = model
        self.__graphics_view = GraphicsView(self, model)
        self.__graphics_view.updateView() # 初始化圆

    def setRadius(self, radius):
        self.__model.setRadius(radius) # 更新model，然后model变化之后view也会相对应的变化

class Model:
    def __init__(self, radius=200):
        self.__observer = [] # 这是一个list吧！
        self.__radius = radius

    def registerObserver(self, a_observer):
        self.__observer.append(a_observer) # 添加观察者

    def setRadius(self, radius):
        self.__radius = radius
        self.notifyObserver()

    def getRadius(self):
        return self.__radius

    def notifyObserver(self):
        for eachObserver in self.__observer:
            eachObserver.updateView() # 我们要通知每一个观察者

if __name__ == "__main__":
    s_model = Model() # 创建一个Model
    s_text_control = TextController(s_model) # 创建一个TextController
    s_graphic_controller = GraphicsController(s_model) # 创建一个GraphicsController
    root.mainloop()


