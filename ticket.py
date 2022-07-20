

class Ticket:
    morningTickets = [6, 6, 6]
    afternoonTickets = [6, 6, 6]
    eveningTickets = [6, 6, 6]
    ticketsRate = [200, 250, 200]
    totalEarnings = 0

    def __init__(self, name: str, age: int, preferredTime: str, preferredMovie: str, num: int):
        assert age > 0, "age cannot be negative or zero"
        assert num > 0, "no of tickets cannot be negative or zero"
        self.name = name
        self.age = age
        self.prefferedTime = preferredTime
        self.preferredMovie = preferredMovie
        self.noOfTickets = num

    def printDetails(self):
        print(
            f"name: {self.name}\nage: {self.age}\nprefferedTime: {self.prefferedTime}\npreferredMovie: {self.preferredMovie}")

    @classmethod
    def validateTicket(cls, preferredTime: str, preferrefMoive: str, noOfTickets: int) -> bool:
        if preferredTime == "morning":
            if preferrefMoive == "rrr":
                if cls.morningTickets[0] >= noOfTickets:
                    return True
                return False
            elif preferrefMoive == "rocketry":
                if cls.morningTickets[1] >= noOfTickets:
                    return True
                return False
            else:
                if cls.morningTickets[2] >= noOfTickets:
                    return True
                return False
        elif preferredTime == "evening":
            if preferrefMoive == "rrr":
                if cls.afternoonTickets[0] >= noOfTickets:
                    return True
                return False
            elif preferrefMoive == "rocketry":
                if cls.afternoonTickets[1] >= noOfTickets:
                    return True
                return False
            else:
                if cls.afternoonTickets[2] >= noOfTickets:
                    return True
                return False
        else:
            if preferrefMoive == "rrr":
                if cls.eveningTickets[0] >= noOfTickets:
                    return True
                return False
            elif preferrefMoive == "rocketry":
                if cls.eveningTickets[1] >= noOfTickets:
                    return True
                return False
            else:
                if cls.eveningTickets[2] >= noOfTickets:
                    return True
                return False

    @classmethod
    def calculatePrice(cls, num: int, preferrefMoive: str, preferredTime: str) -> int:
        if preferredTime == "morning":
            if preferrefMoive == "rrr":
                cls.morningTickets[0] -= num
                cls.totalEarnings += cls.ticketsRate[0] * num
                return cls.ticketsRate[0] * num
            elif preferrefMoive == "rocketry":
                cls.morningTickets[1] -= num
                cls.totalEarnings += cls.ticketsRate[1] * num
                return cls.ticketsRate[1] * num
            else:
                cls.morningTickets[2] -= num
                cls.totalEarnings += cls.ticketsRate[2]*num
                return cls.ticketsRate[2]*num
        elif preferredTime == "evening":
            if preferrefMoive == "rrr":
                cls.afternoonTickets[0] -= num
                cls.totalEarnings += cls.ticketsRate[0] * num
                return cls.ticketsRate[0] * num
            elif preferrefMoive == "rocketry":
                cls.afternoonTickets[1] -= num
                cls.totalEarnings += cls.ticketsRate[1] * num
                return cls.ticketsRate[1] * num
            else:
                cls.afternoonTickets[2] -= num
                cls.totalEarnings += cls.ticketsRate[2]*num
                return cls.ticketsRate[2]*num
        else:
            if preferrefMoive == "rrr":
                cls.eveningTickets[0] -= num
                cls.totalEarnings += cls.ticketsRate[0] * num
                return cls.ticketsRate[0] * num
            elif preferrefMoive == "rocketry":
                cls.eveningTickets[1] -= num
                cls.totalEarnings += cls.ticketsRate[1] * num
                return cls.ticketsRate[1] * num
            else:
                cls.eveningTickets[2] -= num
                cls.totalEarnings += cls.ticketsRate[2]*num
                return cls.ticketsRate[2]*num

    @classmethod
    def printTotalEarnings(cls):
        print(f"total eanings till now: {cls.totalEarnings}")
