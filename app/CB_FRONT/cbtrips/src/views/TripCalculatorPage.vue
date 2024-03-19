<template>
  <div class="trip-calculator-page">
    <h2>Calculadora de Viagens</h2>
    <div class="calculator-container">
      
      <TripCalculator @fetch-trips="fetchBestPrices" />
    </div>
    <div class="destination-container">
     
      <TripDestination v-if="bestPrices.fastTravel" :trip="bestPrices.fastTravel" />
      <TripDestination v-if="bestPrices.economicalTravel" :trip="bestPrices.economicalTravel" />
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
    TripDestination
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
        const response = await axios.post('http://localhost:5000/best-prices', {
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

</style>
