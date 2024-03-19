<template>
  <div class="trip-calculator-page">
    
    <TripCalculator @fetch-trips="fetchTrips"/>

    
    <div v-if="bestPrices.fast_travel" class="trip-card">
      <h3>Viagem Mais Confortável</h3>
      <p>Nome da Empresa: {{ bestPrices.fastTravel.name }}</p>
      <p>Lugar: {{ bestPrices.fast_travel.bed }}</p>
      <p>Tempo: {{ bestPrices.fast_travel.duration }}</p>
      <p>Preço: {{ bestPrices.fast_travel.total_price }}</p>
    </div>

    <div v-if="bestPrices.economical_travel" class="trip-card">
      <h3>Viagem Mais Econômica</h3>
      <p>Nome da Empresa: {{ bestPrices.economicalTravel.name }}</p>
      <p>Lugar: {{ bestPrices.economical_travel.bed }}</p>
      <p>Tempo: {{ bestPrices.economical_travel.duration }}</p>
      <p>Preço: {{ bestPrices.economical_travel.total_price }}</p>
    </div>
  </div>
</template>

<script>
import TripCalculator from './TripCalculator.vue'

export default {
  components: {
    TripCalculator
  },
  data() {
    return {
      bestPrices: {
        fast_travel: null,
        economical_travel: null
      }
    };
  },
}
</script>

<style scoped>

</style>
