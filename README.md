# Messenger
Messenger with a simple interface, written on the basis of the socket library
____
### Install everything you need and run
#### Installation
```
git clone https://github.com/b0shka/messenger.git
cd messenger
pip3 install -r requirements.txt
```
In the file `data/data_config.json` specifies the ip and port, and the same ip and port are specified in the code on which the program will run. And in the file `data/config.json` specifies user data name, number, country
#### Run
##### Running the server code
```
python3 ./server.py
```
##### Run the client code
```
python3 ./client.py
```
![alt text](style/image.png)

### Additionally
A `chat.service` file was also created to run this bot on the server. The `chat.desktop` file contains the code for creating a program shortcut in linux. The file `client.bin` is already a compiled program
