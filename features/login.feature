Feature: Gestión de Accesos Simulados
  Como usuario del sistema SaaS
  Quiero simular el comportamiento de inicio de sesión
  Para comprobar la lógica de validación

  Scenario: Intento de inicio de sesión con credenciales correctas
    Given que existe un usuario llamado "admin"
    When ingreso la contraseña correcta "admin123"
    Then el sistema debería validar positivamente

  Scenario: Intento de inicio de sesión con credenciales incorrectas
    Given que existe un usuario llamado "admin"
    When ingreso la contraseña incorrecta "falsa123"
    Then el sistema debería denegar el acceso
