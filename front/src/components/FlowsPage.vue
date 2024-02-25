<template>
  <div>

    <main class="container-fluid mt-5 col-sm-10 offset-sm-1">
      
      <div class="row">
        <section class="col-md-4">
          <div>
            <h2 class="text-start mb-4 text-body-secondary">
              <i class="bi bi-funnel me-3 " style="font-size: 1.5rem;"></i>
              Filtros
            </h2>
            <article>
              <FlowFilters @filter="filtrosAplicados" />
              <ClientList :clients="clients" />
            </article>
          </div>

        </section>
        <aside class="col-sm-12 col-md-8">
          <h2 class="text-start mb-4">Fluxos</h2>
          <div>
            <FlowSearch @search="searchFlows" />
            <FlowList :filters="filters" :searchName="search" :flowData="flows" />
          </div>
        </aside>
      </div>
    </main>

    <body>

    </body>
  </div>
</template>

<script>
import ClientList from './ClientList.vue'
import FlowList from './FlowList.vue'
import FlowFilters from './FlowFilters.vue'
import FlowSearch from './FlowSearch.vue'
export default {
  components: { ClientList, FlowList, FlowFilters, FlowSearch },
  name: 'FlowPage',
  props: {
    msg: String,

  },
  data() {
    return {
      flows: [],
      clients: [],
      filters: [],
      search: ''
    }
  },
  methods: {
    async getJsonData(jsonFile) {
      const response = await fetch(`/database/${jsonFile}.json`);
      const data = await response.json();
      return data;
    },
    filtrosAplicados(filtros) {
      this.filters = filtros;
    },
    searchFlows(search) {
      this.search = search;
    },
    obterClientes(flows){
      const clientes = [];
      const objetosPorCliente = {};

      for (const objeto of flows) {
        const cliente = objeto.cliente;

        if (!(cliente in objetosPorCliente)) {
          objetosPorCliente[cliente] = 0;
        }

        objetosPorCliente[cliente]++;

        if (!clientes.includes(cliente)) {
          clientes.push(cliente);
        }
      }

      const resultado = clientes.map(cliente => {
        return {
          nome: cliente,
          contagem: objetosPorCliente[cliente],
        };
      });

      return resultado;
    }
  },
  async created() {
    this.flows = await this.getJsonData('roge_loggers');

    this.clients = this.obterClientes(this.flows);

  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
</style>
