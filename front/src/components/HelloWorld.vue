<template>
  <div>
    <header class="">
      <h1>Relação de loggers por fluxo</h1>
    </header>

    <main class="container mt-5 col-sm-10 col-md-10 col-lg-8">
      <div class="row">
        <aside class="col-sm-12 col-md-8">
          <h2>Fluxos</h2>
          <div class="mt-3">
            <FlowList v-for="(flow, index) in flows" :key="index" :id="'collapse' + index" :arquivo="flow.arquivo"
              :loggers="flow.loggers">
            </FlowList>
          </div>
        </aside>
        <section class="col-md-4">
          <h3>Ambientes</h3>
          <article class="mt-3">
            <client-list></client-list>
          </article>
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
export default {
  components: { ClientList, FlowList },
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
