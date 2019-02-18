import React, { Component } from 'react'
import '../App.css'
import axios from 'axios'
import * as S from "../styles/styles";
import logo from "../icons/go_calmly_logo.png";
import { navigate, Link } from "@reach/router"



class Mom extends Component {
  constructor () {
    super ()
    this.state = {
      classifications: []
    }
    this.playSound = this.playSound.bind(this)
  }

  playSound () {
    axios.post('http://localhost:5000/sound_calm')
    .then(response => {
        navigate(`/encounter`)
    })
  }

  render () {
    return (
      <S.Background>
        <S.LogoFull src={logo} />
        {this.playSound()}
        <h2>
            Diffuse tension, ignite awareness.
        </h2>
        <br></br><br></br>
        <h3>
            You are being pulled over. Please stay calm.
        </h3>
        <Link to='/encounter'>
        <button>
            Next</button>
        </Link>


      </S.Background>

        
    )
  }
}
export default Mom;