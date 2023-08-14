<template>
  <div class="vue-tempalte col-lg-12"
       style="display: flex; justify-content: center; align-items: center; width: 100%">
    <form>
      <h3>Forgot Password</h3>
      <br>
      <div class="mb-3">
        <label>Email address</label>
        <input type="email" class="form-control form-control-lg"/>
      </div>
      <br>
      <button type="submit" class="btn btn-dark btn-lg btn-block">Reset password</button>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
