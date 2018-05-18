import random as r
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
legal_x = [0,10]
legal_y = [0,10]
list_boom = []
class Big:
    def __init__(self):
        """在y=1随机生成轰炸机位置"""
        self.x = r.randint(0,10)
        self.y = 1

    def move(self):
        self.Interval = []
        """随机移动左右方向并移动到新的位置(x,1)"""
        self.step = r.randint(0,10)
        self.direction = r.randint(-1,1)#方向，-1为左，0不移动，1为右
        new_x = self.x + self.direction * self.step
        mew_y = self.y
        """判断是否越界"""
        if new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
            pos_y = mew_y
        elif new_x < legal_x[0]:
            pos_x = legal_x[0] - new_x
            pos_y = mew_y
        else:
            pos_x = new_x
            pos_y = mew_y

        """炮台移动前后对应坐标"""
        if self.x > pos_x:
            for i in range(pos_x,self.x + 1 ):
                self.Interval.append(i)
            print("炮台从坐标x=%d移动到x=%d，沿途轰了%d炮"%(self.x,pos_x,self.x + 1 -pos_x ))
            print(">>>轰出%d个炮的位置是x ="% (self.x + 1 -pos_x),end = "")
            print(self.Interval)

        elif self.x < pos_x:
            for i in range(self.x,pos_x + 1):
                self.Interval.append(i)
            print("炮台从坐标x=%d移动到x=%d，沿途轰了%d炮"%(self.x,pos_x,pos_x + 1 -self.x ))
            print(">>>轰出%d个炮的位置是x ="% (pos_x + 1 -self.x),end = "")
            print(self.Interval)
        else:
            self.Interval.append(pos_x)
            print(">>>炮台原地轰了一炮")
            print(">>>轰炮的坐标是x = %s"% str(self.Interval))

        """初始化炮台到移动的目标"""
        self.x = pos_x
        self.y = pos_y
        return (pos_x,pos_y)

class Small:
    def __init__(self):
        """在y=10随机生成小飞机位置"""
        self.x = r.randint(0,10)
        self.y = 10

    def move(self):
        """固定移动，每次向下一步"""
        new_x = self.x
        mew_y = self.y - 1
        """判断是否越界"""
        if mew_y <= legal_y[0]:
            self.x = r.randint(0,10)
            self.y = 10
        else:
            self.x = new_x
            self.y = mew_y            
        return (new_x , mew_y)

class Boom:
    """核武器"""
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = 1

def DAFEIJI(n):  
    Scorer = 0
    list_s = []
    big_air = Big()
    """炮台出场"""

    i = r.randint(3,10)
    while n:
        boom = Boom()
        """核武器生成"""       
        for each_air in range(i):
            small_air = Small()#小飞机出场数量随机生成，位置也随机，所以可能与之前重叠
            list_s.append(small_air)

        pos = big_air.move()
        n = n - 1
        if pos != (boom.x ,boom.y):
            for each in list_s[:]:
                if each.move() == pos:
                    print(">>>>>>>很不幸! 您的炮台撞小飞机了....GG！！")#这个几率.....
                    print("本次打飞机的分数是：%d" % Scorer)
                    sys.exit(0)          
                if(each.move())[0] in (big_air.Interval):
                    print("一架小飞机被打掉..")
                    Scorer += 1
                    list_s.remove(each)
        else:
            print("炮台加载了核武器...======================清屏!=======================..")
            Scorer += len(list_s)
            list_s.clear()
    print("本次打飞机的分数是：%d" % Scorer)
#==============================主程序==================================    
DAFEIJI(2000)