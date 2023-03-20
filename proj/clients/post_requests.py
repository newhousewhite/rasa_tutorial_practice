import json
import requests
import sys

auth_token = sys.argv[1]
print(auth_token)
user_id = sys.argv[2]
print(user_id)
data_idx = int(sys.argv[3])

# (1) getting only NLU model responses
# request payload shud have a key "text". See data1_dic_nlu.
rasa_nlu_endpint = "http://localhost:5005/model/parse?token=" + auth_token


# # (2) complete URL for complete interaction
rasa_api_endpint = "http://localhost:5005/webhooks/rest/webhook?token=" + auth_token

data1_dic_nlu = {"text": "hi there"}
data2_dic_nlu = {"text": "I want to buy a pizza"}
data1_dic_inter = {
    "sender": user_id,    # sender ID
    "message": "I want to buy a pizza"
}
data2_dic_inter = {
    "sender": user_id,    # sender ID
    "message": "large"
}
data3_dic_inter = {
    "sender": user_id,    # sender ID
    "message": "veggie"
}
data4_dic_inter = {
    "sender": user_id,    # sender ID
    "message": "are you a bot?"
}

ep_all = {
    1: rasa_nlu_endpint,
    2: rasa_api_endpint
}

data_all = {
    1: data1_dic_nlu,
    2: data2_dic_nlu,
    3: data1_dic_inter,
    4: data2_dic_inter,
    5: data3_dic_inter,
    6: data4_dic_inter,
}

def post_req(data_dic, rasa_endpoint):
    data_json = json.dumps(data_dic)
    res = requests.post(url=rasa_endpoint, data=data_json)
    print(res)
    return res

if __name__ == '__main__':
    if   data_idx in [1, 2]:
        ep = ep_all[1]
    elif data_idx in [3, 4, 5, 6]:
        ep = ep_all[2]
    res = post_req(data_all[data_idx], ep)
    print(res.json())
