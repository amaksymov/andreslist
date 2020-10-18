# Andreslist

### Quickstart:

Startup all services:
```bash
$ docker-compose up --build
```
Visit [andreslist.com](http://andreslist.com).
Maybe you need add andreslist.com to your __/etc/hosts__ file (on Linux).

API docs [api.andreslist.com/docs](http://api.andreslist.com/docs).

Run server test:
```bash
$ docker-compose up server -d
$ docker-compose exec server pytest .
```
