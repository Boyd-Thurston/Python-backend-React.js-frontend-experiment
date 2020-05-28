import request from 'superagent'

const baseUrl = 'http://localhost:8000/api'

export function getFruit() {
  return request.get(`${baseUrl}/fruitbowl`)
    .then(res => {
      return res.body
    })
}