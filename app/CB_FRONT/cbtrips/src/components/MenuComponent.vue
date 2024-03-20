<template>
  <div class="menu">
    <img src="@/assets/cbLogo.png" class="img-fluid mb-3">
    <ul class="nav flex-column">
      <div class="menu-links">
        <li class="nav-item">
          <img src="@/assets/menu-icon-trip.png" />
          <router-link to="/trips" class="nav-link">Calculadora de Viagens</router-link>
        </li>
      </div>
    </ul>
  </div>
</template>

<style scoped>
.menu {
  background-color: rgb(31, 31, 110);
  padding: 20px; 
  font-family: "Roboto", sans-serif;
  box-shadow: 1px 2px 8px rgba(31, 31, 110, 0.685);
}

.menu img {
  width: 220px;
}

.menu ul {
  margin-top: 50px;
}

.menu ul li {
  margin-bottom: 10px;
  cursor: pointer;
}

.menu ul li a {
  color: white;
  text-decoration: none;
}

.menu ul li a:hover {
  background-color: rgb(231, 45, 12);
}

.menu-links .nav-item{
  display: flex;
}

.menu-links .nav-item img{
  width: 30px;
}
.nav-link{
  color: white;
  font-size: 17px;
  font-weight: bold;
}

@media (min-width: 768px) {
  .menu {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%; 
    width: 300px;
    padding-top: 20px; 
    text-align: center; 
  }

  .menu img {
    display: block;
    margin: 0 auto 20px;
    width: 80%; 
  }

  .menu ul {
    display: block;
    text-align: left; 
  }

  .menu ul li {
    margin-bottom: 10px;
    display: block; 
  }
}

@media (max-width: 767px) {
  .menu {
    width: 100%;
    text-align: center;
  }

  .menu img {
    width: 80%;
    margin: 0 auto 20px;
  }

  .menu ul {
    display: inline-block;
  }

  .menu ul li {
    display: inline-block;
    margin-right: 10px;
  }
}
</style>
