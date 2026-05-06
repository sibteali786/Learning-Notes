ngrok inpect url
`http://127.0.0.1:4040/inspect/http`
### Run ngrok https endpoint to test webhooks locally
ngrok http 5000 
5000 is port for emailControllerAuth2 backend server


### Testing webhooks 
Under mail Settings -> webhook settings
https://app.sendgrid.com/settings/mail_settings/webhook_settings
- use ngrok exposed url ( since it changes regularly ) url to test webhook
- the curl command to run bulk test looks like 
```bash
curl -X POST "https://7344-175-107-227-114.ngrok-free.app/api/bulkEmail/sendBulkEmail/67b4d619aec4b8fb086eee7b" \
  --form-string 'recipients=["sibteali786@gmail.com","ssibteali.ce41ceme@ce.ceme.edu.pk"]' \
  --form-string 'subject=Bulk test SendGrid (2 recipients)' \
  --form-string 'body=<p>Bulk send test to two addresses.</p>' \
  --form-string 'service=sendgrid'
```
here userId after bulkemail and ngrok url should be repalced 


curl command to send emails bulk or single
```bash
curl -X POST "https://0342-175-107-227-114.ngrok-free.app/api/bulkEmail/sendBulkEmail/67b4d619aec4b8fb086eee7b"   --form-string 'recipients=["sibteali786@gmail.com","ssibteali.ce41ceme@ce.ceme.edu.pk"]'   --form-string 'subject=Bulk test SendGrid (2 recipients)'   --form-string 'body=<p>Bulk send test to two addresses.</p>'   --form-string 'service=sendgrid'
```

### Primary db in mongodb
`Contacts`


### Run redis locally to avoid mixing curl commands results
```bash
docker compose -f docker-compose.redis-local.yml up -d
```


### query fro users
```sql
db.users.find({email:"akhan@hillcountrycoders.com"}, {_id: 1, firstName: 1, secondName: 1, email: 1, assignedto: 1}).limit(10)
```
user for reference
```
67b4d619aec4b8fb086eee7b
```
