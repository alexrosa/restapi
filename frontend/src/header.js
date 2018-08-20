import React, {Component} from "react";
import {Link} from 'react-router-dom';

class Header extends Component{

    render(){
        return (
          <nav className="light-blue">
            <div className="nav-wrapper container">

                <a id="logo-container" href="/" className="brand-logo"><img src={process.env.PUBLIC_URL+'logo_agriness.png'} alt={"Logo Agriness"} height="67px"/></a>
                <ul className="right hide-on-med-and-down">
                    <li><Link to="/funcionario" >Funcionário</Link></li>
                    <li><Link to="/materiaprima" >Matéria Prima</Link></li>
                    <li><Link to="/produto" >Produto</Link></li>
                </ul>
            </div>

          </nav>
        );
    }
}

export default Header;