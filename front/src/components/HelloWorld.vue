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
                <flow-list></flow-list>
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
    msg: String
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
