Feature: criação de usuário na área de cadastro
    Scenario: cadastro de usuário feito com sucesso

    Given usuário estar na area de cadastro
    When o usuário preencher os campos com as credenciais
    And clicar no botão "criar conta"
    Then o usuário cadastra com sucesso