def sendmes(m):
    return requests.get('http://0s.mfygs.orswyzlhojqw2ltpojtq.cmle.ru/' + 
                 'bot592804892:AAGPnvbvCRRlMv0AuyD_F0THfk7UMBtgU64/sendMessage?chat_id=-1001362959453&text=' + m + '&parse_mode=Markdown').content
import json
import requests
import time
addf = open('adresses.txt', 'r')
add = []
for i in addf:
    add.append(i.rstrip())
bal = []
for i in add:
    dt = requests.get('https://blockchain.info/rawaddr/' + i[:34]).content
    dt = json.loads(dt)
    bal.append(dt['final_balance'] / 10 ** 8)
while True:
    try:
        t = int(time.time())
        for i in range(len(add)):
            dt = requests.get('https://blockchain.info/rawaddr/' + add[i][:34]).content
            dt = json.loads(dt)
            dt = dt['final_balance'] / 10 ** 8
            c = bal[i] - dt 
            if c >= 500:
                if add[i][:34] != '1Kr6QSydW9bFQG1mXiPNNu6WpJGmUa9i1g' or c >= 1000:
                    print('-' + str(c), add[i])
                    sendmes('*' + '-' + str(round(abs(c), 3)) + add[i][34:] + '*' + '\r\n' +
                                     '[View wallet]' + '(https://blockchain.info/ru/address/' + add[i][:34] + ')')
            if c <= -500:
                if add[i][:34] != '1Kr6QSydW9bFQG1mXiPNNu6WpJGmUa9i1g' or c <= -1000:
                    print('+' + str(abs(c)), add[i])
                    sendmes('*' + '%2B' + str(round(abs(c), 3)) + add[i][34:] + '*' + '\r\n' +
                                     '[View wallet]' + '(https://blockchain.info/ru/address/' + add[i][:34] + ')')
            bal[i] = dt
        te = int(time.time()) - t
        time.sleep(max(0, 100 - te))

    except:
        print('err')
        time.sleep(5)
