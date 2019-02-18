import React, { Component } from 'react'
import '../App.css'
import axios from 'axios'
import Webcam from "react-webcam"
import * as S from "../styles/styles";
import logo from "../icons/go_calmly_logo.png";
import { navigate } from "@reach/router"



class Home extends Component {
  constructor () {
    super ()
    this.state = {
      classifications: []
    }
    this.classifyVideo = this.classifyVideo.bind(this)
  }

  classifyVideo () {
    axios.get('http://localhost:5000/record')
      .then(response => {
        if (response.data.includes('police cruiser') || 
          response.data.includes('ambulance')) {
            this.setState({classifications: response.data})
            navigate(`/mom`)
            console.log('FOUND')
            axios.post('http://localhost:5000/send_sms')
          }
          else {
            this.setState({classifications: response.data})
            setTimeout(this.handleClick, 500)
          }
      })
    
  }

  render () {
    return (
      <S.Background>
        <S.Logo src={logo} />
        <S.Webcam>
          <Webcam/>
        </S.Webcam>
        {this.classifyVideo()}
        <S.List>
          {this.state.classifications.map(function(listValue){
            return <li>{listValue}</li>;
          })}
        </S.List>



      </S.Background>

        
    )
  }
}
export default Home