#!/bin/bash

curl -X POST "http://127.0.0.1:8000/addProduct" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"testing1\",\"description\":\"test\",\"parametres\":{\"some\":1}}"
curl -X POST "http://127.0.0.1:8000/addProduct" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"testing2\",\"description\":\"test2\",\"parametres\":{\"price\":10}}"

curl -X GET "http://127.0.0.1:8000/getProductByName/test?is_full_match=true" -H  "accept: application/json"
curl -X GET "http://127.0.0.1:8000/getProductByName/test?is_full_match=false" -H  "accept: application/json"

#id - 5fb636785ab46c0f3be7b77d заменить на любой из предыдущего запроса
curl -X GET "http://127.0.0.1:8000/getProductByID/5fb636785ab46c0f3be7b77d" -H  "accept: application/json"

curl -X GET "http://127.0.0.1:8000/getProductByParameter/some/1" -H  "accept: application/json"
curl -X GET "http://127.0.0.1:8000/getProductByParameter/some/10" -H  "accept: application/json"