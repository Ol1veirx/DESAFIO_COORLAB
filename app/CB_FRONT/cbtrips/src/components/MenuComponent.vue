<template>
  <div class="menu">
    <ul>
        <img src="@/assets/cbLogo.png">
      <li><router-link to="/" class="router-link">Home</router-link></li>
      <li><router-link to="/trips" class="router-link">Calculadora de Viagens</router-link></li>
    </ul>
  </div>
</template>

<style scoped>
.menu {
  position: fixed;
  left: 0;
  top: 0;
  height: 100%; 
  width: 300px; 
  background-color: rgb(31, 31, 110);
  padding-top: 20px; 
}

.menu img{
    width: 220px;
    margin-bottom: 20px;
}

.menu ul {
  list-style-type: none; 
  padding: 0;
}

.menu ul li {
  margin-bottom: 10px;
}

.menu ul li a {
  color: black;
  text-decoration: none;
  padding: 5px 10px;
  display: block;
}

.menu ul li a:hover {
  background-color: darkblue;
}

.router-link {
  color: white;
  text-decoration: none;
  cursor: pointer;

  font-size: 18px;
}

</style>
