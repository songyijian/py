#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 类继承 class
# new 实体|实例 instance


# class Gongfu:
#     def __init__(self, name):
#         self.name = name
#     def go(self):
#         return f'{self.name} > 动动手指就能杀人'

# class Xixingdafa(Gongfu):
#     # super() 来调用上面类的方法、属性
    
#     def __init__(self, name,daixia):
#         super().__init__(name) # 重新复写类的初始化方法，把参数传进去
#         self.daixia = daixia

#     def douzhuanxingyi(self):
#         return f"{self.daixia}的 > 斗转星移还给你：{super().go()}"



# a = Xixingdafa("六脉神剑",'鸭子')
# print(
#     a.go(),  # 六脉神剑 > 动动手指就能杀人
#     "\n",
#     a.douzhuanxingyi()  # 鸭子的 > 斗转星移：六脉神剑 > 动动手指就能杀人
# )


class Gongfu:
    def __init__(self, name):
        self.name = name

    def go(self):
        return f'{self.name} > 动动手指就能杀人'


class Anqi:
    def __init__(self, anqi):
        self.anqi = anqi

    def zouni(self):
        return f'{self.anqi} > 暗器不长眼'




class Xixingdafa(Gongfu, Anqi):
    # super() 来调用上面类的方法、属性

    def __init__(self, name, daixia):
        super().__init__(name)  # 重新复写类的初始化方法，把参数传进去
        self.daixia = daixia

    def douzhuanxingyi(self):
        return f"{self.daixia}的 > 斗转星移还给你：{super(Gongfu).go()}"


a = Xixingdafa("六脉神剑", '鸭子')
print(
    a.go(),  # 六脉神剑 > 动动手指就能杀人
    "\n",
    a.douzhuanxingyi()  # 鸭子的 > 斗转星移：六脉神剑 > 动动手指就能杀人
)
