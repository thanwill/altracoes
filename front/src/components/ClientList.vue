<template>
    <div>
        <ol class="list-group list-group-numbered mb-5">                   
            <div >            
                <li v-for="(cliente, index) in clients" :key="index" class="mb-2 list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">{{cliente.nome}}</div>
                    </div>
                    <span class="badge text-bg-primary rounded-pill">{{cliente.contagem}}</span>
                </li>
            </div>          
        </ol>
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