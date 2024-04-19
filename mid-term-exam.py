# answer 1
class Star_Cinema:
    hall_list = [] 
    def entry_hall(self, newHall): 
        self.hall_list.append(newHall)

# answer 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = [] # list of touples [(id, movie_name, time),(id, movie_name, time)]
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)
# answer 3
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]
# answer 4
    def book_ticket(self, show_id, seat_list):
        if show_id in self.__seats:
            for row, col in seat_list:
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.__seats[show_id][row][col] == 'free':
                        self.__seats[show_id][row][col] = 'booked'
                    else:
                        print(f"Seat at row {row} and col {col} is already booked.")
                else:
                    print(f"Invalid seat coordinates: row {row}, col {col}.")
        else:
            print(f"No show found with ID: {show_id}")
# answer 5
    def view_show_list(self):
        for id, movie_name, time in self.__show_list:
            print(f"Show ID: {id}, Movie Name: {movie_name}, Time: {time}")

# answer 6
    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            print(f"Available seats for show ID {show_id}:")
            for row_index, row in enumerate(self.__seats[show_id]):
                for col_index, seat in enumerate(row):
                    if seat == 'free':
                        print(f"Row: {row_index}, Col: {col_index}")
        else:
            print(f"No show found with ID: {show_id}")


# extra
hall1 = Hall(rows=30, cols=15, hall_no=1)
hall1.entry_show(id='111', movie_name='Jawan', time='18:00')
hall1.entry_show(id='222', movie_name='Pathan', time='12:00')
seats_to_jawan = [(1, 1), (1, 3), (1, 5)]
hall1.book_ticket('111', seats_to_jawan)
seats_to_pathan = [(1, 4), (1, 6), (1, 3)]
hall1.book_ticket('111', seats_to_pathan)

# answer 7
while True:
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")
    option = input("Enter Option: ")

    if option == "1":

        hall1.view_show_list()

    elif option == "2":
        show_id = input("Enter Show ID: ")
        hall1.view_available_seats(show_id)
    elif option == "3":
       show_id = input("Enter Show ID: ")
       seats = input("Enter seats to book (demo like: row,col  '1,2 2,3'): ")
       seat_list = [tuple(map(int, seat.split(','))) for seat in seats.split()]
       hall1.book_ticket(show_id, seat_list)
    elif option == "4":
        break
    else:
        print("Invalid option. Please choose again.")