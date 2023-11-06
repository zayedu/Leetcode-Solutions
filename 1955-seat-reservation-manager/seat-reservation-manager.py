class SeatManager:

    def __init__(self, n: int):
        self.seats=[1]
        

    def reserve(self) -> int:
        reserved_seat=heapq.heappop(self.seats)
        if not self.seats:
            self.seats.append(reserved_seat+1)
        return reserved_seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)