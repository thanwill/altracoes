<template>
    <div>
        
        <div v-if="flowData">
            <div class="accordion" id="accordionFlows">
                <div class="accordion-item mb-3" v-for="(flow, index) in filteredFlow" :key="index">

                    <h2 class="accordion-header">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse"
                            :data-bs-target="'#' + index" aria-expanded="false" :aria-controls="index">
                            <span class="badge rounded-pill"
                                :class="{ 'text-bg-danger': flow.ambiente !== 'staging', 'text-bg-success': flow.ambiente === 'staging' }">
                                {{ flow.ambiente }}
                            </span>
                            {{ flow.arquivo }}
                        </button>
                    </h2>
                    <div :id="index" class="accordion-collapse collapse" data-bs-parent="#accordionFlows">
                        <div class="accordion-body">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">#</th>
                                        <th scope="col">uid</th>
                                        <th scope="col">label</th>
                                    </tr>
                                </thead>
                                <tbody v-for="(logger, index) in flow.loggers" :key="index">
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
    </div>
</template>

<script>
export default {
    name: 'FlowList',
    props: ['flowData', 'filters'],
    computed: {
        filteredFlow() {
            if (this.filters.length === 0) {
                return this.flowData
            }
            return this.flowData.filter(flow => this.filters.includes(flow.ambiente))
        }
    },
    data() {

        return {
            id: this.flowData.id,
            ambiente: this.flowData.ambiente,
            arquivo: this.flowData.arquivo,
            loggers: this.flowData.loggers
        }
    },

}
</script>

<style>
span {
    margin-right: 25px;
}
</style>