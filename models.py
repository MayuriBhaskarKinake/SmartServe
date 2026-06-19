class Booking:

    def __init__(self, bookings):
        self.bookings = bookings

    def __add__(self, other):
        return self.bookings + other.bookings


# Demo
if __name__ == "__main__":
    b1 = Booking(5)
    b2 = Booking(3)

    print("Total Bookings:", b1 + b2)