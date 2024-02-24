<template lang="js">
    <div>
        <nav class="navbar bg-body-tertiary mb-5">
            <div class="container-fluid">                
                <form class="d-flex" role="search">
                    <input v-model="search" class="form-control me-5 col-sm-8" type="search" placeholder="Procurar por fluxos" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Pesquisar</button>
                </form>
            </div>
        </nav>
    </div>
</template>
<script>
export default {
    name: 'FlowSearch',
    data() {
        return {
            search: ''
        }
    }, 
    watch: {
        search: function (newSearch) {
            this.$emit('search', newSearch)
        }
    }
    
}
</script>
<style lang="css">
    
</style>