# IT Help Desk Ticket Analyzer

filename = "helpdesk_tickets.txt"

total_tickets = 0
categories = {}
priorities = {}
statuses = {}
open_tickets = []
urgent_tickets = []

# Read the help desk tickets
file = open(filename, "r")

for line in file:
    line = line.strip()

    if line != "":
        total_tickets = total_tickets + 1

        parts = line.split(" | ")

        ticket_id = parts[0]
        category = parts[1].replace("Category: ", "")
        priority = parts[2].replace("Priority: ", "")
        status = parts[3].replace("Status: ", "")

        # Count tickets by category
        if category in categories:
            categories[category] = categories[category] + 1
        else:
            categories[category] = 1

        # Count tickets by priority
        if priority in priorities:
            priorities[priority] = priorities[priority] + 1
        else:
            priorities[priority] = 1

        # Count tickets by status
        if status in statuses:
            statuses[status] = statuses[status] + 1
        else:
            statuses[status] = 1

        # Save open tickets
        if status == "Open":
            open_tickets.append(line)

        # Identify urgent unresolved tickets
        if priority == "High" and status == "Open":
            urgent_tickets.append(line)

file.close()

# Save open tickets to a separate file
file = open("open_tickets.txt", "w")

for ticket in open_tickets:
    file.write(ticket + "\n")

file.close()

# Display the report
print("IT HELP DESK TICKET ANALYZER")
print("----------------------------")

print("Total tickets:", total_tickets)

print("\nTickets by category:")
for category in categories:
    print(category + ":", categories[category])

print("\nTickets by priority:")
for priority in priorities:
    print(priority + ":", priorities[priority])

print("\nTickets by status:")
for status in statuses:
    print(status + ":", statuses[status])

print("\nHigh-priority open tickets:", len(urgent_tickets))

for ticket in urgent_tickets:
    print(ticket)

print("\nOpen tickets saved to open_tickets.txt")
