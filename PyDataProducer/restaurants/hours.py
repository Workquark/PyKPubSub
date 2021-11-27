from restaurants.day import Day

class Hours:
    monday: Day
    tuesday: Day
    wednesday: Day
    thursday: Day
    friday: Day
    saturday: Day
    sunday: Day

    def __init__(self, monday: Day, tuesday: Day, wednesday: Day, thursday: Day, friday: Day, saturday: Day, sunday: Day) -> None:
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
