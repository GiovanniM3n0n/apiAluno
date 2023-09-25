# apiAluno

API de Controle de Disciplinas e Tarefas de Aluno Esta é uma API desenvolvida em Django para auxiliar os alunos a gerenciarem suas disciplinas e tarefas. A API oferece funcionalidades para criar, listar, atualizar e excluir alunos, disciplinas e tarefas, bem como associar tarefas a disciplinas e alunos.

Modelos de Dados A API possui três modelos de dados principais:

Modelo Aluno Campos: nome (string): Nome do aluno. email (string): Endereço de e-mail do aluno. Modelo Disciplina Campos: nome (string): Nome da disciplina. descricao (string): Descrição da disciplina. Modelo Tarefa Campos: titulo (string): Título da tarefa. descricao (string): Descrição da tarefa. data_entrega (date): Data de entrega da tarefa. concluida (boolean): Indica se a tarefa está concluída. Relacionamentos: Aluno: Uma tarefa pertence a um aluno. Disciplinas: Uma tarefa pode estar associada a uma ou mais disciplinas. Funcionalidades da API A API inclui as seguintes funcionalidades:

Listagem de Alunos:

Endpoint: /api/alunos/ Método: GET Descrição: Retorna a lista de todos os alunos. Criação de um Aluno:

Endpoint: /api/alunos/ Método: POST Descrição: Permite a criação de um novo aluno. Detalhes do Aluno:

Endpoint: /api/alunos// Método: GET Descrição: Retorna detalhes de um aluno específico com base no ID. Atualização de um Aluno:

Endpoint: /api/alunos// Método: PUT Descrição: Permite a atualização dos detalhes de um aluno específico com base no ID. Exclusão de um Aluno:

Endpoint: /api/alunos// Método: DELETE Descrição: Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas. Listagem de Disciplinas:

Endpoint: /api/disciplinas/ Método: GET Descrição: Retorna a lista de todas as disciplinas. Criação de uma Disciplina:

Endpoint: /api/disciplinas/ Método: POST Descrição: Permite a criação de uma nova disciplina. Detalhes da Disciplina:

Endpoint: /api/disciplinas// Método: GET Descrição: Retorna detalhes de uma disciplina específica com base no ID. Atualização de uma Disciplina:

Endpoint: /api/disciplinas// Método: PUT Descrição: Permite a atualização dos detalhes de uma disciplina específica com base no ID. Exclusão de uma Disciplina:

Endpoint: /api/disciplinas// Método: DELETE Descrição: Permite a exclusão de uma disciplina específica com base no ID. Todas as tarefas associadas a essa disciplina serão desassociadas. Listagem de Tarefas:

Endpoint: /api/tarefas/ Método: GET Descrição: Retorna a lista de todas as tarefas. Criação de uma Tarefa:

Endpoint: /api/tarefas/ Método: POST Descrição: Cria uma nova tarefa associada a um aluno e a uma ou mais disciplinas. Detalhes de uma Tarefa:

Endpoint: /api/tarefas// Método: GET Descrição: Retorna detalhes de uma tarefa específica com base no ID. Atualização de uma Tarefa:

Endpoint: /api/tarefas// Método: PUT Descrição: Atual
