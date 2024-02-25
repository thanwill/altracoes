<template>
  <div class="home">
    <FlowPage />
  </div>
</template>

<script>
// @ is an alias to /src
import FlowPage from '@/components/FlowsPage.vue'

export default {
  name: 'HomeView',
  components: {
    FlowPage
  }
}
</script>
