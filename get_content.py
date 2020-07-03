import requests

def get_content_customer(headers):
  URL = "http://eso-api-gateway-naas-do.dtsdx-ndo.openshift.sdntest.netcracker.com/eso-manager/api/activation/service"

  customer_id=int(input("Customer_id:"))
  customer_name=input("Customer_name:")

  payload = "{\r\n  \"id\": \"customer_id\",\r\n  \"state\": \"Active\",\r\n  \"serviceSpecification\": {\r\n    \"id\": \"sde2e-customer-cfs_1.0.7\"\r\n  },\r\n        \"serviceCharacteristic\": [\r\n                {\r\n                        \"name\": \"complexServiceData\",\r\n                        \"value\": {\r\n                                \"customer\": {\r\n                                        \"customer-name\": \"customer_name\",\r\n                                        \"customer-topology\": \"Full Mesh\",\r\n                                        \"customer-external-id\": \"customer_id\",\r\n                                        \"site-groups\": [\"group_1\"],\r\n                    \"departments\":[\r\n                      {\r\n                        \"department-name\":\"Finance\",\r\n                        \"department-description\":\"Finance Department\",\r\n                        \"dc-department\": false\r\n                      },\r\n                      {\r\n                        \"department-name\":\"Marketing\",\r\n                        \"department-description\":\"Marketing Department\",\r\n                        \"dc-department\": false\r\n                      }\r\n                                        ]\r\n                                }\r\n                        }\r\n                }\r\n        ],\r\n        \"relatedParty\": [\r\n                {\r\n                        \"role\": \"CustomerAccount\",\r\n                        \"id\": \"customer_id\"\r\n                }\r\n        ]\r\n}"
  headers=headers
  #headers = {
  #'Content-Type': 'application/json',
  #'Authorization': 'Bearer eyJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4NjRhZmM5Ny04ZTE2LTQwYjItODIzOC05NjczMmUzNmU0YzMiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOltdfSwiYXpwIjoiODY0YWZjOTctOGUxNi00MGIyLTgyMzgtOTY3MzJlMzZlNGMzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSIsImlzcyI6Imh0dHA6XC9cL2lkZW50aXR5LW1hbmFnZW1lbnQtaWRwLmR0c2R4LW5kby5vcGVuc2hpZnQuc2RudGVzdC5uZXRjcmFja2VyLmNvbSIsInR5cCI6IkJlYXJlciIsImV4cCI6MTU5Mzc4MTk4MywiaWF0IjoxNTkzNzc4MzgzLCJqdGkiOiI2NzRhYWFlMC00ZGM2LTQ3OTItOTllNC1iMjg2NDRmYjhiYmMiLCJ0ZW5hbnQtaWQiOiJzeXN0ZW0ifQ.d5O2uAkSg_Ie5qhBBCa-4cSbY3NFepPfBsVQpGNY1l5yyDq73B_o3B35qXzPAaQnbqxBjeI4n8YmXkjIRgqCPLMLNvAXmPeXD8H4sZPj8YeXQg8QnSoEKzzXE2bL13953sOcaR724Ci8r1gb6BuyiQn-QJgpCA5XwXIqeqns_l-X_uyNWASIveAzg2PhNGnwVFEBfrUgFwDsXtdmMbiRFKEEpmS5SOBdvnIvydHmuMUbJ1pzj_BsXKZE27v449AxNsrjKHSSGcBbFzaAxXdA1G-alJz0PAXWru9iRE0bnlT9--i4mCEPhXlvUzwu-tpiKas25h9Rmuce3ob8ILx8tQ',
 # 'Cookie': '95e55c1cb852d7389f81d84c331c0cb8=c865794e3b3b5e2cdbdd5e8ebeb714ca'
#}

  response = requests.get(url = URL,headers=headers,data = payload)
  #final_result=response.json()
  #print(final_result)
  print("Status code is:",response.status_code)
  response_json=response.json()
  #for index in response_json:
  print(response_json)
  return 1

