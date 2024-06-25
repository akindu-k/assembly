class LittleManComputer:
    def __init__(self):
        self.memory = [0] * 100  # Memory with 100 locations
        self.accumulator = 0  # Accumulator
        self.pc = 0  # Program counter
        self.running = True  # Running state
        self.instruction_set = {
            1: self.add,
            2: self.sub,
            3: self.store,
            5: self.load,
            6: self.branch,
            7: self.branch_if_zero,
            8: self.branch_if_positive,
            9: self.io_operations
        }

    def load_program(self, program):
        for address, instruction in enumerate(program):
            print(address,instruction)
            self.memory[address] = instruction

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100
        return opcode, operand

    def execute(self, opcode, operand):
        if opcode in self.instruction_set:
            self.instruction_set[opcode](operand)
        else:
            print(f"Unknown opcode: {opcode}")
            self.running = False

    def add(self, operand):
        self.accumulator += self.memory[operand]

    def sub(self, operand):
        self.accumulator -= self.memory[operand]

    def store(self, operand):
        self.memory[operand] = self.accumulator

    def load(self, operand):
        self.accumulator = self.memory[operand]

    def branch(self, operand):
        self.pc = operand

    def branch_if_zero(self, operand):
        if self.accumulator == 0:
            self.pc = operand

    def branch_if_positive(self, operand):
        if self.accumulator >= 0:
            self.pc = operand

    def io_operations(self, operand):
        if operand == 1:
            self.accumulator = int(input("Enter a number: "))
        elif operand == 2:
            print(f"Output: {self.accumulator}")

    def run(self):
        while self.running:
            instruction = self.fetch()
            opcode, operand = self.decode(instruction)
            self.execute(opcode, operand)

    

# Example program to load into LMC (add two numbers)
program = [
    901,  # IN
    308,  # STO 8
    901,  # IN
    309,  # STO 9
    508,  # LDA 8
    109,  # ADD 9
    902,  # OUT
    000   # HLT
]

lmc = LittleManComputer()
lmc.load_program(program)
lmc.run()
