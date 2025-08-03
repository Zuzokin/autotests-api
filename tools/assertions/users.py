from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal


def assert_create_user_response(
    request: CreateUserRequestSchema, response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema,
):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на создание пользователя.

    :param get_user_response: Ответ API с данными получения пользователя.
    :param create_user_response: Ответ API с данными создания пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(actual=get_user_response.user, expected=create_user_response.user)


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, корректность данных пользователя

    :param actual: Реальный пользователь.
    :param expected: Ожидаемый пользователь.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.email, expected=expected.email, name="email")
    assert_equal(actual=actual.last_name, expected=expected.last_name, name="last_name")
    assert_equal(
        actual=actual.first_name, expected=expected.first_name, name="first_name"
    )
    assert_equal(
        actual=actual.middle_name, expected=expected.middle_name, name="middle_name"
    )
