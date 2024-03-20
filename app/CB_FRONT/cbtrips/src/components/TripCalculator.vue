<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-6">
        <div class="trip-calculator">
          <div class="input-calculator">
            <div class="header-calc">
              <img src="@/assets/icon-calc-header.png" class="img-fluid mb-3">
              <h2>Calcule o valor da viagem</h2>
            </div>
            <div class="form-group">
              <label for="destination">Destino</label>
              <select id="destination" class="form-control" v-model="selectedDestination">
                <option value="">Selecione o destino</option>
                <option v-for="destination in destinations" :key="destination.id" :value="destination.city">{{ destination.city }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="date">Data</label>
              <input type="date" id="date" class="form-control" v-model="selectedDate" />
            </div>
            <button @click="fetchTrips" class="btn btn-primary btn-search">Buscar</button>
          </div>
        </div>
      </div>

      <div class="popup" v-if="showPopup">
        <div class="popup-content">
          <p>Nenhuma data/destino selecionado(a).</p>
          <button @click="hidePopup" class="btn btn-primary btn-popup">OK</button>
        </div>
      </div>

      <div class="col-md-6">
        <div class="trip-cards">
          <div v-if="!fastTravel && !economicalTravel" class="" style="">
            <div class="trip-card-message">
              <p>Nenhum dado selecionado</p>
            </div>
          </div>
          
          <div v-if="fastTravel" class="card trip-card trip-card-fast">
            <div class="card-body">
              <img class="icon-cards" src="@/assets/icon-card-fast.png"/>
              <div class="vertical-dotted-line"></div>
              <div class="content-card-fast">
                <h3 class="card-title">Viagem Mais Rápida</h3>
                <p class="card-text"><span class="font-weight-bold">Nome da Empresa:</span> {{ fastTravel.company_name }}</p>
                <p class="card-text"><span class="font-weight-bold">Poltrona:</span> {{ fastTravel.bed }}</p>
                <p class="card-text"><span class="font-weight-bold">Duração:</span> {{ fastTravel.duration }}</p>
                <p class="card-text"><span class="font-weight-bold">Preço Total:</span> {{ fastTravel.total_price }}</p>
              </div>
            </div>
          </div>
          <div v-if="economicalTravel" class="card trip-card trip-card-economical">
            <div class="card-body">
              <img class="icon-cards" src="@/assets/icon-card-economic.png"/>
              <div class="vertical-dotted-line"></div>
              <div class="content-card-fast">
                <h3 class="card-title">Viagem Mais Econômica</h3>
                <p class="card-text"><span class="font-weight-bold">Nome da Empresa:</span> {{ economicalTravel.company_name }}</p>
                <p class="card-text"><span class="font-weight-bold">Leito:</span> {{ economicalTravel.bed }}</p>
                <p class="card-text"><span class="font-weight-bold">Duração:</span> {{ economicalTravel.duration }}</p>
                <p class="card-text"><span class="font-weight-bold">Preço Total:</span> {{ economicalTravel.total_price }}</p>
              </div>
            </div>
          </div>
          <div v-if="resultsVisible">
            <button @click="clearResults" class="btn btn-secondary btn-cards-clear">Limpar Resultados</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedDestination: '',
      selectedDate: '',
      destinations: [], 
      fastTravel: null,
      economicalTravel: null,
      showPopup: false
    };
  },
  methods: {
    async fetchTrips() {
      if (!this.selectedDestination || !this.selectedDate) {
        this.showPopup = true;
        return; 
      }
      
  
      try {
        const response = await axios.post('http://localhost:3000/best-prices', {
          city: this.selectedDestination,
          date: this.selectedDate
        });
        this.fastTravel = response.data.fast_travel;
        this.economicalTravel = response.data.economical_travel;
        this.resultsVisible = true;
    } catch (error) {
        console.error("Erro ao buscar viagens", error);
      }
    },
    hidePopup() {
      
      this.showPopup = false;
    },
    clearResults() {
      this.fastTravel = null;
      this.economicalTravel = null;
      this.resultsVisible = false;
    },
    async fetchDestinations() {
      try {
        const response = await axios.get('http://localhost:3000/trips');
        this.destinations = response.data;
      } catch (error) {
        console.error("Erro ao buscar destinos", error);
      }
    }
  },
  mounted() {
    this.fetchDestinations();
  }
}
</script>

<style scoped>

.trip-calculator {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 15px;
  font-family: "Roboto", sans-serif;
}

.input-calculator {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 25px;
  background-color: rgb(246, 247, 248);
  padding: 45px;
  height: 500px;
  border-radius: 8px;
  box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.171)
}

.form-group{
  margin-bottom: 20px;
}

.form-group label {
  font-size: 22px;
  color: black;
  width: 350px;
}

.header-calc{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.header-calc img{
  width: 50px;
}

.header-calc h2{
  font-size: 27px;
}

.btn-search{
  width: 150px;
}

.input-calculator button {
  margin-top: 15px;
}

.trip-cards {
  padding-top: 30px; 
  margin-bottom: 8px;
}

.trip-card-fast{
  margin: 10px;
  box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.233);
  background-color: rgba(255, 0, 0, 0.103);
}

.trip-card-economical{
  margin: 10px;
  box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.144);
  background-color: rgba(0, 128, 0, 0.089);
}

.card-body{
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.card-body .icon-cards{
  width: 160px;
}

.vertical-dotted-line {
  border-left: 4px dotted black; 
  height: 190px; 
}


.card-body h3{
  padding: 6px;
  color: rgb(255, 255, 255);
  font-weight: bold;
  border-radius: 8px;
  border: none;
  box-shadow: 1px 1px 8px rgba(0, 0, 0, 0.13);
} 

.card-body p {
  font-size: 18px;
}

.card-body span {
  font-weight: bold;
}

.trip-card-economical .card-body h3 {
  background-color: rgba(5, 175, 5, 0.603);
}

.trip-card-fast .card-body h3{
  background-color: rgb(235, 2, 2);
  font-style: italic;
}

.trip-card-message{
  font-size: 25px;
  font-weight: bold;
}

.btn-cards-clear{
  background-color: rgb(31, 31, 110);
  border: none;
  font-weight: bold;
  box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.11);
}

.popup {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  z-index: 9999; 
}

.popup-content {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  height: 200px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); 
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

.btn-popup{
  width: 100px;
}

.popup p {
  margin-bottom: 15px;
  font-size: 23px
}

</style>
