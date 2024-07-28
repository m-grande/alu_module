from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate


def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)


# TEST CASE HALF ADDER
print("Testing half_adder function")
print(half_adder(0, 0))  # Expected output: (0, 0)
print(half_adder(0, 1))  # Expected output: (1, 0)
print(half_adder(1, 0))  # Expected output: (1, 0)
print(half_adder(1, 1))  # Expected output: (0, 1)
print("======")


def full_adder(a, b, c):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, c)
    c_out = OR_gate(carry1, carry2)
    return (sum2, c_out)


# TEST CASE FULL ADDER
print("Testing full_adder function")
print(full_adder(0, 0, 0))  # Expected output: (0, 0)
print(full_adder(1, 1, 1))  # Expected output: (1, 1)
print(full_adder(0, 1, 1))  # Expected output: (0, 1)
print(full_adder(1, 1, 0))  # Expected output: (0, 1)
print("======")


def ALU(a, b, c, opcode):
    if opcode == 0:
        s, carry = half_adder(a, b)
    elif opcode == 1:
        s, carry = full_adder(a, b, c)
    return (s, carry)


# TEST CASE ALU
print("Testing ALU function")
print(ALU(0, 0, 1, 0))  # Expected output: (0, 0) - half adder with a=0, b=0
print(ALU(0, 0, 1, 1))  # Expected output: (1, 0) - full adder with a=0, b=0, c=1
print(ALU(1, 1, 1, 0))  # Expected output: (0, 1) - half adder with a=1, b=1
print(ALU(1, 1, 1, 1))  # Expected output: (1, 1) - full adder with a=1, b=1, c=1
