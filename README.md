# Configuration Manager
This repository contains flask based endpoints for configuration manager service.



## Configurations

* Install all the packages using the command below:
  ```
  $ pip3 install --upgrade -r requirements.txt
  ```
* Root directory contains `.env.example` file, configure it according to you needs
* Rename the file using the command below:
  ```
  $ cp .env.example .env
  ```
* To export the environment variable use the command given below:
  ```
  $ source .env
  ```

## To start server

To start the server use the command given below:

```
$ flask run --host=$FLASK_HOST_IP --port=$((FLASK_HOST_PORT))
```
First type to start the server in virtual environment, if it is not working the exit the virtual environment and run it simple with above command.

## Development Resources

* [Virtual environment creation steps](https://gist.github.com/aliartiza75/16f0bd59991a9ab469f617c2a71191dd)
