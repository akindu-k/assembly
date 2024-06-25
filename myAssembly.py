class LittleManComputer:
    
    def __init__(self) -> None:
        self.memory = [0] *100
        self.accumulator = 0
        self.pc = 0
        self.running = True
        self.instruction_set = {
           # 0 : self.halt,
            1 : self.add,
            2 : self.sub,
            3 : self.store,
            5 : self.load,
            6 : self.branch,
            7 : self.branch_if_zero,
            8 : self.branch_if_positive,
            9 : self.io_operations,
        }
    def load_program(self,program):
        for address,instruction in enumerate(program): #instruction eka 901 wage ewa
            self.memory[address] = instruction; #memory cell wala peliyata instruction tika damma
            
    def fetch(self):
        instruction = self.memory[self.pc]; #memory eken fetch kala 901 wage ins eka
        self.pc += 1; 
        return instruction;
    
    def decode(self,instruction): #opcode ekai operand ekai decode kala 901 awoth 9 | 01
        
        #tmp = str(instruction);
        #opcode = int(tmp[0]
        opcode = instruction // 100;            
        #operand = int(tmp[1:]);
        operand = instruction % 100;
        return opcode,operand;
    
    def execute(self,opcode,operand):
        if opcode in list(self.instruction_set.keys()):
            method = self.instruction_set[opcode];
            method(operand);
        else:
            print(f"Unknown opcode {opcode}");
            self.running = False;
    
    def add(self,operand):
        self.accumulator  = self.accumulator + self.memory[operand] #operand should always be a memory location
    
    def sub(self,operand):
        self.accumulator = self.accumulator - self.memory[operand];
    
    def store(self,operand):
        self.memory[operand] = self.accumulator;
    
    def load(self,operand):
        self.accumulator = self.memory[operand];
    
    def branch(self,operand):
        self.pc = operand;
    
    def branch_if_zero(self,operand):
        if (self.accumulator == 0):
            self.pc = operand;

    def branch_if_positive(self,operand):
        if (self.accumulator >= 0):
            self.pc = operand;
            
    def io_operations(self,operand):
        
        if (operand == 1):
            self.accumulator = int(input("Input: "));
        
        elif (operand == 2):
            self.accumulator = int(input("Input: "));
        
        else:
            print(f"Invalid operand {operand} for io_operations");
            self.running = False;
    
    #def halt(self,operand):
     #   if (operand == 0):
      #      self.running = False;
        
    def run(self):
        while(self.running):
            instruction = self.fetch();
            opcode , operand = self.decode(instruction);
            self.execute(opcode,operand);
        

        
    



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