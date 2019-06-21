[Install Docker on macOS](https://runnable.com/docker/install-docker-on-macos)

[Install Docker on Windows 10](https://runnable.com/docker/install-docker-on-windows-10)

``
$ docker-compose up
``

The APIs will return [JSON](https://www.w3schools.com/whatis/whatis_json.asp) results.

``/api/items`` returns lists of items accepting a start index and a count of items to return

```
$ curl http://localhost:5000/api/items/50/10

$ curl http://localhost:5000/api/items/50

$ curl http://localhost:5000/api/items
```

``/api/similar`` returns lists of items that are similar

```
$ curl http://localhost:5000/api/similar/B0006VMBHI
```

There are also support for [HTML](https://www.w3schools.com/whatis/whatis_html.asp) output

```
$ open -a Safari http://localhost:5000/items/similar

$ open -a Safari http://localhost:5000/items
```