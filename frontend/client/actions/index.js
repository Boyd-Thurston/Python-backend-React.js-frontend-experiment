import { getFruit } from "../api"

export const RECEIVE_FRUIT = 'RECEIVE_FRUIT'

const receiveFruit = fruit => {
  return {
    type: RECEIVE_FRUIT,
    fruit
  }
}

export const fetchFruit = () => {
  return dispatch => {
    getFruit()
      .then(words => {
        dispatch(receiveFruit(fruit))
      })
  }
}