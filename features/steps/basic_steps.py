from behave import given, then

@given('un escenario básico')
def step_impl_given(context):
    pass

@then('la prueba debe pasar sin errores')
def step_impl_then(context):
    assert True
