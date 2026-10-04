class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        counter=0
        fleet_time=0
        for pos, speed in cars:
            time = (target-pos)/speed
            if time > fleet_time:
                fleet_time = time
                counter+=1
        return counter
    