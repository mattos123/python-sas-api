from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = "xxx"## defina aqui sua chave rsa
auth = "xxx" ## defina aqui sua authkey
prod_id = 'xxx'#defina aqui seu id de produto da cryptolens
def Authkey(key):
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id=prod_id, \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
        print("Licença invalida: {0}".format(result[1]))
        return False, None
    else:
        print("Licenciamento validado atraves da api.")
        license_key = result[0]
        print(result)
        expiration_date_formatted = license_key.expires.strftime('%d-%m-%Y %H:%M:%S')
        print("Licença expira: " + str(expiration_date_formatted))
        return True, license_key.expires
