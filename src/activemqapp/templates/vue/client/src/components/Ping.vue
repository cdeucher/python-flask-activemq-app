<template>
  <div class="container">
    <div v-if="checkUser()" class="form-group">
         {{user}}
    </div>      
    <div class="form-group">
      <ul>
        <ol>
          <li for="anwers" v-for="item in getMessages()" :key="item">
            {{item}}
          </li>              
        </ol>  
      </ul>  
    </div>     

    <div v-if="!checkUser()" class="form-group">
        <label for="name">Nome</label>
        <input type="text" id="name"
                        class="form-control"
                      v-model="user">
        <button type="button" @click="saveName" class="btn btn-primary">Logar</button>              
    </div> 
    <div v-if="checkUser() && checkWinner()" class="form-group">
        <label for="dica">Winner {{getWinner()}}</label>              
    </div>      
    <div v-if="checkUser() && !checkWinner()" class="form-group" style='margin-top: 80px;'>
        <label for="dica">{{getTip()}}</label>
        <input type="text" id="word"
                        class="form-control"
                         v-on:keyup.enter="sendWord"
                      v-model="msg">
        <button type="button" @click="sendWord" class="btn btn-primary">Enviar</button>                
    </div>         
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      host: window.location.href,
      msg: '',
      user: '',
      username: '',
      message: { word:0,tip:'',list:[]},
      winner:''
    };
  },
  methods: {
    saveName(){
      this.username = this.user;
    },
    getWinner(){
      return this.winner;   
    },
    getTip(){
      return this.message.tip;   
    },  
    getMessages(){
      return this.message.list;
    },  
    checkUser(){
       return (this.username != '') ? true : false;
    },
    checkWinner(){
       return (this.winner != '') ? true : false;
    },    
    sendWord() {
      const path = this.host+'/word';
      const auth = {  headers: {
            'Content-Type': 'application/json',
          }
      }
      axios.post(path, {msg:this.msg,user:this.username}, auth).then(response => {
            this.winner = response.data.winner;
            if(this.winner == ''){
              this.msg = '';
            }
      }).catch(e => {
            console.error(e);
      })
    },
    updateWord(){
      const path = this.host+'/msg';
      const auth = {  headers: {
            'Content-Type': 'application/json',
          }
      }      
      axios.post(path,{},auth)
        .then((res) => {
          this.winner  = res.data.winner;
          this.message = res.data;
        })
        .catch((error) => {
          console.error(error);
        });           
    }
  },
  created() {
    this.updateWord()
    setInterval(() => {
        this.updateWord()
    }, 10000)
  },
};
</script>