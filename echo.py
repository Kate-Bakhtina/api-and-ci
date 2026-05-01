import requests

class Echo:

    BASE_URL = "https://postman-echo.com/"

    def __init__(self):
        pass

    def __get_result(self, response):
        result = {
            "response": response.json(),
            "status": response.status_code
        }
        return result

    def get(self):
        params = {
            "page": 1
        }
        response = requests.get(self.BASE_URL + "get", params=params)
        return self.__get_result(response)

    def post(self):
        form_data = {
            "login": "Ekaterina",
            "password": "123"
        }
        response = requests.post(self.BASE_URL + "post", data=form_data)
        return self.__get_result(response)

    def put(self):
        params = {
            "user": 1
        }
        form_data = {
            "login": "Kate",
            "password": "456"
        }
        response = requests.put(self.BASE_URL + "put", data=form_data, params=params)
        return self.__get_result(response)

    def patch(self):
        params = {
            "user": 1
        }
        text = "I like drinking a coffee"
        response = requests.patch(self.BASE_URL + "patch", data=text, params=params)
        return self.__get_result(response)

    def delete(self):
        params = {
            "user": 1
        }
        response = requests.delete(self.BASE_URL + "delete", params=params)
        return self.__get_result(response)

