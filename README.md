# SmartHome System

<p align="center">
	This project was part of the Analysis and Design of Information Systems course at NTUA.
<p>
	
<p align="center">
	<img alt="Byte Code Size" src="https://img.shields.io/github/languages/code-size/ChristosHadjichristofi/NodeRed-SmartHome?color=yellowgreen" />
	<img alt="# Lines of Code" src="https://img.shields.io/tokei/lines/github/ChristosHadjichristofi/NodeRed-SmartHome?color=yellowgreen" />
	<img alt="# Languages Used" src="https://img.shields.io/github/languages/count/ChristosHadjichristofi/NodeRed-SmartHome?color=yellow" />
	<img alt="Top language" src="https://img.shields.io/github/languages/top/ChristosHadjichristofi/NodeRed-SmartHome?color=yellow" />
	<img alt="Last commit" src="https://img.shields.io/github/last-commit/ChristosHadjichristofi/NodeRed-SmartHome?color=important" />
</p>

## Technology Stack
* [Apache Flink](https://flink.apache.org/) to proccess our data
* [RabbitMQ](https://www.rabbitmq.com/) as message broker
* [NodeJS](https://nodejs.org/en/) & [ExpressJS](https://expressjs.com/) to create a server that routes and handles all incoming requests from the devices
* [OpenTSDB](http://opentsdb.net/) as the database
* [Grafana](https://grafana.com/) as a  user dashboard to monitor the devices
* [Python3](https://www.python.org/downloads/) to create dummy data that represent the data from the IoT sensors and to create a simulation script which makes many api calls to the express server

## Tools
* [Docker](https://www.docker.com/) to create containers

## Apache Flink


## Installation
The following installation instructions are intended for Linux Distros.


## Devices
Because this project will eventually be a simulation of a smart home system, we had to think of some devices that exist in a smart home system.

The simulation consists of:

|Room ID|Room       |
|-------|-----------|
|0      |Bedroom    |
|1      |Living Room|
|2      |Kitchen    |
|3      |Bathroom   |
|4      |Balcony    |

Each device that appears in the following table consists of its name plus a number. The number is in which room this device belongs. If no number exists, there's only one device of that kind in the house.

|Device                 |Name            |Value                    |Value Range                                                                   |
|-----------------------|----------------|-------------------------|------------------------------------------------------------------------------|
|Smoke sensor           |sensorSmoke     |`bool` state             |binary                                                                        |
|Light sensor           |sensorLight0    |`int` lm                 |range `0...1000` (sunshine: `>500`, evening: `0 ~ 100`, lighting: `100...500`)|
|Light sensor           |sensorLight1    |`int` lm                 |"                                                                             |
|Light sensor           |sensorLight4    |`int` lm                 |"                                                                             |
|Motion sensor          |sensorMotion1   |`bool` state             |binary                                                                        |
|Motion sensor          |sensorMotion4   |`bool` state             |binary                                                                        |
|Temperature sensor     |sensorTemp0     |`int` temp, `int` tempDif|temp: range `10...35`, tempDif example: `+/- 4`                               |
|Temperature sensor     |sensorTemp1     |`int` temp, `int` tempDif|"                                                                             |
|Window/Door magnet     |sensorMagnet0   |`bool` state             |binary                                                                        |
|Window/Door magnet     |sensorMagnet1   |`bool` state             |"                                                                             |
|Window/Door magnet     |sensorMagnet2   |`bool` state             |"                                                                             |
|Window/Door magnet     |sensorMagnet3   |`bool` state             |"                                                                             |
|Alarm                  |alarm           |`bool` state             |binary                                                                        |
|Siren                  |siren           |`bool` state             |binary                                                                        |
|Thermostat             |thermostat      |`bool` state, `int` temp |state: binary, temp: range `10...35`                                          |
|Lamp                   |lamp0           |`bool` state             |binary                                                                        |
|Lamp                   |lamp1           |`bool` state             |"                                                                             |
|Lamp                   |lamp2           |`bool` state             |"                                                                             |
|Lamp                   |lamp3           |`bool` state             |"                                                                             |
|Lamp                   |lamp4           |`bool` state             |"                                                                             |
|Vacuum                 |vacuum          |`bool` state             |binary                                                                        |
|Air-Conditioner        |ac0             |`bool` state, `int` temp |state: binary, temp: range `18...30`                                          |
|Air-Conditioner        |ac1             |`bool` state, `int` temp |"                                                                             |
|Water Heater           |waterHeater     |`bool` state             |binary                                                                        |
|Switch - Phone charger |switch0         |`bool` state             |binary                                                                        |
|Switch - Coffee machine|switch1         |`bool` state             |"                                                                             |

## Scenario
Because this is a simulation, we had to create a scenario based on the life of an imaginary person, Bob. <br>
Bob works on weekdays. More specifically:
* He wakes up at 07:30
* Eats breakfast at 08:00
* Works from 09:00 to 17:00
* He arms the alarm before leaving the house and disarms the alarm when he returns
* Takes a shower at 17:30
* Eats dinner at 20:00
* Sleeps at 24:00

On the weekends he has a more relaxed schedule:
* He wakes up at 09:00
* He sleeps at 02:00

Bob, on a daily basis has some demands for this smart home system. More specifically:
* He wants the Water heater to start boiling water at 17:00
* He wants the vacuum to clean every Monday - Wednesday - Friday from 10:00 to 12:00
* He wants his phone to get charged from 03:30 to 06:30
* He wants to have his coffee ready by 07:45
* He wants the living room lights to be turned on when its getting dark and he enters the appartment
* He wants the balcony lights to be turned on when its getting dark and motion is detected on the balcony 
* He wants the lights in the bedroom, bathroom and kitchen to be switched off when he arms the alarm
* He wants the thermostat to be set on when the temperature drops below 22 degrees
* He wants the a/c in the bedroom to be turned on when the temperature rises above 29 degrees
* He wants the a/c in the living room to be turned on when the temperature rises above 29 degrees
* He wants door/window openings to be logged to the database

Also in case of an emegerncy, he wants to be notified from a bot. Such emergencies are:
* Fire
* Burglary
* Possible malfunction of any temperature sensor in the smart system

Based on the above a script was created, that simulates Bob's life for a period of a week.
Unexpected events throughout the week:
* On Tuesday at 13:00 burglars broke into Bob's house using the door in the living room
* On Friday at 20:00 there was a fire in Bob's kitchen
* On Sunday at 16:00 a temperature sensor malfunctioned


## Diagrams
![component-diagram]()
![deployment-diagram]()
