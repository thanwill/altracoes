<template lang="js">
<div>
    <nav class="navbar bg-body-tertiary mb-5 ">
        <div class="container-fluid">
            
            <form class="d-flex" role="search">
                <input v-model="search" class="form-control" type="search" placeholder="Pesquisar" aria-label="Search" />
                <button class="btn btn-outline-success ms-3 me-3" type="submit">Limpar</button>
                <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#addFlowModal">Adicionar</button>
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
            // verifica se não está vazia
            if (newSearch.length > 0) {
                this.$emit('search', newSearch);
            } else {
                this.$emit('search', '');
            }
        }
    }

}
</script>
