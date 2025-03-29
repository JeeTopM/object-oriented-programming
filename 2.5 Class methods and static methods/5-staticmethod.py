"""
Лев создаёт программу для водителей. 
В ней вы указываете расстояние, которое планируете проехать, расход топлива на 100км вашей машины, цену на бензин в вашем регионе. 
Программа выводит на экран информацию о будущих финансовых расходах. Лев вероломно использует статический метод для подсчёта.
"""   
class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = distance * (fuel / 100) * price
        print(round(result, 2))

lev = Driver()
dist, fuel, price = [float(i) for i in input().split()]
lev.calculate_fuel_costs(dist, fuel, price)