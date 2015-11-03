# Integrating R and the AVANSE DB
The goal of this document is to design and document the integration of an R client and a REST-style data store.
Initially we will work towards attaching parcel boundaries to farmers

## HTTP requests

```R
GET("AvanseIndicators/v1/geo/checkid/45")
```



