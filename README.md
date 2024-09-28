# Vending-Machine-Control

This repository contains the implementation of a Python program that simulates the operation of the coin mechanism of a vending machine for soft drinks. The machine offers functionalities for both consumers and administrators, allowing for payment operations and the management of coins and banknotes.

Features

Consumer User:

Drink Purchase Simulation:
• The machine accepts money in banknotes and coins.
• If the amount inserted is sufficient for the purchase, the change will be calculated and returned automatically.
• The drink will be "released" to the user.
• If the inserted amount is insufficient or change cannot be provided, the purchase will be canceled, and a message will be displayed informing the issue.

Administrator User:
• View Balance of Banknotes and Coins: The administrator can view the available quantity of each type of banknote and coin in the machine.
• Update Balance of Banknotes and Coins: The administrator can manually update the number of banknotes and coins by type, allowing for restocking or necessary adjustments to the system.
• Control the Number of Coins by Type: The system automatically manages the number of coins available for change, ensuring that the machine operates within its capacity.
