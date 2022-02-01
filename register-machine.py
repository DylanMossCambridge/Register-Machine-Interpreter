TRACE = True
f = open("input.txt", "r")
register_states = [0] + list(map(lambda x: int(x), f.readline()[1:-2].split(", ")))
instructions = {a : b.split(", ") for a, b in [x.strip().lower().split(": ") for x in f]}
current_instruction = "0"

while True:
  if TRACE: print(f"Instruction number: {current_instruction} \nRegister states: {register_states}")
  if current_instruction not in instructions: print(f"ERRONEOUS HALT: {register_states}")
  instruction = instructions[current_instruction]
  if instruction[0] == "halt": print(f"PROPER HALT: {register_states}"); break
  elif instruction[0][0:3] == "inc": 
    if int(instruction[0][5:-1]) >= len(register_states): register_states += [0] * (int(instruction[0][5:-1]) - len(register_states) + 1)
    register_states[int(instruction[0][5:-1])] += 1; current_instruction = instruction[1]
  elif instruction[0][0:3] == "dec":
    if int(instruction[0][5:-1]) >= len(register_states): register_states += [0] * (int(instruction[0][5:-1]) - len(register_states) + 1)
    if register_states[int(instruction[0][5:-1])] == 0: current_instruction = instruction[2]
    else: register_states[int(instruction[0][5:-1])] -= 1; current_instruction = instruction[1]
  else: print("ERROR Parsing instruction"); break

f.close()