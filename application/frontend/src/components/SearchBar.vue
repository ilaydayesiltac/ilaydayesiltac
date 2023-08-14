<template>
<form class="searchbar_form">
  <input type="text" autocomplete="off" name="input" style="text-indent:17px;" placeholder="Write your domain or keyword" class="searchbar">
  <router-link to="/result"><button type="submit" class="search_btn">Search</button></router-link>
</form>
</template>

<script>
export default {
  name: 'SearchBar',
};
</script>

<style scoped>


.searchbar {
  background: url('../assets/searchicon.png') no-repeat scroll 15px 20px ;
  background-size: 20px;
  padding-left: 25px;
  border: 0;
  border-radius: 60px;
  color: black;
  width: 860px;
  height: 65px;
  border: 1px solid #64113F;
}

.searchbar:focus {
  outline: none;
}

.searchbar::placeholder {
  color: rgba(0, 0, 0, 0.61);
  }

.search_btn {
  border: 0;
  border-radius: 50px;
  color: white;
  padding: 15px 40px;
  background: #64113F;
  position: absolute;
  right: 25px;
  top: 10px;
  cursor: pointer;
  width: 143px;
  height: 49px;
}

.searchbar_form {
  position: relative;
  display: inline-block;
  width: 100%;
}
</style>
