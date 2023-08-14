<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>{{ slogan }}</h3>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: {
      default: '',
      required: false,
    },
    slogan: {
      default: '',
      required: false,
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style  lang="scss">
.hello{

  h3 {
  color: #17ADEE ;
  margin-top: 10px;
  font-family: Kiwi Maru;
  font-size: 40px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  width: 900px;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

h1{
    margin: auto;
    color: #64113F;
    text-align: center;
    font-family: Lora;
    font-size: 64px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    width: 592px;
    height: 85px;
    flex-shrink: 0;
}
}

</style>
