<template>
    <div>
        <ol class="list-group list-group-numbered mb-5">                   
            <div v-for="(cliente, index) in clients" :key="index">
                
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">{{cliente.nome}}</div>
                    </div>
                    <span class="badge text-bg-primary rounded-pill">{{cliente.contagem}}</span>
                </li>
            </div>
        </ol>
        <div class="mb-4">
            <label for="formFileMultiple" class="form-label">Adicionar fluxos</label>
            <input class="form-control" type="file" id="formFileMultiple" multiple>
        </div>
        <button type="button" class="btn btn-outline-secondary mb-5">Salvar</button>

    </div>
</template>

<script>
export default {
    name: 'ClientList',
    props: ['clients']
}
</script>

<style>
button {
    width: 100%;
}
</style>