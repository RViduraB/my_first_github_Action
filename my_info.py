import datetime as time

class Me:

    def name(self):
        return "Vidura Bandara"

    def age(self):
        birth_year = 1996
        current_year = time.datetime.now().year
        return current_year - birth_year

    def display_info(self):
        print(f"*******************************************")
        print(f"**      Name: {self.name()}                     **")
        print(f"**      Age: {self.age()}                          **")
        print(f"*******************************************")

    def message(self):
        # first Automation Execution
        first_execution_date = time.date(2026, 7, 27)
        today_date = time.date.today()

        # age gap
        days_passed = (today_date - first_execution_date).days
        years_passed = days_passed // 365
        remaining_days = days_passed % 365

        # for ages , days and time
        if years_passed > 0:
            time_msg = f"It has been {years_passed} year(s) and {remaining_days} day(s) since the first execution."
        else:
            time_msg = f"It has been {days_passed} day(s) since the first execution."

        msg = f">>>My first GitHub Action workflow is successfully executed!<<<\n >>>From: {self.name()}<<< \n >>>Status: {time_msg}<<<"
        return msg

    def run(self):
        self.display_info()
        print(self.message())



if __name__ == "__main__":
    me = Me()
    me.run()