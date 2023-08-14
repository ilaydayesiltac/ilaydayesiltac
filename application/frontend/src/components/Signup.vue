<template>
  <center>
    <div class="vue-tempalte col-lg-12"
         style="display: flex; justify-content: center; align-items: center; width: 100%">
      <form>
        <h3>Sign Up</h3>
        <div class="mb-3">
          <p>Email address</p>
          <input type="email" class="form-control form-control-lg" v-model="email"/>
        </div>
        <div class="mb-3">
          <p for="pass">Password</p>
          <input type="password" class="form-control form-control-lg" v-model="password"/>
        </div>
        <button @click="signUp" class="btn btn-dark btn-lg btn-block">Sign Up</button>
        <p class="forgot-password text-right">
          <br>
          Already registered
          <router-link :to="{ name: 'login' }">sign in?</router-link>
        </p>
      </form>
    </div>
  </center>
</template>

<script>

import axios from 'axios';

export default {
  name: 'sign-up',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    signUp() {
      const formData = new FormData();
      formData.append('email', this.email);
      formData.append('password', this.password);
      axios.post('http://127.0.0.1:5000/sign_up', formData)
        .then((response) => {
          if (response.is_success) {
            console.log('notify olarak mesaj basılacak');
          }
        })
        .catch((error) => {
          console.log('notify olarak response.fail mesajı basılacak.', error);
        });
    },
  },
};
</script>
