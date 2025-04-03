<template>
  <div class="container">
    <h1>Relatório CADOP</h1>

    <div class="search-bar">
      <input v-model="busca" placeholder="Buscar por razão social..." />
      <button @click="buscarPorRazaoSocial">Buscar</button>
    </div>

    <table>
      <thead>
        <tr>
          <th>Razão Social</th>
          <th>CNPJ</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in cadopList" :key="item.id">
          <td>{{ item.Razao_Social }}</td>
          <td>{{ item.CNPJ }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cadopList = ref([])
const busca = ref('')

// Busca todos os registros ao carregar a página
const carregarTodos = async () => {
  const { data } = await axios.get('http://localhost:8000/cadop')
  cadopList.value = data
}

// Busca filtrada por razão social
const buscarPorRazaoSocial = async () => {
  if (!busca.value.trim()) {
    await carregarTodos()
    return
  }

  try {
    const { data } = await axios.get(`http://localhost:8000/cadop/${encodeURIComponent(busca.value)}`)
    cadopList.value = data
  } catch (err) {
    console.error('Erro ao buscar:', err)
    cadopList.value = []
  }
}

onMounted(carregarTodos)
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  background-color: #f9f5ff;
  padding: 40px;
  min-height: 100vh;
  color: #333;
}

h1 {
  color: #7c3aed;
  font-size: 26px;
  margin-bottom: 20px;
  text-align: center;
}

.search-bar {
  text-align: center;
  margin-bottom: 20px;
}

.search-bar input {
  padding: 8px;
  font-size: 16px;
  width: 250px;
  margin-right: 10px;
}

.search-bar button {
  padding: 8px 16px;
  background-color: #7c3aed;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-bar button:hover {
  background-color: #6d28d9;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(124, 58, 237, 0.1);
}

th {
  background-color: #c084fc;
  color: white;
  padding: 12px;
  text-align: left;
}

td {
  padding: 12px;
  border-bottom: 1px solid #f3e8ff;
}

tr:nth-child(even) {
  background-color: #f3e8ff;
}

tr:hover {
  background-color: #fde68a;
  transition: 0.3s ease;
  cursor: pointer;
}
</style>
