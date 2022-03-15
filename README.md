# Data Capture And Stats
## This program was created as part of the hiring process for Indigo.


This document describes the steps to execute the program as well as to execute the defined unit tests for:

- Run Program
- DataCapture class unit tests
- BuildStats class unit tests

## Structure
The project is composed by two files:
- stats.py: Is where all the business logic is contained. Classes and methods to run the program.
- stats_tests.py: Is where we defined the unit tests to validate the behaviour of the classes and methods.

### 1. Run Program
Inside stats.py file, there are three defined classes:
1. BuildStats: Is used to create and reproduce the statistical methods.
2. DataCapture: Is used to set the initial data values, set new values and build the stats.
3. DataCaptureAndStats: Is the class that let us instantiate DataCapture and run the wanted method and logic. User define what to execute and what values to set.

To run the program you need to follow the next steps:
1. Go to stats.py file.
2. In the DataCaptureAndStats class, inside the init method, you can set the initial values to compute changing the value of the "initialValues" constant.
3. In the DataCaptureAndStats class, inside the run method, you can add new values by using the method '.add(#)'.
4. Once added wanted values, you can either show_values(), or build the stats by calling build_stats().
5. By creating an instance of BuildStats through build_stats() you can now use the statistical functions less(bound), greater(bound), betwteen(lowerBound, upperBound).

Once defined all the initial parameters and the methods you want to reproduce, you just need to run the following command.

> python stats.py

### 2. Run Unit Tests
There are one unit test created to valiadte the behaviour of each method defined in the program. To define new ones, you need to go to the stats_test.py file and inside the ClassTest define new unit tests.

To run existing ones, you need to run the following command:
> python stats_tests.py

As a result you should receive an OK which means all the unit test has passed succesfully.
