# OOP Workout

## Completed Work

This folder contains my solutions for the OOP workout exercises.

Completed files:

* `c1_vehicle.py` - basic Vehicle class
* `c2_tank.py` - FuelTank class with private attributes
* `c3_types.py` - Car, Truck, and Motorcycle using inheritance
* `c4_electric.py` - ElectricCar class
* `c5_dunders.py` - dunder methods for Vehicle objects
* `c6_fleet.py` - Fleet manager class

## Pair Work

For the first challenges, I worked through the ideas together with classmates and discussed the class structure before writing the code. The later parts were completed more independently by building on the previous challenge files.

## Challenges and Difficulties

The first challenge was easier because it mainly focused on creating a class, adding attributes, and writing simple methods. Challenge 2 was also understandable after seeing how private attributes work with double underscores.

The harder part started when multiple classes had to work together. In Challenge 3, I had to understand how `FuelledVehicle` extends `Vehicle`, and how `Car`, `Truck`, and `Motorcycle` can reuse the same parent logic with different capacities and consumption values.

Another difficult part was making sure the program does not change the object state when an operation fails. For example, if there is not enough fuel or charge, the kilometres should stay the same.

The electric car challenge helped me understand that not every vehicle should inherit from the same fuel-based class. The electric car is still a vehicle, but it uses battery charge instead of a fuel tank.

The final fleet manager was the most challenging because it combined all earlier classes. It helped me understand how different vehicle objects can be stored together and handled using common methods like `drive()` and `describe()`.

Overall, this workout helped me practise object-oriented programming concepts such as classes, constructors, methods, encapsulation, inheritance, overriding, dunder methods, and working with multiple Python files.
