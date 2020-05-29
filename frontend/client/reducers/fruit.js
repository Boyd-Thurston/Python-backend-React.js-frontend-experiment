import RECEIVE_FRUIT from '../actions'

const initialState = []

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case RECEIVE_FRUIT:
      return fruit
    default:
      return state
  }
}

export default reducer