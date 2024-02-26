<template lang="scoped">
    <div>
        
        <div class="mb-4 col-md-8 text-center offset-2">
            <label for="formFileMultiple" class="form-label">Adicionar fluxos</label>
            <input class="form-control mb-4" type="file" id="formFileMultiple" multiple>
            <button class="btn btn-primary" > Adicionar </button>
        </div>        
    </div>
</template>
<script>
export default {
    name: 'FlowAdd',
    data() {
        return {
            files: []
        }
    }, 
    methods: {
        addFlows() {
            console.log('Adicionando fluxos');
        }
    }, // emite um evento para o componente pai para atribuir o showAddFlow para false
    closeAddFlow() {
        this.$emit('addFlow', false);
    }
    
}
</script>
<style lang="css">
    
</style>