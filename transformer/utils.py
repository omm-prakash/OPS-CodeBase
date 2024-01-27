import time, datetime

class Time():
    def __init__(self):
        self.begin = 0
        self.final = 0
    def now(self):
        return datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    def reset(self):
        self.begin = time.time()
        self.final = time.time()        
    def start(self, message=None):
        if message:
            self.message = message
        self.begin = time.time()
    def end(self):
        self.final = time.time()
        tm = float(self.final-self.begin)
        unit = 'sec'
        if tm > 60:
            tm = tm/60
            unit = 'min'
        elif tm > 3600:
            tm = tm/3600
            unit = 'hr'
        if self.message:
            print('\n>> {}: Done!! Time taken: {:.4f} {}'.format(self.message, tm, unit))
        else:
            print('\n>> Done!! Time taken: {:.4f} {}'.format(tm, unit))
        self.message = None
