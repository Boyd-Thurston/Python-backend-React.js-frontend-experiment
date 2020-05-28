import { ADD_FRUITS } from "../actions"

const initialState = []

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_FRUITS:
      return action.fruits
    default:
      return state
  }
}

export default reducer