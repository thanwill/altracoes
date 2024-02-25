<template lang="">
    <div>
        <header>
            <nav class="navbar bg-body-tertiary mb-5 ">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                <img src="/floui-logo.svg" alt="Logo" width="200" height="24" class="d-inline-block align-text-top">
                </a>
                <div class="col"></div>
                <span>{{ msg }}</span>
                <div class="col">
                <nav>
                    <router-link to="/">Home</router-link> |
                    <router-link to="/about">About</router-link>
                </nav>
                </div>
            </div>
            </nav>
        </header>
    </div>
</template>
<script>
export default {
    name: 'HeaderPage',
    props: {
        msg: String
    }

}
</script>
<style lang="css">
    span {
        font-size: 1.5rem;
        font-weight: bold;
    }
</style>