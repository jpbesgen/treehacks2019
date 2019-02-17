import React, { Component } from 'react';
import { Router, Link } from "@reach/router"
import Home from "./components/Home";
import Encounter from "./components/Encounter";
import Calm from "./components/Calm";

import * as S from "./styles/styles";
import './App.css';


class App extends Component {
  render() {
    return (
      <S.Background>
        <Router>
          <Home path="/"/>
          <Encounter path="/encounter"/>
          <Calm path="/calm"/>
        </Router>
      </S.Background>
    );
  }
}

export default App;