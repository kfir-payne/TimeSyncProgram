# Time Sync Program
A Python time sync program that will consist of a server and clients.
I should be able to run the server on one machine, and few (<100) clients on different machines in the same network.

Each client should send it's time every second to the server.
The server must choose one client from all the clients, whose clock will be the master clock. 

The server must send the master clock to each client every second.
If the master client does not send it's time for one minute, the server must choose a new client from the other clients to be the master clock.

Each client should implement a command line interface, in which the user can ask the the client for the last master clock it received from the server.
The UI should be console based, and be as simple as possible.


