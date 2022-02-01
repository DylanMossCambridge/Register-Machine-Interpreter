TRACE = True
f = open("input.txt", "r")

#(R0, R1, R2....)
register_states = [0] + list(map(lambda x: int(x), f.readline()[1:-2].split(", ")))

#{instruction_label : instruction_code} eg. {"0": "inc(r0), 1", ...}
instructions = {a : b.split(", ") for a, b in [x.strip().lower().split(": ") for x in f]}

current_instruction = "0"

while True:

  if TRACE: print(f"Instruction number: {current_instruction} \nRegister states: {register_states}")

  #Check for erronous halt, ie. calling an instruction outside of the instruction list 
  if current_instruction not in instructions:
    print(f"ERRONEOUS HALT: {register_states}")

  instruction = instructions[current_instruction]

  #If the program halts, print register states and exit
  if instruction[0] == "halt":
    print(f"PROPER HALT: {register_states}")
    break

  elif instruction[0][0:3] == "inc":
    #If instruction is calling for a register out of bounds, instanciate all registers up to that value
    if int(instruction[0][5:-1]) >= len(register_states):
      register_states += [0] * (int(instruction[0][5:-1]) - len(register_states) + 1)

    #Add one to the register state and branch to the next instruction
    register_states[int(instruction[0][5:-1])] += 1
    current_instruction = instruction[1]

  elif instruction[0][0:3] == "dec":
    #If instruction is calling for a register out of bounds, instanciate all registers up to that value
    if int(instruction[0][5:-1]) >= len(register_states):
      register_states += [0] * (int(instruction[0][5:-1]) - len(register_states) + 1)

    #If register value is 0, branch to second instruction
    if register_states[int(instruction[0][5:-1])] == 0:
      current_instruction = instruction[2]

    #Otherwise, subtract one from the register value and branch to the first instruction 
    else:
      register_states[int(instruction[0][5:-1])] -= 1
      current_instruction = instruction[1]

  else:
    print("ERROR Parsing instruction")
    break

f.close()