from behave import given, when, then

@given('que existe un usuario llamado "{username}"')
def step_impl_user(context, username):
    context.username = username
    # En un test real consultaríamos a la base de datos
    assert username == "admin"

@when('ingreso la contraseña correcta "{password}"')
def step_impl_pass_correct(context, password):
    context.password = password
    assert password == "admin123"

@when('ingreso la contraseña incorrecta "{password}"')
def step_impl_pass_incorrect(context, password):
    context.password = password
    assert password != "admin123"

@then('el sistema debería validar positivamente')
def step_impl_val_pos(context):
    assert context.username == "admin" and context.password == "admin123"

@then('el sistema debería denegar el acceso')
def step_impl_val_neg(context):
    assert context.password != "admin123"
