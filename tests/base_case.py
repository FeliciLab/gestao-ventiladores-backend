from unittest import TestCase
from run import app
from config.db import db
from .mocks.mock_items import mock_items
import json
from copy import deepcopy
from api.v2.migrations.itens_from_service_order import ItemsMigration


class BaseCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()
        self.mock_items = mock_items
        self.items_from_triagem = ItemsMigration().fetch_items_from_triagem()

    def tearDown(self):
        # Não será apagado para testar performance do BD
        # for collection in self.db.list_collection_names():
        #     self.db.drop_collection(collection)
        # for item in self.inserted_objects:
        #     self.db.remove({'_id': item})
        pass

    def many_make_post(self, mock):
        payload = json.dumps({'content': [mock]})

        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        return response

    def get_mock(self, tipo, nome):
        if tipo == 'item':
            return deepcopy(self.mock_items[nome])
