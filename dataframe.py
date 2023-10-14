from HealthData import HealthData as hd
from PointsCalculator import PointsCalculator as pc
    
def main()->None:
    
    user = { 
            'Sleep' : pc(4).getPoints(),
            'Diet' : pc(4).getPoints(),
            'Exercise' : pc(4).getPoints()            
            }

    health = hd(user)
    health.add([1, 2, 3])
    print(health.getAvg('Sleep'))
    health.printDf()
    health.newCol("Avg Sleep", [health.getAvg('Sleep')])
    health.printDf()
    
    health.toCSV()
    
    
main()


