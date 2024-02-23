<template>
    <div>
        <div class="accordion" id="accordionExample">
            <div class="accordion-item mb-3">
                <h2 class="accordion-header">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target=" '#' + id "
                        aria-expanded="true" :aria-controls="id">
                        {{ arquivo }}
                    </button>
                </h2>
                <div :id="id" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nemo temporibus magni illo, odio debitis nulla pariatur quis culpa optio dicta saepe harum ea voluptatem. Nemo perferendis ipsam reiciendis optio?
                    </div>
                </div>
            </div>            
        </div>
    </div>
</template>

<script>
export default {
    name: 'FlowList',
    props: {
        msg: String,
        arquivo: String,
        loggers: Array,
        id: String
    }

}
</script>

<style></style>