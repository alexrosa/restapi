import React, {Component} from 'react';
import './App.css';
import axios from "axios/index";
import {uri_server_api} from './index.js';


class MateriaPrima extends Component {

    constructor(props){
        super(props);
        this.state = {
            error_message: '',
            nome: '',
            materias: [],
            quantidade: '',
        };
        this.handleDelete = this.handleDelete.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.renderFuncionarios = this.renderFuncionarios.bind(this);
        this.handleEdit = this.handleEdit.bind(this);
    }

    getURI = () => {
        return uri_server_api + '/materia_prima/';
    }

    componentWillMount(){
        this.getFuncionarios();
    }

    handleSubmit(e){
        e.preventDefault();
        axios.post(this.getURI(), {
            nome: this.state.nome,
            quantidade: this.state.quantidade,
        }).then(response =>{
            this.setState({
                materias: [response.data,...this.state.materias]
            })
        }).catch(error =>{
            this.setState({
                error_message: error.message,
            });
            console.log(error.message);
        });
    }

    handleEdit(id){
        const materias = this.state.materias;

        axios.get(this.getURI()+id)
            .then(response => this.setState({
                nome: response.data.nome,
                quantidade: response.data.quantidade,
                materias: materias,
            })
        );
    }

    handleDelete(id){
        const isNotId = func => func.id !== id;
        const updateMaterias = this.state.materias.filter(isNotId);
        this.setState({
            materias: updateMaterias
        });
        axios.delete(this.getURI()+id);
    }

    getFuncionarios(){
        console.log(this.getURI());
         axios.get(this.getURI()).then(response => this.setState({
            materias: [...response.data]
        }));
    }

    renderFuncionarios(){
        return (
             <div className={"media"}>
                 <h5>Lista de Matérias Primas</h5>
               <table>
                   <thead>
                        <tr>
                            <td>Nome:</td>
                            <td>Quantidade:</td>
                            <td>...</td>
                        </tr>

                   </thead>
                   <tbody>
                   {this.state.materias.map(materiaprima => (
                    <tr key={materiaprima.id}>
                        <td>{materiaprima.nome}</td>
                        <td>{materiaprima.quantidade}</td>
                        <td>
                            <button onClick={()=> this.handleEdit(materiaprima.id)}
                                    className={"btn"}>Editar
                            </button>
                            <button onClick={()=> this.handleDelete(materiaprima.id)}
                                    className="btn btn-sm btn-warning float-right">
                                Excluir
                            </button>
                        </td>
                    </tr>
                   ))}
                   </tbody>
                </table>
           </div>
      );
    }

    render(){
        return(
            <div className={"container"}>
                <div className={"row justify-content-center"}>
                    <div className={"col-md-8"}>
                        <div className="card">
                            <div className="card-header">Matéria Prima</div>
                                <div className="card-body">
                                    <form onSubmit={this.handleSubmit}>
                                        <label>
                                            Nome:
                                            <input type="Text"
                                                   className="form-group"
                                                   name="nome"
                                                   id="nome"
                                                   label="Nome"
                                                   value={this.state.nome}
                                                   onChange={(e)=> this.setState({nome: e.target.value})}
                                            />
                                        </label>
                                        <br/>
                                        <label>Quantidade:
                                             <input type="Text"
                                                   className="form-group"
                                                   name="quantidade"
                                                   id="quantidade"
                                                   label="Quantidade"
                                                   value={this.state.quantidade}
                                                   onChange={(e)=> this.setState({quantidade: e.target.value})}/>
                                        </label>
                                        <br/>
                                        <br/>
                                        <button type="submit" className="btn btn-primary">
                                          Incluir
                                        </button>
                                    </form>
                                    <button onClick={()=>this.setState({
                                            nome: '',
                                            quantidade: 0}
                                            )} className="btn btn-primary right-aligned">
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

export default MateriaPrima;
