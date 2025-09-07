class UndergroundSystem:

    def __init__(self):
        self.active_check_ins = { }

        '''
        id -> (station, check_in time)
        '''
        self.trips = { }

        '''
        (start_station, end_station) -> [time_delta0,time_delta1,...,time_deltan]
        '''

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.active_check_ins:
            raise ValueError('User is already checked in. Please checkout before trying to check in again')

        self.active_check_ins[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.active_check_ins:
            raise ValueError('User never checked in.')

        check_in_info = self.active_check_ins[id]
        del self.active_check_ins[id]
        trip_stations = (check_in_info[0], stationName)

        time_delta = t - check_in_info[1]

        if trip_stations in self.trips:
            self.trips[trip_stations].append(time_delta)
        else:
            self.trips[trip_stations] = [time_delta]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_deltas = self.trips[(startStation,endStation)]
        
        return sum(time_deltas)/len(time_deltas)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)