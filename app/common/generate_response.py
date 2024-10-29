from .http_code import HTTP_200_OK, HTTP_201_CREATED

def generate_response(data=None, message=None, status=None):
    """
    Toma datos, mensajes y estados, y devuelve un diccionario con los datos, mensajes y estados.
    
    :param data: Los datos que desea devolver al cliente.
    :param message: Este es el mensaje que desea mostrar al usuario.
    :param status: El código de estado HTTP, por defecto es 400 (opcional)
    :return: Un diccionario con las claves: data, message, status.
    """
    
    if status == HTTP_200_OK or status == HTTP_201_CREATED:
        status_bool = True
    else:
        status_bool = False
        
    return {
        "data": data,
        "message": modify_slz_error(message, status_bool),
        "status": status_bool
    }, status
    
def modify_slz_error(message, status):
    """
    Toma un mensaje y un estado y devuelve una lista de errores.
    :param message: El mensaje de error que desea mostrar.
    :param status: El código de estado HTTP que desea devolver.
    :return: Una lista de diccionarios.
    """
    
    final_error = list()
    
    if message:
        if type(message) == str:
            if not status:
                final_error.append({ "error": message })
            else:
                final_error = message
        elif type(message) == list:
            final_error = message
        else:
            for key, value in message.items():
                final_error.append({ "error": str(key) + ": " + str(value[0]) })
    else:
        final_error = None
    return final_error