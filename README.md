# Configuration Manager
This repository contains flask based endpoints for configuration manager service.

## Configurations and server initialization

* Instal docker ce version [link](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

* Start mongodb server:
```bash
    $ sudo docker run --name=config-manage-mongodb --net=host -d mongo:latest 
```

* Check mongodb server is running:
```bash
    $ sudo docker logs config-manage-mongodb
```

* Move inside the project folder:
```bash
    $ cd config-manager
```

* Install python virtual environment:

```bash
    $ python3 -m pip install --user config-manager-venv
```

* Create a virtualenv
```bash
    $ python3 -m virtualenv env
```

* Activate virtual environment
```bash
    $ source config-manager-venv/bin/activate
```

* Install all the packages using the command below:
  ```bash
  $ pip3 install --upgrade -r requirements.txt
  ```
* Root directory contains `.env.example` file, configure it according to you needs
* Rename the file using the command below:
  ```bash
  $ cp .env.example .env
  ```
* To export the environment variable use the command given below:
  ```bash
  $ source .env
  ```

* To start the server use the command given below:

```bash
$ flask run --host=$FLASK_HOST_IP --port=$((FLASK_HOST_PORT))
```

## API Documentation

APi documentation can be found on this link [API DOCUMENTATION](https://documenter.getpostman.com/view/5856653/RzZAixnE)



