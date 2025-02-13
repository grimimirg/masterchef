  MasterChef Consumer Availability Management

MasterChef Consumer Availability Management
===========================================

This project is designed to manage the availability of consumers to receive a weekly menu. Track which consumers are available during specific weeks and facilitates the assignment of menus based on their availability.

Table of Contents
-----------------

*   [Features](#features)
*   [Classes](#classes)
    *   [ConsumerAvailability](#consumeravailability)
    *   [MasterChef](#masterchef)
*   [Usage](#usage)
*   [Requirements](#requirements)
*   [License](#license)

Features
--------

*   Track consumer availability for each week.
*   Add or remove availability for consumers.
*   Retrieve the first available week for a specific consumer.
*   Manage references for menus sent to consumers.

Classes
-------

### ConsumerAvailability

This class represents the availability of a consumer for a specific week.

#### Attributes

*   `weekNumber`: The week number for which the consumer is available.
*   `consumer`: The identifier for the consumer.

#### Methods

*   `__repr__()`: Returns a string representation of the consumer's availability.

### MasterChef

This class manages the overall availability data for consumers.

#### Attributes

*   `data`: The input data representing consumer availability.
*   `consumersAvailabilities`: A list of `ConsumerAvailability` instances.
*   `groupedConsumersAvailabilities`: A dictionary grouping weeks by consumer.

#### Methods

*   `prepareData()`: Prepares the availability data from the input.
*   `getConsumersAvailabilities()`: Returns the list of all consumer availabilities.
*   `prepareGroupedDataForConsumers()`: Groups the availability data by consumer.
*   `addAvailability(weekNumber, consumer)`: Adds a new availability for a consumer.
*   `removeAvailability(weekNumber, consumer)`: Removes an availability for a consumer.
*   `getFirstAvailableWeekForConsumer(consumer)`: Returns the first available week for a specified consumer.

Usage
-----

To use this code, simply run the `uv run app.py`. The function initializes the `MasterChef` class with an empty calendar and iterates through each week of the year, checking for consumer availability and managing menu assignments.
    

### Example Output

The output will display the weekly processing of consumer availability and menu assignments, including messages about adding and removing references.

Requirements
------------

This code is written in Python and requires no external libraries. It is compatible with Python 3.x.

License
-------

This project is licensed under the MIT License. See the LICENSE file for more details.
