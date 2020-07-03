import requests
import json
import get_content as g
import post_contentversion2 as p


def call_function(case_enter,headers):
  if(case_enter==1):
    g.get_content_customer(headers)
  elif(case_enter==2):
    p.post_request_customer(headers)



if __name__ == "__main__":
    print("Please enter the case to execute:")
    print("1:Get_customer_service")
    print("2:Post_cusotmer service")
    case_enter=int(input())
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4NjRhZmM5Ny04ZTE2LTQwYjItODIzOC05NjczMmUzNmU0YzMiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOltdfSwiYXpwIjoiODY0YWZjOTctOGUxNi00MGIyLTgyMzgtOTY3MzJlMzZlNGMzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSIsImlzcyI6Imh0dHA6XC9cL2lkZW50aXR5LW1hbmFnZW1lbnQtaWRwLmR0c2R4LW5kby5vcGVuc2hpZnQuc2RudGVzdC5uZXRjcmFja2VyLmNvbSIsInR5cCI6IkJlYXJlciIsImV4cCI6MTU5Mzc5MDA4MCwiaWF0IjoxNTkzNzg2NDgwLCJqdGkiOiJiYTkzZDk1NS03ZTUxLTQ2NjctOGE5Ny02ZjJlMGNkMGZmMDEiLCJ0ZW5hbnQtaWQiOiJzeXN0ZW0ifQ.b_yHt-2KxoYD9uq-rhjXeRaFqXtVHbFbTaOzUptoLsVvmP7imlflJjBS67WNjYT0YfQSK8b1VveDkKP2hlVmu8FcGxya6kRXZICU_lEHoJ7Vu9bz9MTwT0pOqZgX8vJVZgSCToXiip8CB2cT6W6Dl128q4pF-loC0c3gDM8YVwVQIKqZ4geY7ahPVgi0MPpeJCUTQMOrNsIA0hdd_dfCa8vulXrYaHvAVPVgG7vse8_fFu38UfWS0kys1zb2Kai_AhAHjhDjTdZSZra8tXYuCJCf_xT5YZUPTYwDeaiQlDy0-utZ7aOKqIwxBw9-VrziNy3L9aIg5HeHJgAnMCFl9A',
  'Cookie': '95e55c1cb852d7389f81d84c331c0cb8=c865794e3b3b5e2cdbdd5e8ebeb714ca'
}
    call_function(case_enter,headers)

