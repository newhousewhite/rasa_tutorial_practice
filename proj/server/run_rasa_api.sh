# pre-requisites
# 0. activate virtualenv: source venv/bin/activate
# 1. run rasa action: python -m rasa run actions
# 2. run ngrok: bash run_ngrok.sh
# 3. update external network webhook_url in credentials.yml: telegram -> webhook_url
# 4. run rasa api: bash run_rasa_api.sh

python -m rasa run \
  --enable-api \
  --cors "*" \
  --debug \
  --auth-token $AUTH_TOKEN \
  --credentials credentials.yml \
  --endpoints endpoints.yml \
  -p 8443