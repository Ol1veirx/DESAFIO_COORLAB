<template>
  <div id="app">
    <MenuComponent></MenuComponent>
    <TripCalculatorPage></TripCalculatorPage>
  </div>
</template>

<script>
import TripCalculatorPage from './views/TripCalculatorPage.vue'
import MenuComponent from './components/MenuComponent.vue'

export default {
  name: 'App',
  components: {
    MenuComponent,
    TripCalculatorPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}
</style>
