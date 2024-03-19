<template>
  <div class="trip-calculator">
    <h2>Calcule o valor da viagem</h2>
    <div class="input-container">
      <label for="destination">Destino</label>
      <select id="destination" v-model="selectedDestination">
        <option value="">Selecione o destino</option>
        <option v-for="destination in destinations" :key="destination.id" :value="destination.city">{{ destination.city }}</option>
      </select>
    </div>
    <div class="input-container">
      <label for="date">Data</label>
      <input type="date" id="date" v-model="selectedDate" />
    </div>
    <button @click="fetchTrips">Buscar</button>

    <div class="trip-cards">
      <div v-if="fastTravel" class="trip-card">
        <h3>Viagem Mais Rápida</h3>
        <p>Nome da Empresa: {{ fastTravel.company_name }}</p>
        <p>Lugar: {{ fastTravel.bed }}</p>
        <p>Duração: {{ fastTravel.duration }}</p>
        <p>Preço Total: {{ fastTravel.total_price }}</p>
      </div>
      <div v-if="economicalTravel" class="trip-card">
        <h3>Viagem Mais Econômica</h3>
        <p>Nome da Empresa: {{ economicalTravel.company_name }}</p>
        <p>Lugar: {{ economicalTravel.bed }}</p>
        <p>Duração: {{ economicalTravel.duration }}</p>
        <p>Preço Total: {{ economicalTravel.total_price }}</p>
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
      economicalTravel: null
    };
  },
  methods: {
    async fetchTrips() {
      try {
        const response = await axios.post('http://localhost:5000/best-prices', {
          city: this.selectedDestination,
          date: this.selectedDate
        });
        this.fastTravel = response.data.fast_travel;
        this.economicalTravel = response.data.economical_travel;
      } catch (error) {
        console.error("Erro ao buscar viagens", error);
        alert("Erro ao buscar viagens.");
      }
    },
    async fetchDestinations() {
      try {
        const response = await axios.get('http://localhost:5000/trips');
        this.destinations = response.data;
      } catch (error) {
        console.error("Erro ao buscar destinos", error);
        alert("Erro ao buscar destinos.");
      }
    }
  },
  mounted() {
    this.fetchDestinations();
  }
}
</script>

<style scoped>

</style>
