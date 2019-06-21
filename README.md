[Install Docker on macOS](https://runnable.com/docker/install-docker-on-macos)

[Install Docker on Windows 10](https://runnable.com/docker/install-docker-on-windows-10)

### To run the Dockerhub image:

```
mkdir datasets && cd datasets
wget https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz
cd ..
docker pull pull krmarcus/flask-ml-example
docker run -v "$(pwd)"/datasets:/app/datasets -p 5000:5000 krmarcus/flask-ml-example
```

You should now be able to go to

```
http://localhost:5000/items/similar
http://localhost:5000/items
```

### To run the code locally through Docker:

Clone the repo

```
git clone https://github.com/krmarcus-ucsd/flask-ml-example.git
cd flask-ml-example
```

Download the dataset

```
mkdir datasets && cd datasets
wget https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz
```

Build and run Docker image

``
$ docker-compose up
``

You should now be able to go to

```
http://localhost:5000/items/similar
http://localhost:5000/items
```

### JSON APIs

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

### HTML Web Pages

There are also support for [HTML](https://www.w3schools.com/whatis/whatis_html.asp) output

```
$ open -a Safari http://localhost:5000/items/similar

$ open -a Safari http://localhost:5000/items
```
