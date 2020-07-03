import requests

def post_request_customer(headers):
  url = "http://eso-api-gateway-naas-do.dtsdx-ndo.openshift.sdntest.netcracker.com/eso-manager/api/activation/service"

  customer_id=int(input("Customer_id:"))
  customer_name=input("Customer_name:")

  #payload = "{\r\n  \"id\": \"1234567891014\",\r\n  \"state\": \"Active\",\r\n  \"serviceSpecification\": {\r\n    \"id\": \"sde2e-customer-cfs_1.0.7\"\r\n  },\r\n        \"serviceCharacteristic\": [\r\n                {\r\n                        \"name\": \"complexServiceData\",\r\n                        \"value\": {\r\n                                \"customer\": {\r\n                                        \"customer-name\": \"customer_346\",\r\n                                        \"customer-topology\": \"Full Mesh\",\r\n                                        \"customer-external-id\": \"1234567891014\",\r\n                                        \"site-groups\": [\"group_1\"],\r\n                    \"departments\":[\r\n                      {\r\n                        \"department-name\":\"Finance\",\r\n                        \"department-description\":\"Finance Department\",\r\n                        \"dc-department\": false\r\n                      },\r\n                      {\r\n                        \"department-name\":\"Marketing\",\r\n                        \"department-description\":\"Marketing Department\",\r\n                        \"dc-department\": false\r\n                      }\r\n                                        ]\r\n                                }\r\n                        }\r\n                }\r\n        ],\r\n        \"relatedParty\": [\r\n                {\r\n                        \"role\": \"CustomerAccount\",\r\n                        \"id\": \"1234567891014\"\r\n                }\r\n        ]\r\n}"

  payload = "{\r\n  \"id\": \"customer_id\",\r\n  \"state\": \"Active\",\r\n  \"serviceSpecification\": {\r\n    \"id\": \"sde2e-customer-cfs_1.0.7\"\r\n  },\r\n        \"serviceCharacteristic\": [\r\n                {\r\n                        \"name\": \"complexServiceData\",\r\n                        \"value\": {\r\n                                \"customer\": {\r\n                                        \"customer-name\": \"customer_name\",\r\n                                        \"customer-topology\": \"Full Mesh\",\r\n                                        \"customer-external-id\": \"customer_id\",\r\n                                        \"site-groups\": [\"group_1\"],\r\n                    \"departments\":[\r\n                      {\r\n                        \"department-name\":\"Finance\",\r\n                        \"department-description\":\"Finance Department\",\r\n                        \"dc-department\": false\r\n                      },\r\n                      {\r\n                        \"department-name\":\"Marketing\",\r\n                        \"department-description\":\"Marketing Department\",\r\n                        \"dc-department\": false\r\n                      }\r\n                                        ]\r\n                                }\r\n                        }\r\n                }\r\n        ],\r\n        \"relatedParty\": [\r\n                {\r\n                        \"role\": \"CustomerAccount\",\r\n                        \"id\": \"customer_id\"\r\n                }\r\n        ]\r\n}"
  headers=headers
  #headers = {
  #'Content-Type': 'application/json',
  #'Authorization': 'Bearer eyJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4NjRhZmM5Ny04ZTE2LTQwYjItODIzOC05NjczMmUzNmU0YzMiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOltdfSwiYXpwIjoiODY0YWZjOTctOGUxNi00MGIyLTgyMzgtOTY3MzJlMzZlNGMzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSIsImlzcyI6Imh0dHA6XC9cL2lkZW50aXR5LW1hbmFnZW1lbnQtaWRwLmR0c2R4LW5kby5vcGVuc2hpZnQuc2RudGVzdC5uZXRjcmFja2VyLmNvbSIsInR5cCI6IkJlYXJlciIsImV4cCI6MTU5Mzc3ODA5MiwiaWF0IjoxNTkzNzc0NDkyLCJqdGkiOiI5N2VlOGY4OC1kYWZmLTRmYjUtYTAyNS1jNTZjYzlhZDNmMTkiLCJ0ZW5hbnQtaWQiOiJzeXN0ZW0ifQ.NxEgUwj7aaXjBciKTgAGxAQo2tQclmzjhhuhn8-0HjmNomWOIG_NJYHZVPcoa4oiMdkR1aM7LjFYyfsGSjezIz-p4jYkyoRW0a939X5SmZ75NqUZyxsswhWWaGq1lr0Upgqq5fsVzBQ-1JQRcLuiUKRv1cI0kWUh8Os7s4fx4TKxDcxSNbEMA4SpBDc-SQUQCON-GZesSD2AvAaZHPrKBWpazc_b16oX56KiSqTns5CFHBSuhaZdPz4dBLgh62wy2ox2zh1VQQ8sydbIKPhFh8mDzL25najdzN_a1-qJCapYAbPYymTYgQ9nO1WO7Lt_c4yXSfpn59eh1mc0rgNAlg',
 # 'Cookie': '95e55c1cb852d7389f81d84c331c0cb8=32bc09ae1a6229baf6aa04000f468703'
#}

  response = requests.request("POST", url, headers=headers, data = payload)
  print("Status code is:",response.status_code)
  response_json=response.json()
  for key,value in response_json.items():
      print(key, ":",value)

  #print(response.text.encode('utf8'))
  return 1
