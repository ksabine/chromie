### Chromie Time Keeper Application

### time-keeper
Containerized web API that with singular, root endpoint (`http://localhost/`) that will return the current UTC datetime in ISO format

OpenAPI / Swagger spec available at http://localhost/docs

#### Build and Run (docker native)
```
# build container
docker build time-keeper -t time-keeper:latest
# run container (-d is optional to run detached)
docker run -p 80:80 -d time-keeper:latest
```

#### Build and Run (docker-compose)
```
# build container
docker-compose build time-keeper
# run container (-d is optional to run detached)
docker-compose up -d time-keeper
```


### time-tester
Container used to test time-keeper container API endpoint.  Will perform GET call on endpoint X times per second based on `CALLS_PER_SECOND` environment variable.  It will also output a JSON log containing timestamp, success, status_code, and ttlb.

#### Environment Variables
| Variable | Default  | Description  |
|-----|-----|-----|
| ENDPOINT  | http://time-keeper  | API endpoint to query with GET call  |
| CALLS_PER_SECOND | 10  | Number of API calls to request per second  |

#### Build and Run (docker native)
Ensure time-keeper container is built and running before starting time-tester

```
# build container
docker build time-tester -t time-tester:latest
# run container (-d is optional to run detached)
docker run --link time-keeper time-tester:latest
```

#### Build and Run (docker-compose)
With docker-compose, time-keeper will be started automatically when time-tester is started

```
# build both containers
docker-compose build
# run test-container
docker-compose up time-tester
```