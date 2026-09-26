import os
while True:
  binary = input("Input a binary number ")
  valid_binary = {"1", "0"}
  check_number = 0
  final_number = 0
  number = list(binary)
  bits = len(number)
  if not set(number).issubset (valid_binary):
    print("Wrong, Program Terminated")
    os._exit(0)
  for i in range(bits):
    if number[check_number] == "1":
      final_number += 2**(bits- check_number -1)
      check_number += 1
    else:
      check_number += 1
  if bits == 8 and final_number > 64 and final_number < 91 or final_number > 96 and final_number < 123:
    letter = chr(final_number)
    print(letter)
  else:
    print(final_number)
