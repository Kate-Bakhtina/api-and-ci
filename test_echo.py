from echo import Echo

class TestEcho:

    example = Echo()

    def __get_status(self, result):
        return result.get("status")

    def __get_response(self, result):
        return result.get("response")


    def test_get(self):
        result = self.example.get()
        status = self.__get_status(result)
        args = self.__get_response(result).get("args")

        assert status == 200
        assert args.get("page") == "1"

    def test_post(self):
        result = self.example.post()
        status = self.__get_status(result)
        form = self.__get_response(result).get("form")

        assert status == 200
        assert form.get("login") == "Ekaterina"
        assert form.get("password") == "123"

    def test_patch(self):
        result = self.example.patch()
        status = self.__get_status(result)
        args = self.__get_response(result).get("args")
        data = self.__get_response(result).get("data")

        assert status == 200
        assert args.get("user") == "1"
        assert data == "I like drinking a coffee"

    def test_put(self):
        result = self.example.put()
        status = self.__get_status(result)
        args = self.__get_response(result).get("args")
        form = self.__get_response(result).get("form")

        assert status == 200
        assert args.get("user") == "1"
        assert form.get("login") == "Kate"
        assert form.get("password") == "456"

    def test_delete(self):
        result = self.example.delete()
        status = self.__get_status(result)
        args = self.__get_response(result).get("args")

        assert status == 200
        assert args.get("user") == "1"