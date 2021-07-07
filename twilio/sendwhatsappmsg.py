from twilio.rest import Client 
 
account_sid = 'ACb6281eb42e5eb0df5ee904ebf938deb1' 
auth_token = '208667aa1eb06bcd2cf44b8be1bc7233' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='This is test',      
                              to='whatsapp:+60193303762' 
                          ) 
 
print(message.sid)