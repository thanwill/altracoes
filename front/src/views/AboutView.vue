<template>
  <div class="about">

    <div v-if="token">
      <button @click="logout" class="btn btn-primary">Sair</button>
      <h1>This is an about page</h1>
    </div>

    <div v-else>
      <form class="col-sm-10 offset-sm-1 col-md-4 offset-md-4 ">
        <h1 class="mb-5">Lorem, ipsum.</h1>
        <div class="mb-3">
          <label for="exampleInputEmail1 text-start" class="form-label">Endereço de e-mail</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">Nós nunca compartilharemos suas informações.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1 text-start" class="form-label">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input me-3" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Manter-me conectado</label>
        </div>
        <button type="submit" class="btn btn-primary mt-3">Enviar</button>
      </form>
    </div>

  </div>
</template>
<script>
export default {
  name: 'AboutView',
  props: {
    token: {
      type: String,
      required: true,
      default: ''
    } 

  }

}
</script>

<style scoped>

</style>