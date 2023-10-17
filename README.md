Author: Dylan Murphy
Contact address: dmurphy@uoregon.edu
Description:
This is a trivial web server built using Flask that reads a port number from a config file. You are able to enter page names and the program will return them if they exist, otherwise it will return a 404 file not found error. If the string entered contains '~' or '..', it with return a 403 forbidden error.