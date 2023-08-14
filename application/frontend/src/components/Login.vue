<template>
  <center>
    <div class="vue-tempalte col-lg-12"
         style="display: flex; justify-content: center; align-items: center; width: 100%">
      <form>
        <h3>Sign In</h3>
        <div class="mb-3">
          <label>Email address</label>
          <input type="email" v-model="email" class="form-control form-control-lg"/>
        </div>
        <div class="mb-3">
          <label>Password</label>
          <input type="password" v-model="password" class="form-control form-control-lg"/>
        </div>
        <button @click="signIn" type="submit" class="btn btn-dark btn-lg btn-block">Sign In</button>
        <p class="forgot-password text-right mt-2 mb-4">
          <router-link to="/ForgotPassword">Forgot password ?</router-link>
        </p>
        <div class="social-icons">
          <ul>
            <li><a href="#"><i class="fa fa-google"></i></a></li>
            <li><a href="#"><i class="fa fa-facebook"></i></a></li>
            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
          </ul>
        </div>
      </form>
    </div>
  </center>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    signIn() {
      const formData = new FormData();
      formData.append('email', this.email);
      formData.append('password', this.password);
      axios.post('http://127.0.0.1:5000/sign_in', formData)
        .then((response) => {
          if (response.is_success) {
            this.$router.push('/home');
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
