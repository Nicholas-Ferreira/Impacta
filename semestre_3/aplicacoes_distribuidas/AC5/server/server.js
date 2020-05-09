require('dotenv').config()
const PORT = process.env.PORT || 8080
const jsonServer = require('json-server')
const server = jsonServer.create()
const router = jsonServer.router('./database/db.json')
const middlewares = jsonServer.defaults()

server.use(middlewares)
server.use(router)
server.listen(PORT, () => {
  console.log(`** Server rodando na porta ${PORT} **`)
})