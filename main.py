
from ticket import Ticket

if __name__ == "__main__":
    while True:
        print("Timings: \nMorning  Afternoon  Evening")
        print("\n")
        print("Movies playing now: \nRRR Rocketry KGF-2")
        print("\n")
        userName = input("enter your name: ")
        userAge = int(input("enter your age: "))
        preferredTime = input("enter your preffered time: ").lower()
        preferredMovie = input("enter your preferred movie: ").lower()
        noOfTickets = int(input("enter the no of tickets you want: "))
        newTicket = Ticket(userName, userAge, preferredTime,
                           preferredMovie, noOfTickets)
        if newTicket.validateTicket(newTicket.prefferedTime, newTicket.preferredMovie, newTicket.noOfTickets):
            totalPrice = Ticket.calculatePrice(
                noOfTickets, newTicket.preferredMovie, newTicket.prefferedTime)
            print(f"total price: {totalPrice}")
        else:
            print("sorry tickets are sold out :(")
