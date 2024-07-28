# ALU Module

This project implements basic logic gates, a half adder, a full adder, and an Arithmetic Logic Unit (ALU) in Python. The ALU can perform addition operations based on the provided opcode.

## Directory Structure

```
alu_module/
├── and_gate.py
├── or_gate.py
├── xor_gate.py
├── alu_module.py
└── README.md
```


## Files Description

- `and_gate.py`: Contains the implementation of the AND gate.
- `or_gate.py`: Contains the implementation of the OR gate.
- `xor_gate.py`: Contains the implementation of the XOR gate.
- `alu_module.py`: Main module that implements the half adder, full adder, and ALU using the logic gates.
- `README.md`: Documentation of the project.

## Logic Gates

### AND Gate
The AND gate returns 1 if both inputs are 1, otherwise it returns 0.

### OR Gate
The OR gate returns 1 if at least one of the inputs is 1, otherwise it returns 0.

### XOR Gate
The XOR gate returns 1 if the inputs are different, otherwise it returns 0.

## Half Adder

A half adder adds two single-bit binary numbers (a and b). It outputs a sum and a carry.

- Sum: `s = XOR_gate(a, b)`
- Carry: `c = AND_gate(a, b)`

## Full Adder

A full adder adds three single-bit binary numbers (a, b, and carry-in c). It outputs a sum and a carry-out.

- Sum1, Carry1: Output from the first half adder with inputs (a, b).
- Sum2, Carry2: Output from the second half adder with inputs (Sum1, c).
- Final Sum: `sum2`
- Carry-out: `c_out = OR_gate(Carry1, Carry2)`

## ALU (Arithmetic Logic Unit)

The ALU can perform different arithmetic operations based on the opcode.

- If opcode is 0, the ALU performs a half-adder operation.
- If opcode is 1, the ALU performs a full-adder operation.

## How to Run

1. Ensure you have all the required files (`and_gate.py`, `or_gate.py`, `xor_gate.py`, `alu_module.py`) in the same directory.
2. Run the `alu_module.py` file to execute the test cases and see the output of the half adder, full adder, and ALU.

```bash
python alu_module.py
```

# Example Output
```
Testing half_adder function
(0, 0)
(1, 0)
(1, 0)
(0, 1)

Testing full_adder function
(0, 0)
(1, 1)
(0, 1)
(0, 1)

Testing ALU function
(0, 0)
(1, 0)
(0, 1)
(1, 1)
```
