<template>
    <div>
        <div class="card mb-3">
            <div class="card-body">

                <span v-for="(environment, index) in environments" :key="index">
                    <input type="checkbox" class="btn-check" :id="`btn-check-${index}`" autocomplete="off">
                    <label class="btn m-1" :for="`btn-check-${index}`">{{ environment }}</label>
                </span>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FiltersEnv',
    props: {
        environments: {
            type: Array,
            default: () => ['production', 'staging']
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