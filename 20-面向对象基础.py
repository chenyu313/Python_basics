class SweetPotato():
    #魔法⽅法
    #在Python中， __xx__() 的函数叫做魔法⽅法，指的是具有特殊功能的函数。
    #__init__() ⽅法的作⽤：初始化对象。
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地⽠的状态
        self.cook_static = '⽣的'
        # 调料列表
        self.condiments = []

    #定义烤地⽠⽅法
    def cook(self, time):
        """烤地⽠的⽅法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '⽣的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半⽣不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    #如果类定义了 __str__ ⽅法，那么就会打印从在这个⽅法中 return 的数据。
    def __str__(self):
        return f'这个地⽠烤了{self.cook_time}分钟, 状态是{self.cook_static}'

#创建对象，测试实例属性和实例⽅法
digua1 = SweetPotato()
print(digua1)
digua1.cook(5)
print(digua1)