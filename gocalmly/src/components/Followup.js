import React, { Component } from 'react'
import '../App.css'
import axios from 'axios'
import {Link} from "@reach/router"
import * as S from "../styles/styles";
import logo from "../icons/go_calmly_logo.png";
import { navigate } from "@reach/router"
import followup from "../icons/followup.png";


class Mom extends Component {
  constructor () {
    super ()
    this.state = {
      classifications: []
    }
    this.playSound = this.playSound.bind(this)
  }

  playSound () {

  }

  render () {
    return (
      <S.Background>
        <S.LogoFull src={logo} />
        <br></br>
        <S.Followup src={followup} />
    
      </S.Background>

        
    )
  }
}
export default Mom;