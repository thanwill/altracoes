<template>
    <div>
        <div class="accordion" id="accordionExample">
            <div class="accordion-item mb-3">
                <h2 class="accordion-header">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#' + id"
                        aria-expanded="true" :aria-controls="id">
                        <span class="badge rounded-pill"
                            :class="{ 'text-bg-danger': ambiente !== 'staging', 'text-bg-success': ambiente === 'staging' }">{{
                                ambiente }}</span>
                        {{ arquivo }}
                    </button>
                </h2>
                <div :id="id" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">uid</th>
                                    <th scope="col">label</th>
                                </tr>
                            </thead>
                            <tbody v-for="(logger, index) in loggers" :key="index">
                                <tr>
                                    <th scope="row">{{ index + 1 }}</th>
                                    <td>{{ logger.uid }}</td>
                                    <td class="text-start">{{ logger.label }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FlowList',
    props: ['flowData'],
    data() {
        return {
            id: this.flowData.id,
            arquivo: this.flowData.arquivo,
            ambiente: this.flowData.ambiente,
            loggers: this.flowData.loggers
        }
    },
    created() {
        console.log(this.flowData);
    }


}
</script>

<style>
span {
    margin-right: 25px;
}
</style>