<template>
  <div>
    <div class="card mb-3">
      <div class="card-body">
        <span v-for="(ambiente, index) in ambientes" :key="index">
          <input v-model="filters" :value="ambiente"  type="checkbox" class="btn-check" :id="`btn-check-${index}`" autocomplete="off" />
          <label class="btn m-1" :for="`btn-check-${index}`">
            {{ ambiente }}
          </label>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FlowFilters",
  props: {
    ambientes: {
      type: Array,
      default: () => ["production", "staging"],
    },
  },
  data() {
    return {
      filters:[],
    };
  },
  watch: {
    filters: function (novoFiltro) {
      this.$emit("filter", novoFiltro); 
    },
  }
};
</script>

<style>
input {
  padding: 10px !important;
}
</style>
