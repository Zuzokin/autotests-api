from http import HTTPStatus
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import GetUserResponseSchema

from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response


@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(
    function_user: UserFixture,  # Используем фикстуру для создания пользователя
    private_users_client: PrivateUsersClient,
):
    response = private_users_client.get_user_me_api()

    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(
        create_user_response=function_user.response, get_user_response=response_data
    )

    validate_json_schema(response.json(), response_data.model_json_schema())
