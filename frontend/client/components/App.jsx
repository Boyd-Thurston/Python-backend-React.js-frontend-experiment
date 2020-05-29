import React from 'react'
import { connect } from 'react-redux'

import { fetchFruit } from '../actions'

export class App extends React.Component {

  componentDidMount(){
    this.props.dispatch(fetchFruit())
  }

  render(){
    return (
      <h1>React development has begun!</h1>
    )
  }
}

export default connect()(App)
