from tests.base_case import BaseCase
from unittest import main
import json


class BodyResponseTest(BaseCase):
    def test_all_routes_update_patch_delete_return_empty_body(self):
        ...


    def test_all_routes_marshmallow_validation(self):
        ...


    def test_all_entity_one_get_has_json_response(self):
        ...


    def test_all_entity_one_many_has_json_response(self):
        ...


    def test_all_entity_find_post_has_json_response(self):
        ...


    def test_post_parameter_only_accept_objects_list(self):
        ...


    def test_delete_parameter_only_accept_string_list(self):
        ...


    def test_delete_parameter_can_be_convert_to_objectid(self):
        ...


if __name__ == '__main__':
    main()
