from venv import logger
# Import the module
import json


"""
Load json data
"""

def load_json_data():
    try:
        """
        Open the orders.json file
        """
        with open("C:\\Code\\Agnostiq\\Dynamodb\\data\\data.json") as file:
            """
            Load its content and make a new dictionary
            """
            file  = open("C:\\Code\\Agnostiq\\Dynamodb\\data\\data.json", "a")
            file.write("[")
            for i in range(1,101):
                data = '{"userId":"user'+str(i)+'","_id":"100'+str(i)+'"},'
                file.write(data)
            file.write("]")
            file.close()
            
    except Exception as e:
        print(e)



if __name__ == '__main__':
    load_json_data()