<template>
  <div class="container">
      <h1>Buscar Operadoras</h1>
      <hr />
      <div class="form-todo form-group">
        <p>
          <input placeholder="Insira o dado da empresa que deseja buscar" type="text" name="termo" class="form-control" v-model="termo" />
        </p>
        <button v-on:click="buscarOperadoras" type="submit" class="btn btn-primary">Buscar</button>
      </div>
      <div class="list-group">
        <!-- Faz dois for. Um for para pegar o conteudo de operadoras. E outro for para pegar o conteudo de chave e valor dentro da operadora que esta sendo percorrida pelo primeiro for -->
        <div class="list-group-item" v-for="(operadora, index) in operadoras" :key="index">
          <div v-for="(valor, chave) in operadora" :key="chave">
            <strong>{{ chave }}:</strong> {{ valor }}
          </div>
        </div>
        <hr />
      </div>
    </div>  
</template>

<script>
import axios from 'axios'

export default {
  name: 'ResultadoBuscaComponent',
  data() {
    return {
      operadoras: [],
      termo: ''
    }
  },
  methods: {
    async buscarOperadoras() {
      if(this.termo === ''){
        // Se o campo do termo estiver vazio, exibe um alerta de campo inválido 
        alert("Campo vazio! Insira um valor válido para buscar.")
      }else{
        // Faz a requisição para o backend passando o termo digitado no input
        const response = await axios.get(`http://localhost:5000/buscar_operadoras?termo=${this.termo}`)

        //Armazena a resposta da requisição na variável operadoras
        this.operadoras = response.data;
      }
    }
  }
}
</script>