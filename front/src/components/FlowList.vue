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
                            <div v-if="flow.loggers.length > 0">
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
                                        <td class="text-start">{{ logger.label ? logger.label : 'Sem rótulo' }}</td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                            <div v-else>
                                <p class="mt-3">Nenhum logger encontrado</p>
                            </div>
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
    props: ['flowData', 'filters', 'searchName'],
    computed: {
        filteredFlow() {
            let result = this.flowData;
            if (this.filters.length > 0) {
                result = result.filter(flow => this.filters.includes(flow.ambiente));
            }
            if (this.searchName) {
                result = result.filter(flow => flow.arquivo.includes(this.searchName));
            }
            return result;
        }
    }

}
</script>

<style>
span {
    margin-right: 25px;
}
</style>