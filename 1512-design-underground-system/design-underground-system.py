class UndergroundSystem:

    def __init__(self):
        self.trips = {}
        '''
        self.trips should look like:
            (startStation,endStation) -> [sum_of_all_times,trips]
        '''

        self.check_ins = {}

        '''
        self.check_ins should look like:
            id -> (checkIn_station,checkIn_time)
        '''
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_ins:
            raise ValueError("Please check out before you try checking in again.")
        
        self.check_ins[id] = (stationName,t) 


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_ins:
            raise ValueError("Please check in before you try checking in again.")

        check_in_station, check_in_time = self.check_ins[id]
        del self.check_ins[id]
        trip = (check_in_station,stationName)

        if trip in self.trips:
            self.trips[trip][0] += t-check_in_time
            self.trips[trip][1] += 1
        else:
            self.trips[trip] = [t-check_in_time,1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum_times, trips = self.trips.get((startStation,endStation),[0,0])
        avg_time = sum_times/trips
        return avg_time


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)