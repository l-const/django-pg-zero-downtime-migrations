from .settings import *  # noqa: F401, F403

INSTALLED_APPS += [  # noqa: F405
    'tests.apps.good_flow_app',
    'tests.apps.bad_rollback_flow_drop_column_with_notnull_default_app',
    'tests.apps.bad_rollback_flow_drop_column_with_notnull_app',
    'tests.apps.bad_rollback_flow_change_char_type_that_safe_app',
    'tests.apps.bad_flow_add_column_with_default_app',
    'tests.apps.bad_flow_add_column_with_notnull_default_app',
    'tests.apps.bad_flow_add_column_with_notnull_app',
    'tests.apps.bad_flow_change_char_type_that_unsafe_app',
]
