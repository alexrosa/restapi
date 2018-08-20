import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Header from './header';
import 'materialize-css/dist/css/materialize.css';
import 'materialize-css/dist/js/materialize.min.js';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Funcionario from './Funcionario';
import MateriaPrima from './MateriaPrima';
import Produto from './Produto';
import registerServiceWorker from './registerServiceWorker';

export const uri_server_api = "http://localhost:5000/api";

ReactDOM.render(
                <BrowserRouter>
                    <div id="container">
                        <Header/>
                        <Switch>
                            <Route exact path="/" exact={true} component={App}/>
                            <Route exact path="/funcionario" component={Funcionario}/>
                            <Route exact path="/materiaprima" component={MateriaPrima}/>
                            <Route exact path="/produto" component={Produto}/>
                        </Switch>
                    </div>
                </BrowserRouter>
                ,
                document.getElementById('root')
);
registerServiceWorker();
