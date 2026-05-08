import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client
import webbrowser

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase = create_client(url,key)

#>>>>>>>>>> VISUALIZAR IMAGEN
"""resp = supabase.storage.from_('image-bucket').get_public_url("xbox-series-x.png")
print(resp)
webbrowser.open(resp)"""

#>>>>>>>>>> DESCARGAR IMAGEN

"""BASEDIR = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(BASEDIR,'img','imagen.png')

data = supabase.storage.from_('image-bucket').download('xbox-series-x.png')
with open(file_path,'wb') as f:
    f.write(data)"""

#>>>>>>>>>> SUBIR IMAGEN A BUCKET
BASEDIR = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(BASEDIR,'img','xbox-series-s.png')

with open(file_path,'rb') as f:
    resp = supabase.storage.from_('image-bucket').upload(
        path='xbox-series-s.png',
        file=f,
        file_options={
            'content-type':'image/png'
        }
    )

print(resp)