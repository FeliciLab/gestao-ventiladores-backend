

class ServiceBase():
    def parser_mongo_response_to_list(self, mongo_response):
        docs = []
        for obj in mongo_response:
            docs.append(obj)

        return docs
