import React, { Component } from 'react';
import './App.css';




class Main extends Component{
    render(){
        return (
            <div className="section no-pad-bot" id="index-banner">
                <div className="row center">
                    <h1 className="header center blue-text">Agriness - Gestão de Produtos</h1>
                </div>
            </div>
        );
    }
}

class App extends Component {
  render() {
    return(
        <div id="container">

            <Main/>
        </div>
    );
  }
}

export default App;
