import React, { Component } from 'react'
import '../App.css'
import axios from 'axios'
import * as S from "../styles/styles";
import logo from "../icons/go_calmly_logo.png";
import { navigate, Link } from "@reach/router"



class Encounter extends Component {
  constructor () {
    super ()
    this.state = {
      classifications: []
    }
    this.playSound = this.playSound.bind(this)
  }

  playSound() {
    axios.post('http://localhost:5000/sound_encounter')
      .then(response => {
        navigate('/followup')
      })
  }

  render () {
    return (
      <S.Background>
        <S.Logo src={logo} />
        {this.playSound()}
        <br></br><br></br>
        <h2>
          Analyzing conversation.
        </h2>
        <p>
        <Link to='/followup'>
        <button>
            Next</button>
        </Link>
        </p>

      </S.Background>

    )
  }
}
export default Encounter;