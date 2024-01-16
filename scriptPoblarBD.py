#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Importar faker
from faker import Faker
from faker.providers import *
fake = Faker("es_ES") #Instanciar clase Faker en idioma español

#Importar conector de postgresql
import psycopg2;

try:
    connection = psycopg2.connect( #Cadena de conexión con la base de datos bdcourier desde python
        host = '10.10.10.2',
        user = 'postgres',
        password = 'postgres',
        database = 'bdcourier',
        port = '15532'
    )
    print('Conexion Exitosa a base de datos contenerizada bdcourier de postgresql.')
    cursor = connection.cursor()
    
    #Imprimir la version derl servidor de postgresql
    #cursor.execute("SELECT version();") #Obtener la version del servidor de postgresql
    #row = cursor.fetchone()
    #print(row)
    
    #Obtener los datos de la tabla cliente
    #cursor.execute("SELECT * FROM cliente;")
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(row)
    
    #Insertar datos en base de datos courier tabla "cliente" desde python con faker ********************************************
    numeroRegistrosTablaCliente = 10 #Numero de registros a ingresar en tabla cliente
    for i in range(numeroRegistrosTablaCliente):
        #Datos generados con faker para tabla cliente
        cicliente = str(fake.random_number(digits=10))
        nombrecliente = fake.first_name()
        apellidocliente = fake.last_name()
        direccioncliente = fake.street_address()
        telefonocliente = fake.phone_number().replace(' ','')
        telefonocliente = telefonocliente[2:]
        
        insert_query = """ INSERT INTO cliente (ciCliente,nombreCliente,apellidoCliente,direccionCliente,telefonoCliente) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (cicliente,nombrecliente,apellidocliente,direccioncliente,telefonocliente)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla cliente:",numeroRegistrosTablaCliente)
    
    #Insertar datos en base de datos courier tabla "destinatario" desde python con faker ********************************************
    numeroRegistrosTablaDestinatario = 10 #Numero de registros a ingresar en tabla destinatario
    for i in range(numeroRegistrosTablaDestinatario):
        #Datos generados con faker para tabla destinatario
        cidestinatario = str(fake.random_number(digits=10))
        nombredestinatario = fake.first_name()
        apellidodestinatario = fake.last_name()
        direcciondestinatario = fake.street_address()
        telefonodestinatario = fake.phone_number().replace(' ','')
        telefonodestinatario = telefonodestinatario[2:]
        
        insert_query = """ INSERT INTO destinatario (cidestinatario,nombredestinatario,apellidodestinatario,direcciondestinatario,telefonodestinatario) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (cidestinatario,nombredestinatario,apellidodestinatario,direcciondestinatario,telefonodestinatario)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla destinatario:",numeroRegistrosTablaDestinatario)
    
    #Insertar datos en base de datos courier tabla "tipoenvio" desde python con faker ********************************************
    numeroRegistrosTablaTipoEnvio = 10 #Numero de registros a ingresar en tabla tipoenvio
    for i in range(numeroRegistrosTablaTipoEnvio):
        #Datos generados con faker para tabla tipoenvio
        descripcionTipoEnvio = fake.text(max_nb_chars=120)
        fragilPesado = fake.pybool() #True = 0, Fragil = 1
        
        insert_query = """ INSERT INTO tipoenvio (descripciontipoenvio,fragilpesado) VALUES (%s,%s)"""
        record_to_insert = (descripcionTipoEnvio,fragilPesado)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla tipoenvio:",numeroRegistrosTablaTipoEnvio)
    
    #Insertar datos en base de datos courier tabla "repartidor" desde python con faker ********************************************
    numeroRegistrosTablaRepartidor = 10 #Numero de registros a ingresar en tabla repartidor
    for i in range(numeroRegistrosTablaRepartidor):
        #Datos generados con faker para tabla repartidor
        nombrerepartidor = fake.first_name()
        apellidorepartidor = fake.last_name()
        direccionrepartidor = fake.street_address()
        cargorepartidor = fake.word(ext_word_list=['Repartidor novato', 'Repartidor intermedio', 'Repartidor avanzado'])
        
        insert_query = """ INSERT INTO repartidor (nombrerepartidor,apellidorepartidor,direccionrepartidor,cargorepartidor) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (nombrerepartidor,apellidorepartidor,direccionrepartidor,cargorepartidor)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla repartidor:",numeroRegistrosTablaRepartidor)

    #Insertar datos en base de datos courier tabla "estadoencomienda" desde python con faker ********************************************
    numeroRegistrosTablaEstadoEncomienda = 10 #Numero de registros a ingresar en tabla estadoencomienda
    for i in range(numeroRegistrosTablaEstadoEncomienda):
        #Datos generados con faker para tabla estadoencomienda
        activoEncomienda = fake.pybool() #Encomienda inactiva = 0, Encomienda activa = 1
        if(activoEncomienda == True):
            encomienda = 'Encomienda activa'
        else:
            encomienda = 'Encomienda inactiva'
        fechaEstado = fake.date()
        
        insert_query = """ INSERT INTO estadoencomienda (activoEncomienda,fechaEstado) VALUES (%s,%s)"""
        record_to_insert = (encomienda,fechaEstado)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla estadoEncomienda:",numeroRegistrosTablaEstadoEncomienda)
    
    #Insertar datos en base de datos courier tabla "ticket" desde python con faker ********************************************
    numeroRegistrosTablaTicket = 10 #Numero de registros a ingresar en tabla ticket
    for i in range(numeroRegistrosTablaTicket):
        #Datos generados con faker para tabla ticket
        descripcionTicket = fake.text(max_nb_chars=120) 
        fechaCreacion = fake.date()
        fechaActualizacion = fake.date()
        costoEncomienda = fake.numerify('###.##')
                
        insert_query = """ INSERT INTO ticket (descripcionticket,fechacreacion,fechaactualizacion,costoencomienda) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (descripcionTicket,fechaCreacion,fechaActualizacion,costoEncomienda)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla ticket:",numeroRegistrosTablaTicket)
    
    #Insertar datos en base de datos courier tabla "ruta" desde python con faker ********************************************
    numeroRegistrosTablaRuta = 10 #Numero de registros a ingresar en tabla ruta
    for i in range(numeroRegistrosTablaRuta):
        #Datos generados con faker para tabla ruta
        origen = fake.city()
        destino = fake.city()
                
        insert_query = """ INSERT INTO ruta (origen,destino) VALUES (%s,%s)"""
        record_to_insert = (origen,destino)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla ruta:",numeroRegistrosTablaRuta)
    
    #Insertar datos en base de datos courier tabla "encomienda" desde python con faker ********************************************
    #Obtener estados de tabla estadoencomienda
    cursor.execute("SELECT idestado FROM estadoencomienda;")
    rows = cursor.fetchall()
    arrayIdEstadoEncomienda = []
    for row in rows:
        auxiliar = row[0]
        arrayIdEstadoEncomienda = arrayIdEstadoEncomienda + [auxiliar]
    
    numeroRegistrosTablaEncomienda = 10 #Numero de registros a ingresar en tabla encomienda
    for i in range(numeroRegistrosTablaEncomienda):
        #Datos generados con faker para tabla ruta
        idEstado = arrayIdEstadoEncomienda[i]
        tipoEncomienda = fake.word(ext_word_list=['maritima', 'aerea', 'terrestre'])
        altura = fake.numerify('###') #En cm
        peso = fake.numerify('###')#En cm
        descripcionEncomienda = fake.text()
        categoria = fake.word(ext_word_list=['Categoria A: Documentos', 'Categoria B: 4x4','Categoria C: 100 Kg $5000','Categoria D: Prendas de vestir', 'Categoria E: Medicinas', 'Categoria F: Libros y equipos computacion', 'Categoria G: Numero familiar de migrante ecuatoriano'])
                
        insert_query = """ INSERT INTO encomienda (idestado,tipoencomienda,altura,peso,descripcionencomienda,categoria) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (idEstado,tipoEncomienda,altura,peso,descripcionEncomienda,categoria)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla encomienda:",numeroRegistrosTablaEncomienda)
    
    #Insertar datos en base de datos courier tabla "envio" desde python con faker ********************************************
    #Obtener estados de tabla ticket
    cursor.execute("SELECT idticket FROM ticket;")
    rows = cursor.fetchall()
    arrayIdTicket = []
    for row in rows:
        auxiliar = row[0]
        arrayIdTicket = arrayIdTicket + [auxiliar]
        
    #Obtener estados de tabla destinatario
    cursor.execute("SELECT iddestinatario FROM destinatario;")
    rows = cursor.fetchall()
    arrayIdDestinatario = []
    for row in rows:
        auxiliar = row[0]
        arrayIdDestinatario = arrayIdDestinatario + [auxiliar]
        
    #Obtener estados de tabla ruta
    cursor.execute("SELECT idruta FROM ruta;")
    rows = cursor.fetchall()
    arrayIdRuta = []
    for row in rows:
        auxiliar = row[0]
        arrayIdRuta = arrayIdRuta + [auxiliar]
    
    #Obtener estados de tabla cliente
    cursor.execute("SELECT idcliente FROM cliente;")
    rows = cursor.fetchall()
    arrayIdCliente = []
    for row in rows:
        auxiliar = row[0]
        arrayIdCliente = arrayIdCliente + [auxiliar]
    
    #Obtener estados de tabla tipoenvio
    cursor.execute("SELECT idtipoenvio FROM tipoenvio;")
    rows = cursor.fetchall()
    arrayIdTipoEnvio = []
    for row in rows:
        auxiliar = row[0]
        arrayIdTipoEnvio = arrayIdTipoEnvio + [auxiliar]
    
    
    #Obtener estados de tabla encomienda
    cursor.execute("SELECT idencomienda FROM encomienda;")
    rows = cursor.fetchall()
    arrayIdEncomienda = []
    for row in rows:
        auxiliar = row[0]
        arrayIdEncomienda = arrayIdEncomienda + [auxiliar]
    
    #Obtener estados de tabla repartidor
    cursor.execute("SELECT idrepartidor FROM repartidor;")
    rows = cursor.fetchall()
    arrayIdRepartidor = []
    for row in rows:
        auxiliar = row[0]
        arrayIdRepartidor = arrayIdRepartidor + [auxiliar]
    
    numeroRegistrosTablaEnvio = 10 #Numero de registros a ingresar en tabla envio
    for i in range(numeroRegistrosTablaEnvio):
        #Datos generados con faker para tabla envio
        idTicket = arrayIdTicket[i]
        idDestinatario = arrayIdDestinatario[i]
        idRuta = arrayIdRuta[i]
        idCliente = arrayIdCliente[i]
        idTipoEnvio = arrayIdTipoEnvio[i]
        idEncomienda = arrayIdTipoEnvio[i]
        idRepartidor = arrayIdRepartidor[i]
        duracionEnvio = fake.time()
        
        insert_query = """ INSERT INTO envio (idticket,iddestinatario,idruta,idcliente,idtipoenvio,idencomienda,idrepartidor,duracionenvio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (idTicket,idDestinatario,idRuta,idCliente,idTipoEnvio,idEncomienda,idRepartidor,duracionEnvio)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
          
    count = cursor.rowcount
    print("Registros insertados exitosamente en tabla envio:",numeroRegistrosTablaEnvio)
    
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print('Conexión finalizada')


# In[ ]:




