<template>
    <div>
        <div class="card mb-3">
            <div class="card-body">
                <input type="checkbox" class="btn-check" id="btn-check-4" autocomplete="off">
                <label class="btn m-1" for="btn-check-4">production</label>

                <input type="checkbox" class="btn-check " id="btn-check-5" checked autocomplete="off">
                <label class="btn  m-1" for="btn-check-5">staging</label>

                <input type="checkbox" class="btn-check " id="btn-check-6" checked autocomplete="off">
                <label class="btn  m-1" for="btn-check-6">homolog</label>
                
                <input type="checkbox" class="btn-check" id="btn-check-7" checked autocomplete="off">
                <label class="btn  m-1" for="btn-check-7">qa</label>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FiltersEnv',
    props: {
        environment: {
            type: Array
        }
    },
    data() {
        return {
            env: this.environment
        }
    }

}
</script>

<style>
input {
    padding: 10px !important;
}
</style>