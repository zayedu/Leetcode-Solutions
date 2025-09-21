class UndergroundSystem:

    def __init__(self):
        self.trips = { }
        '''
        (start_station, end_station) -> (time_sum, time_observations)
        '''
        self.check_ins = { }
        '''
        id -> (station,check_in_time)
        '''
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        if id in self.check_ins:
            raise ValueError("You must check out prior to checking back in")
        
        self.check_ins[id] = (stationName,t)        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_ins:
            raise ValueError('Please check in before trying to check out.')

        start_station,start_time = self.check_ins[id]

        trip_id = (start_station,stationName)

        if trip_id in self.trips:
            self.trips[trip_id] = (self.trips[trip_id][0]+(t-start_time),self.trips[trip_id][1]+1)
        else:
            self.trips[trip_id] = (t-start_time,1)

        del self.check_ins[id]
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, observations = self.trips.get((startStation,endStation))

        return total_time/observations
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)