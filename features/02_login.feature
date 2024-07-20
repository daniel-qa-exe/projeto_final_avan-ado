Feature: login de usuário
    Scenario: login de usuário feito com sucesso

    Given ao usuário estar na página de login
    When o usuário preencher os campos com as credenciais corretas
    And clicar no botão "iniciar sessão" 
    Then o usuário loga com sucesso