fetch('http://127.0.0.1:5000/api/alunos')
  .then(resposta => resposta.json())
  .then(dados_da_turma =>{
    const listaElementos = document.getElementById("lista-de-alunos")
    for (let aluno of dados_da_turma){
      const item = document.createElement("li")
      item.textContent = `Nome: ${aluno.nome}, Nota: ${aluno.nota}`
      listaElementos.appendChild(item)
    }
  })