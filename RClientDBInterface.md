# Integrating R and the AVANSE DB
The goal of this document is to design and document the integration of an R client and a REST-style data store.
Initially we will work towards attaching parcel boundaries to farmers

## HTTP requests
The first step is to establish simple communication with the server. A url was created for the purpose of testing to see if the R client can reach the server

```R
GET("<server path in email>/v1/geo/checkid/45")
```



