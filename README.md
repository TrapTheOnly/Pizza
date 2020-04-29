# Pizza

## Table of contents
* [General info](#general-info)
* [Project details](#project-details)
* [Installation](#installation)
* [FAQ](#faq)

## General info
This is a Pizza app, which has main functions, such as:
* Creating a new user 
* Logging in 
* Ordering a pizza
* Changing its ingredients
* Adding extensions to it
* Oredirng and saving the reciept to your account
* As admin adding new pizzas to available ones
* As admin searching data about all users
* Notifying all users about new pizzas

## Project details
* Current version - 2.1
* Created using Tkinter on Python
* Uses SQLite databases to store information

## Installation
```
pip install tk
git clone https://github.com/TrapTheOnly/Pizza.git
```
## FAQ
### Currently confirmed issues
* If somewhy you terminated the program without proper exit, check if your ..\Pizzas\pizza_ings.txt file consists only of only one '0' or not. If not, then delete everything written in it and write '0' The file's inside should look like:
```
0
```
