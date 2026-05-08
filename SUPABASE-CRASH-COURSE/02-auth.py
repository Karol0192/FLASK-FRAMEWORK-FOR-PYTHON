import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase = create_client(url,key)

email = os.getenv('random_email')
password = 'lollollo'

#user = supabase.auth.sign_up({
#    'email':email,
#    'password':password,
#})

user = supabase.auth.sign_in_with_password({
    'email' : email,
    'password':password
})

print('ID:',user.user.id)
print('EMAIL:',user.user.email)
#print('TOKEN:',user.session.access_token)

#data = supabase.table('producto').select('*').execute()
#print(data)

supabase.auth.sign_out()

data = supabase.table('producto').select('*').execute()
print(data)