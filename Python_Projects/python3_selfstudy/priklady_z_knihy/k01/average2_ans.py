#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

numbers = []
indexes = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("zadejte číslo nebo Enter pro ukončení: ")
        if not line:
            break
        indexes.append(len(numbers))
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

swapped = True
while swapped:
    swapped = False
    for index in indexes:
        if index + 1 == len(numbers):
            break
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
            swapped = True

index = int(len(numbers) / 2)
median = numbers[index]
if index and index * 2 == len(numbers):
    median = (median + numbers[index - 1]) / 2

print("čísla:", numbers)
print("počet =", len(numbers), "součet =", total,
      "nejmenší =", lowest, "největší =", highest,
      "průměr =", total / len(numbers), "medián =", median)
