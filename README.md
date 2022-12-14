# IoT System

<p align="center">
	This project was part of the Analysis and Design of Information Systems course at NTUA.
<p>
	
<p align="center">
	<img alt="Byte Code Size" src="https://img.shields.io/github/languages/code-size/sergiosb96/InfoSystems_Project?color=yellowgreen" />
	<img alt="# Lines of Code" src="https://img.shields.io/tokei/lines/github/sergiosb96/InfoSystems_Project?color=yellowgreen" />
	<img alt="# Languages Used" src="https://img.shields.io/github/languages/count/sergiosb96/InfoSystems_Project?color=yellow" />
	<img alt="Top language" src="https://img.shields.io/github/languages/top/sergiosb96/InfoSystems_Project?color=yellow" />
	<img alt="Last commit" src="https://img.shields.io/github/last-commit/sergiosb96/InfoSystems_Project?color=important" />
</p>

## Technology Stack
* [Apache Flink](https://flink.apache.org/) to proccess our data.
* [RabbitMQ](https://www.rabbitmq.com/) as message broker.
* [NodeJS](https://nodejs.org/en/) to create a server that publishes and consumes messages.
* [OpenTSDB](http://opentsdb.net/) as the database.
* [Grafana](https://grafana.com/) as a  user dashboard to monitor the devices.
* [Python3](https://www.python.org/downloads/) to create the dummy data that represent the data from the IoT sensors.

## Tools
* [Docker](https://www.docker.com/) to create containers

## Installation
The following installation instructions are intended for Docker deployment. Docker is a tool that runs on all modern Operating Systems and simply works.
You simply execute the commands listed on the installation.txt file.

## Devices
This project is a simulation of a real life IoT system, we came up with a scenario that represent a real life use case. 

The devices we use:

|ID     |Location   |
|-------|-----------|
|0      |Fridge     |
|1      |Freezer    |


|Device                 |Name            |Value                    |Value Range                                                                   |
|-----------------------|----------------|-------------------------|------------------------------------------------------------------------------|
|Motion sensor          |sensorMotion0   |`bool` state             |binary                                                                        |
|Motion sensor          |sensorMotion1   |`bool` state             |binary                                                                        |
|Temperature sensor     |sensorTemp0     |`int` temp, `int` tempDif|temp: range `0 ... 10`                        							      |
|Temperature sensor     |sensorTemp1     |`int` temp, `int` tempDif|temp: range `-3 ... -13`                                                      |
|Door magnet     		|sensorMagnet0   |`bool` state             |binary                                                                        |
|Door magnet    		|sensorMagnet1   |`bool` state             |binary                                                                        |

## Scenario
This IoT system is a simulation of a Food Warehouse <br>
The owner of this company had an accident that made all of his inventory go to waste so he hired a team to build a smart monitoring system to prevent a similar accident. <br>
The Warehouse works on weekdays from 8:00 to 17:00 and on weekends from 10:00 to 14:00 <br>
The Food is stored in 2 places, 1 walk-in Freezer and a seperate room that is a Fridge. <br>
Each of them has Temperature Sensors that mesure the exact temperature and calculate the difference between the previous timestamp. <br>
We also have Magnet Sensors and Motion Sensors in each of these locations. <br>
The Magnet Sensors are located in the door of each location and records when it is opened and closed. <br>
The Motion Sensors are also located inside each location to prevent from anyone being trapped inside the Freezer or Fridge and have any accident. <br>
This system is not intended to replace any security system as the states are reported from each sensor every 15 minutes to prevent any network bottleneck. <br>
The technology that is used to actually send the data to our message broker is not presented nor analyzied in our project. <br>
In our scenario we simulated the data from a full Week. <br>