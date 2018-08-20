import React, {Component} from 'react';
import './App.css';
import axios from "axios/index";
import {uri_server_api} from './index.js';


class Produto extends Component {

    constructor(props){
        super(props);
        this.state = {
            error_message: '',
            nome: '',
            id_funcionario: '',
            produtos: [],
            value: 0,
        };
        this.handleDelete = this.handleDelete.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.renderFuncionarios = this.renderFuncionarios.bind(this);
        this.handleEdit = this.handleEdit.bind(this);
        this.handleSelectSubmit = this.handleSelectSubmit.bind(this);
    }

    getURI = () => {
        return uri_server_api + '/produto/';
    }

    componentWillMount(){
        this.getFuncionarios();
    }

    handleSelectSubmit = (e) => {
        this.setState({value: e.target.value});
    }

    handleSubmit(e){
        e.preventDefault();
        axios.post(this.getURI(), {
            nome: this.state.nome,
            jornada_trabalho: this.state.value,
        }).then(response =>{
            this.setState({
                funcionarios: [response.data,...this.state.funcionarios]
            })
        }).catch(error =>{
            this.setState({
                error_message: error.message,
            });
            console.log(error.message);
        });
    }

    handleEdit(id){
        const funcionarios = this.state.funcionarios;

        axios.get(this.getURI()+id)
            .then(response => this.setState({
                nome: response.data.nome,
                value: response.data.jornada_trabalho,
                funcionarios: funcionarios,
            })
        );
    }

    handleDelete(id){
        const isNotId = func => func.id !== id;
        const updateFuncionarios = this.state.funcionarios.filter(isNotId);
        this.setState({
            funcionarios: updateFuncionarios
        });
        axios.delete(this.getURI()+id);
    }

    getFuncionarios(){
        console.log(this.getURI());
         axios.get(this.getURI()).then(response => this.setState({
            funcionarios: [...response.data]
        }));
    }

    renderFuncionarios(){
        return (
             <div className={"media"}>
                 <h5>Lista de Produtos</h5>

                 <div className="collection with-header">
                   <ul>
                       <li className="collection-header"><h4>Produtos</h4></li>
                      {this.state.produtos.map(produto => (
                          <li key={produto.id} className="collection-item">{produto.nome}</li>
                   ))}
                   </ul>
                 </div>
           </div>
      );
    }

    render(){
        return(
            <div className={"container"}>
                <div className={"row justify-content-center"}>
                    <div className={"col-md-8"}>
                        <div className="card">
                            <div className="card-header">Produto</div>
                                <div className="card-body">
                                    <form id="funcionario" onSubmit={this.handleFuncionarioSubmit}>
                                      <label>
                                          <select onChange={()=>this.handleFuncionarioSelectChange}>

                                          </select>
                                      </label>
                                    </form>

                                    <form onSubmit={this.handleSubmit}>
                                        <label>
                                            Nome:
                                            <input type="Text"
                                                   className="form-group"
                                                   name="nome"
                                                   id="nome"
                                                   label="Nome"
                                                   value={this.state.nome}
                                                   onChange={(e)=> this.setState({nome: e.target.nome})}
                                            />
                                        </label>
                                        <br/>
                                        <label>Jornada de Trabalho:
                                            <select onChange={this.handleSelectSubmit}
                                                    value={this.state.value}
                                                    className="browser-default">
                                                <option value="0">Selecione uma Jornada</option>
                                                <option value="4">4 horas</option>
                                                <option value="6">6 horas</option>
                                                <option value="8">8 horas</option>
                                            </select>
                                        </label>
                                        <br/>
                                        <br/>
                                        <button type="submit" className="btn btn-primary">
                                          Incluir
                                        </button>
                                    </form>
                                    <button onClick={()=>this.setState({
                                            nome: '',
                                            value: 0,
                                        })} className="btn btn-primary right-aligned">
                                          Cancelar
                                        </button>

                                    <hr/>
                                    {this.renderFuncionarios()}
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
        );
    }
}


export default Produto;
