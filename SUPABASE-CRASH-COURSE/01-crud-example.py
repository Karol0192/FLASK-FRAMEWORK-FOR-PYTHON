import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase = create_client(url,key)

#>>>>>>>>SELECCIONAR REGISTROS DE TABLA PRODUCTO
#data = supabase.table('producto').select('*').execute()
#print(data)

#>>>>>>>>SELECCIONAR REGISTROS DE TABLA PRODUCTO POR CAMPOS
#data = supabase.table('producto').select('id,nombre').execute()
#print(data)

#>>>>>>>>SELECCIONAR REGISTRO POR FILTRADO
#computadora = supabase.table('producto').select('id,nombre').eq('nombre','Computadora').execute()
#print(computadora)

#>>>>>>>>INSERTAR REGISTROS
#producto = supabase.table('producto').insert({'nombre':'Xbox Series X'}).execute()
#producto = supabase.table('producto').insert({'nombre':'Xbox One X'}).execute()

#>>>>>>>>UPDATED OF DATA
#producto = supabase.table('producto').update({'nombre':'Xbox Series S'}).eq('id',4).execute()