import React, { Component } from 'react'
import './App.css'
import axios from 'axios'
import Webcam from "react-webcam"
import * as S from "./styles/styles";
import logo from "./icons/go_calmly_logo.png";


class App extends Component {
  constructor () {
    super ()
    this.state = {
      classifications: []
    }
    this.handleClick = this.handleClick.bind(this)
  }

  // handleClick () {
  //   axios.get('http://localhost:5000/record')
  //     .then(response => this.setState({classifications: response.data}))
  // }

  handleClick () {
    axios.get('http://localhost:5000/record')
      .then(response => {
        if (response.data.includes('police cruiser') || 
          response.data.includes('ambulance')) {
            this.setState({classifications: response.data})
            console.log('FOUND')
          }
          else {
            this.setState({classifications: response.data})
            setTimeout(this.handleClick, 500)
          }
      })
    
  }

  // handleClick () {
  //   axios.get('http://localhost:5000/record')
  //     .then(function(response) {
  //       this.setState({classifications: response.data})
  //     })
  // }

  render () {
    return (
      <S.Background>
        <S.Logo src={logo} />
        <S.Webcam>
          <Webcam/>
        </S.Webcam>
        <S.Button onClick={this.handleClick}>
          Hi
        </S.Button>
        <S.List>
          {this.state.classifications.map(function(listValue){
            return <li>{listValue}</li>;
          })}
        </S.List>



      </S.Background>

        
    )
  }
}
export default App