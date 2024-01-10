# import funciones.corefile as cf
# cf.MY_DATABASE='data/campers.json'
# def newcamper(campus :dict):
#     data=campus.get('campus').get("campers")
#     camper={
#         "Nroid":'',
#         "Nombre":'',
#         "Apellido":'',
#         "Direccion":'',
#         "Acudiente":{},
#         "telecontacto":{},
#         "Estado":''
#     }
# Acudiente ={
#     "Id":"1",
#     "Nrotel":'666',
#     "Nombre":'Acudiente 1',
#     "Email":'Acudiente@gmail.com'
# }
# phone={
#     "Id":"1",
#     "Nrote":'444',
#     "Ubicacion":'Casa'
# }
# Camper1={
#     "Nroid":'123',
#         "Nombre":'AAA',
#         "Apellido":'BBB',
#         "Direccion":'Cra',
#         "Acudiente":{},
#         "telecontacto":{},
#         "Estado":'I'
# }
# Camper1["Acudiente"].update({str((len(Camper1["Acudiente"])+1.))zfill(3):Acudiente})
# data.update({Camper1["Nroid"]:Camper1})
# campus.get('campus').get("campers").update(data)
# print(json.dumps(campus,indent=4))