'''Tkinter教程之Canvas篇(1)'''
# 提供可以用来进行绘图的Container，支持基本的几何元素，使用Canvas进行绘图时，所有的操作都是通过Canvas，不是通过它的元素
# 元素的表示可以使用handle或tag。
'''1.第一个Canvas程序'''
# -*- coding: cp936 -*-
# 指定画布的颜色为白色
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.pack()
#root.mainloop()
# 为明显起见，将背景色设置为白色，用以区别root

'''2.创建一个item'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的颜色为白色
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
# 创建一个矩形，坐标为(10,10,110,110)
#cv.create_rectangle(10,10,110,110)
#cv.pack()
#root.mainloop()
# 为明显起见，将背景色设置为白色，用以区别root
'''3.指定item的填充色'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的背景色为白色
# 使用属性fill设置它的填充颜色
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.create_rectangle(10,10,110,110,fill = 'red')
#cv.pack()
#root.mainloop()
# 指定矩形的填充色为红色
'''4.指定item的边框颜色'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的背景色为白色
# 使用属性outline设置它的边框颜色
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.create_rectangle(10,10,110,110,outline = 'red')
#cv.pack()
#root.mainloop()
# 指定矩形的边框颜色为红色
'''5.指定边框的宽度'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性width指定线的宽度
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.create_rectangle(10,10,110,110,outline = 'red',width = 5)
#cv.pack()
#root.mainloop()
# 指定矩形的边框颜色为红色，设置线宽为5，注意与Canvas的width是不同的。
'''6.画虚线'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性dash,这个值只能为奇数
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.create_rectangle(10,10,110,110,
#                    outline = 'red',
#                    dash = 10,
#                    fill = 'green')
#cv.pack()
#root.mainloop()
# 指定矩形的边框颜色为红色,画虚线
'''7.使用画刷填充'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性stipple
#from tkinter import *
#root = Tk()
# 创建一个Canvas，设置其背景色为白色
#cv = Canvas(root,bg = 'white')
#cv.create_rectangle(10,10,110,110,
#                    outline = 'red',
#                    stipple = 'gray12',
#                    fill = 'green')
#cv.pack()
#root.mainloop()
# 指定矩形的边框颜色为红色,自定义画刷
'''8.修改item的坐标'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用Canvas的方法来重新设置item的坐标
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
rt = cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    stipple = 'gray12',
                    fill = 'green')
cv.pack()
# 重新设置rt的坐标（相当于移动一个item）
cv.coords(rt,(40,40,80,80))
root.mainloop()
# 动态修改item的坐标