<template>
  <div>
    <header>
      <nav class="navbar bg-body-tertiary p-3">
        <div class="container-md">
          <a class="navbar-brand" href="#">
            <img src="/floui-logo.svg" alt="Logo" width="200" height="24" class="d-inline-block align-text-top">
            Relação de loggers por fluxo
          </a>
        </div>
      </nav>
    </header>

    <main class="container-fluid mt-5 col-sm-10 offset-sm-1">
      <div class="row">
        <aside class="col-sm-12 col-md-8">
          <h2 class="text-start mb-4">Fluxos</h2>
          <div>
            <FlowList v-for="(flow, index) in flows" :key="index" :flowData="{ ...flow, id: 'collapse' + index }">
            </FlowList>
          </div>
        </aside>
        <section class="col-md-4">
          <div>
            <h2 class="text-start mb-4">Ambientes</h2>
            <article>
              <FiltersEnvironment />
              <ClientList />
            </article>
          </div>

        </section>
      </div>
    </main>

    <body>


    </body>
  </div>
</template>

<script>
import ClientList from './ClientList.vue'
import FlowList from './FlowList.vue'
import FiltersEnvironment from './FiltersEnv.vue'
export default {
  components: { ClientList, FlowList, FiltersEnvironment },
  name: 'HelloWorld',
  props: {
    msg: String,

  },
  data() {
    return {
      flows: [],
      clients: []
    }
  },
  methods: {
    async getJsonData(jsonFile) {
      const response = await fetch(`/database/${jsonFile}.json`);
      const data = await response.json();
      console.log(data);
      return data;
    }
  },
  async created() {
    this.flows = await this.getJsonData('roge_loggers');
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
