#!/usr/bin/python3
# t1k random
import requests, os
import urllib3
import random
from multiprocessing import Pool #<----- pip install
import time
import json
urllib3.disable_warnings()

def randomUsername():
    wefdef1 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm') for i in range(1)))
    wefasf2 = ''.join((random.choice('._qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(2)))
    wefasf3 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(1)))
    randomUsername = wefdef1+wefasf2+wefasf3
    return randomUsername
def randomUsername2():
    wefdef1 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(5)))
    randomUsername = wefdef1
    return randomUsername
def randomUsername3():
    wefdef1 = ''.join((random.choice('ksaheckr') for i in range(1)))
    wefasf2 = ''.join((random.choice('._qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(3)))
    wefasf3 = ''.join((random.choice('ksaheckr') for i in range(1)))
    randomUsername = wefdef1+wefasf2+wefasf3
    return randomUsername
def randomUsername4():
    wefdef1 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm') for i in range(1)))
    wefasf2 = ''.join((random.choice('._qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(1)))
    wefasf3 = ''.join((random.choice('qwertyuioplkjhgfdsazxcvbnm0123456789') for i in range(1)))
    randomUsername = wefdef1+wefasf2+wefasf3
    return randomUsername
t4_fromWhere = input("ENTER A NUMBER TO START FROM TOP : \n[ 100 ] -> 100,99,98,97...\nEnter a Number or hit enter (default:5000): ") or "5000" 
t4_fromWhere=int(t4_fromWhere)
 
def reqx(rs):
    for x in range(t4_fromWhere, 0, -1):
        username=randomUsername()
        username2=randomUsername2()
        username3=randomUsername3()
        username4=randomUsername4()
        url = f"https://www.tiktok.com:443/@{username}?lang=en"
        url2 = f"https://www.tiktok.com:443/@{username2}?lang=en"
        url3 = f"https://www.tiktok.com:443/@{username3}?lang=en"
        url4 = f"https://www.tiktok.com:443/@{username4}?lang=en"
        cookies = {"tt_csrf_token": "s4JlvLfVoAjEl0fy5B2Cebo-", "ttwid": "1%7CYEAaN2jDV6pMLAm1wXm0OaKICYWJ7H25t66ancXJaRI%7C1646924400%7Cce9ec8814425f957765a9a5194883858e00662cb8ec3a2bceb726101b1bd130d", "msToken": "ZIzDsQa1IJPHU8eYdM6O5zl63rBQxktJ3JB223adizD562pVc1U2kSTpQkwvowNy-INE-1tOek4dClXvFWwQ32clU6-OFPNlDuV5lkF6bN_qFfv3f813ZnAzevic139CC3G-K", "_abck": "FB2E114C7CA6A41DCAB57D5C6D1FF2D3~-1~YAAQ12RDF3wZ/1J/AQAA8aRFdAe0ypCb1IsSM1bDK0hG2D1DeCIFtOk1/puRKMR1SGm6/tein5arAO6UlMrLQHQzsH0ao+esKvGYZ132duXaYvFwB0Q0yZP9i0fVVdqYLZzZ0FEAJ0QOLcFoAdAw+vJW9yc6i2+7zpCHARhMjCAKCVExUyVH1UFhqAKoAQ/eC4Q6B48vCyX2UbfY+0sgWhI5jPi1RVnlD43Jdbksx9qksTHPFBHEIk6MXFcTzNI3Lb/+kNE+EhB01Vpsrw92zkAEi9S3leoHquhYXnqJY45rOcrEK6M5yWkPdwIdU2GSM6no4YlAP1Fg5RkUBsUvCJ07k3UZ97jQDChLgSun4XE7gN9pQFt3O0pgYc1efpphatEuvqPC4otuMsA==~-1~-1~-1", "bm_sz": "C0437DB853794D2164CF2DFE6EF20188~YAAQpTNWsrKDX1N/AQAa1s0/dA8wPD/gAwgLeYS4xevm9ceSHkA6Wr4pBlrj118KZxoxJsJTT8qKj+0ScoqxDaUV3C+2B4Sbw0/ubHZA+Hv8VAKwTHhGo1KyboEECDKXUx9ha+rLbMPOAsV4tRz4PcSJX9EA8mtuujNWGDlG/+hClt12X6LHZWyRmSkEhJ1NXnGt3gqWwCT1/UvPW0oJ5bMDrin3PqXCxV+xupUa0mK9dwbfDJ1mr1C5u0kqaZwAifA9nk9giNzGcPycfd1jQg8BkKkES27HENEOJqVSEmZsvHU=~3418873~3452511", "csrf_session_id": "42a24e8f5acc762d130a74ea2e165732", "s_v_web_id": "verify_l0l3blrw_Hat792HT_PCkG_4FgU_BPgq_LMApKKcr17oE", "ak_bmsc": "FE51FB814EC818836C53E9347AEBDBE3~000000000000000000000000000000~YAAQpTNWssC1XnN/A1AASvA/dA8t2A7p32sozBHbGFNvOtKWJNKoK2GOP5k9dqTMwXvYsoNQJG1oH9lEGUPMGClp2UUG+lXuPQMEUZ6SrxTJqIjIJyzRG7QR6nSmkRZd1nQYEzACpISzuLQFbaxTc6Na8xwoy500FAKVEGH3joFnhGtYTnW77T4mosZ7h/UpgigkIi1/vIDHGZ6FNJxME0Z5n+Jj6TD0TdWe29cMD0er7l0jyrv25dkOeL12IGlonSKzrfJLYdXewLP1Unmqeyl2lI56Dq+EahdazomLQKh3bUXwn2B3H9bUedBva0W9xM9T3NgeJOmLdjtgrrJSUFbuegFxY4kUVYe5LW0ZuZC3sxP8+CGsxhuBkzUKFEcSQZCNysipzLPz", "bm_sv": "74C17ADCC4635958C89E7007F3814A3B~sjm7m1MG2uEXHLzuABgnCUm6Ob13P+Xq/rvmL0Os/bUYV9LHQFOm04l2JUHEkkJdB7LR8Wk3imDI5crYvBFGPy7Zfp1JAgrnbuDYV0w5Fnfc1W/cSBEAcm+2VVg9VQm3ZqPjI2TcSRUtG64bhIFDd/5JYa6a8Hv11/7i55hYwcs=", "bm_mi": "F34001AABE0E401E3E8DB5C7DA9168FA~A9I2kZ1R12XUtm0rWHS38gI3PC7lJsGyq2gi0+hqKKd9N12IqyElx4XsFehA4D9/XTOCAufsj7pTRYj8S15ViRlHsGLdwtxehWr5n50bnKqPBZHeGrmfz12XEcxlfnZjbZcKrnKMnbGOq6G5UC+5NkQvkK1msxMI3bVan9a3uGXcE/8+V7pz1zTxd4GIZDwwbYMx91aApBCDDA0czxoGO3urnaVdWBgjY31IsexG641HDdY=", "passport_csrf_token": "8437c121ff2a7a202124c76a344a82ca", "passport_csrf_token_default": "84f7c651f12a7a202524176a341a82ca", "odin_tt": "d0a120c1f44812492120fc5900d9f6b354ada80859e2c3246041b9d55710645f467a294393836381f6c0056baf3c94d28ffef5eece9e47dafbe33d36a2ac694b546de986d7eb76787b92afe1b36bb5b99", "cmpl_token": "AgQQAAQQ_F-RMpbIXO7cW_R08-EuVAjzef1Q0YMFNVw", "passport_auth_status": "21abbe6c62512eee8ad85d5b65dd624c%2C", "passport_auth_status_ss": "21abbe6c62512eee8ad85d5b65dd624c%2C", "sid_guard": "f032143860a0a82a2d4209cfd20581de%7C1646923195%7C5114000%7CMon%2C+09-May-2022+14%3A39%3A55+GMT", "uid_tt": "dc515cda7018d62b36f15ce91c1186dcff813fd04d1f1c56925c6a9e130be585", "uid_tt_ss": "dc5a5cda70d8d62b36f15ce91c1186dcff813fd04d111c56925c6a9e2a0be585", "sid_tt": "f095443860a0a13a2d4509cfd20581de", "sessionid": "f095443813a0a82a2d4509cfd20581de", "sessionid_ss": "f135443860a0a82a213509cfde0581de", "sid_ucp_v1": "1.0.0-KDA5Mjg4NDIyYzE2ZTY3ZjY41dRkNzI1ODcwNE31YjY1NzYxYTA0N2YKHwiFiL_2iaL1lGIQu5uokQYwewsgDDC7m6iRBjgIQBIQAxoGbWFsaXZhIiBmMDk1NDQzODYwYTBhODJhMmQ0NTA5Y2ZkMjA1ODFkZQ", "ssid_ucp_v1": "1.0.0-KDA5Mjg4NDIyYzE2ZT13AZjY4ZjRkNzI1ODcwNDRmYjY1NzYxYTA0N2YKHwiFiL_2iaL1QGIQu5uokQYYswsgDDC7m6iRBjgIQBIQAxoGbWFsaXZhIiBmMDkQANDQzODYwYTBhODJhMmQ0NTA5Y2ZkMjA1ODFkZQ", "store-idc": "alisg", "store-country-code": "sa", "tt-target-idc": "alisg", "passport_fe_beating_status": "true", "msToken": "pZ1TCUnUdeojr10fpd_dRNU5e0Q6X5XhwX2I1ktq36DVooH6AJs3EvbNjiu9PNWK3k5m7ZvzyNXbo3mVpGMOr8iMLPycAZ6-vSztANy7mqug3YD1gHPRbZG1giJ3z_6GeNt"}
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.tiktok.com/setting", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
        s=requests.get(url, headers=headers, cookies=cookies, verify=False)
        s2=requests.get(url2, headers=headers, cookies=cookies, verify=False)
        s3=requests.get(url3, headers=headers, cookies=cookies, verify=False)
        s4=requests.get(url4, headers=headers, cookies=cookies, verify=False)
        if s.status_code == 200:
            print(f"[ - ]\x1b[1;38;5;197m {username} \x1b[0m")
            pass
        else:
            print(f"[1 + {s.status_code} ]\x1b[1;38;5;120m {username} \x1b[0m")
            file = open("found1.txt", "a+")
            file.write(f"{username}\n")
            file.close()
        if s2.status_code == 200:
            print(f"[ - ]\x1b[1;38;5;197m {username2} \x1b[0m")
            pass
        else:
            print(f"[ + ]\x1b[1;38;5;120m {username2} \x1b[0m")
            file = open("found2.txt", "a+")
            file.write(f"{username2}\n")
            file.close()
        if s3.status_code == 200:
            print(f"[ - ]\x1b[1;38;5;197m {username3} \x1b[0m")
            pass
        else:
            print(f"[ + ]\x1b[1;38;5;120m {username3} \x1b[0m")
            file = open("found3.txt", "a+")
            file.write(f"{username3}\n")
            file.close()
        if s4.status_code == 200:
            print(f"[ - ]\x1b[1;38;5;197m {username4} \x1b[0m")
            pass
        else:
            print(f"[ + ]\x1b[1;38;5;120m {username4} \x1b[0m")
            file = open("found4.txt", "a+")
            file.write(f"{username4}\n")
            file.close()

possibleCharXXX = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
RanUsernameXXX = ''.join(random.choice(possibleCharXXX) for i in range(t4_fromWhere))
with Pool(processes=5) as pool: #<--- change 100 to 10 if ur pc is shit
    print(pool.map(reqx, RanUsernameXXX))            
