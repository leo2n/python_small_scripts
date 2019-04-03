import random


class RedPacket:
    def __init__(self):
        pass

    def redPacket(self, money:int, people:int):
        """
        money 单位为分, people 最小单位为1
        """
        if money // people == 0:
            return False
        pointsAll = [i for i in range(1, money)]
        points = random.sample(pointsAll, people-1)
        points.sort()
        def lines(points:list, money:int):
            points2 = [] # 线段的长度的list
            pointsLen = len(points)
            for i in range(pointsLen-1):
                points2.append(points[i+1] - points[i])
            points2.insert(0, points[0])
            points2.append(money-points[-1])
            return points2
        result = lines(points, money)
        print([str(i/100)+"元" for i in result])


if __name__ == "__main__":
    r = RedPacket()
    r.redPacket(1788, 16)

        
        
        
        