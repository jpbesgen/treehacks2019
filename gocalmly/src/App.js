import React, { Component } from 'react';
import { Router, Link } from "@reach/router"
import Home from "./components/Home";
import Encounter from "./components/Encounter";
import Mom from "./components/Mom";
import Followup from "./components/Followup"

import * as S from "./styles/styles";
import './App.css';


class App extends Component {
  render() {
    return (
      <S.Background>
        <Router>
          <Home path="/"/>
          <Encounter path="/encounter"/>
          <Mom path="/mom"/>
          <Followup path="/followup"/>
        </Router>
      </S.Background>
    );
  }
}

export default App;