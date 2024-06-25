class LittleManComputer:
    
    def __init__(self) -> None:
        self.memory = [0] *100
        self.accumulator = 0
        self.pc = 0
        self.running = True
        self.instruction_set = {
            "add" : self.add,
            "sub" : self.sub,
            "sta" : self.store,
            "load" : self.load
        }