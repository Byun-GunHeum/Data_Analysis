'''
    @classmethod
    def from_string(cls,time_string):
        hour,minute,second=map(int,time_string.split(':'))
        time=cls(hour,minute,second)
        return time
 
    @staticmethod
    def is_time_valid(time_string):
        hour,minute,second=map(int,time_string.split(':'))
        return hour<=24 and minute<=59 and second<=60
'''