from datetime import datetime

from hamcrest import (
    assert_that,
    all_of,
    has_property,
    starts_with,
    instance_of,
    has_properties,
    equal_to,
)


class GetV1Account:


    @classmethod
    def check_response_values(
            cls,
            response,
            login
    ):
        assert_that(
            response,
            all_of(
                has_property('resource', has_property('login', starts_with(login))),
                has_property('resource', has_property('registration', instance_of(datetime))),
                has_property(
                    'resource', has_properties(
                        {
                            'rating': has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0)
                                }
                            )
                        }
                    )
                ),
                has_property('resource', has_property('roles', instance_of(list))),
                has_property('resource', has_property('online', instance_of(datetime)))
            )
        )