/* Crie 3 arquivos HTML: artigos.html, contato.html e erro.html
Coloque qualquer conteúdo para cada página html
Ele deve aparecer o nome do arquivo no path do browser
Qualquer path diferente ele deve mostrar a mensagem erro.html
A leitura dos arquivos html deve ser assincrona
A roda principal "/" deve renderizar artigos.html
*/
var http = require ('http')
var server = http()

server.listen(8081)
    console.log("Servidor rodando na porta 8081")
