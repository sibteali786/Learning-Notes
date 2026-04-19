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