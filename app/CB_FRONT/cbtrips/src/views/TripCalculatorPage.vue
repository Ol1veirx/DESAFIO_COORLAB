<template>
  <div class="container-main">
    <div class="trip-calculator-page">
      <div class="calc-header-page">
        <img src="@/assets/icon-calc-trip.png" />
        <h2>Calculadora de Viagens</h2>
      </div>
      <div class="calculator-container">
        <TripCalculator @fetch-trips="fetchBestPrices" />
      </div>
      <div class="destination-container">
        <TripDestination v-if="bestPrices.fastTravel" :trip="bestPrices.fastTravel" />
        <TripDestination v-if="bestPrices.economicalTravel" :trip="bestPrices.economicalTravel" />
      </div>
    </div>
  </div>
</template>

<script>
import TripCalculator from '@/components/TripCalculator.vue';
import TripDestination from '@/components/TripDestination.vue';

import axios from 'axios';

export default {
  components: {
    TripCalculator,
    TripDestination,
  },
  data() {
    return {
      bestPrices: {
        fastTravel: null,
        economicalTravel: null
      },
      selectedDestination: '',
      selectedDate: ''
    }
  },
  methods: {
    async fetchBestPrices() {
      try {
        const response = await axios.post('http://localhost:3000/best-prices', {
          destiny: this.selectedDestination,
          date: ''
        });
        this.bestPrices.fastTravel = response.data.fast_travel;
        this.bestPrices.economicalTravel = response.data.economical_travel;
      } catch (error) {
        console.error("Erro ao buscar destino", error);
        alert("Erro ao buscar destino.");
      }
    }
  }
}
</script>

<style scoped>

.container-main{
  height: 85px;
  background-color: whitesmoke;
  box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.205);
}

.trip-calculator-page{
 position: fixed;
  left: 15%;
  top: 14%;
  width: 80vw;
  box-shadow: 1px 2px 5px rgba(0, 0, 0, 0.363);
  font-family: "Roboto", sans-serif;
}

.calc-header-page{
  display: flex;
  align-items: center;
  justify-items: left;
  gap: 15px;
  padding: 15px;
  text-align: left;
  background-color: rgb(31, 31, 110);
  color: white;
}

.calc-header-page img{
  width: 50px;
}

</style>
