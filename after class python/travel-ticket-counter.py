passenger_name= "Anna"
destination= "Italy"
ticket_price= 980.00
number_of_tickets= 2
is_available= True

print("Passenger Name:",passenger_name)
print("Destination:",destination)
print("Ticket price:",ticket_price)
print("Number of tickets",number_of_tickets)
print("Availability:",is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

#ARTHIMETIC OPERATIONS

total_cost = ticket_price * number_of_tickets
discount= 100
final_cost= total_cost - discount

print("Total cost:", total_cost)
print("Discount given:", discount)
print("Final cost:", final_cost)

print("Double ticket price:",ticket_price*2)
print("Ticket price after 50rs added:", ticket_price+50)
print("Half ticket price:",ticket_price/2)

#COMPARISON OPERATORS

print("Is the ticket price under than Rs700?", ticket_price<700)
print("Is the destination Italy?",destination=="Italy")
print("Are two tickets booked?", number_of_tickets ==2 )
print("Is the final price more than Rs2000", final_cost>2000)

#STRING OPERATIONS
message= passenger_name + " is travelling to " + destination + "."
print(message)
print("destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("Second letter of destination:", destination[1])
print("Length of passenger name:", len(passenger_name))

#SWAPPING VALUES
morning_ticket= 560
evening_ticket= 780
print("Prices before swapping")
print("Morning ticket price:", morning_ticket)
print("Evening ticket price:", evening_ticket)

temp= morning_ticket
morning_ticket= evening_ticket
evening_ticket= temp
print("After swapping")
print("Morning ticket price:", morning_ticket)
print("Evening ticket price:", evening_ticket)

#SUMMARY
print("TICKET BOOKING SUMMARY")
print("Passenger Name:",passenger_name)
print("Destination:",destination)
print("Final amount to pay: Rs",final_cost)
print("Number of tickets booked:",number_of_tickets)
print("Booking confirmed?",is_available)
