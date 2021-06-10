<template>
    <div class="col-6 col-md-2">
        <button class="btn w-100 text-start" @click="convert(id)">
            <div class="row g-1 align-items-center justify-content-center">
                <div class="col-auto d-flex align-items-center"><img :src="require(`../assets/interface/${data[id].source}.png`)" width="12" height="12" /></div>
                <div class="col-auto"><small class="text-normal ms-1">{{ numeralFormat(sourceCount, '0.[0]a') }}</small></div>
            </div>
            <div class="small text-center ps-2" style="line-height:1;">
                <i class="small text-normal fas fa-fw fa-caret-down"></i>
            </div>
            <div class="row g-1 align-items-center justify-content-center">
                <div class="col-auto d-flex align-items-center"><img :src="require(`../assets/interface/${data[id].resource}.png`)" width="14" height="14" /></div>
                <div class="col-auto"><span class="text-light ms-1">{{ numeralFormat(destinationCount, '0.[0]a') }}</span></div>
            </div>
        </button>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    props: [ 'id' ],
    computed: {
        ...mapState([
            'data',
        ]),
        sourceCount: function() {
            return Math.floor(this.data[this.data[this.id].source].count / this.data[this.id].rate) * this.data[this.id].rate
        },
        destinationCount: function() {
            return Math.floor(this.data[this.data[this.id].source].count / this.data[this.id].rate)
        },
    },
    methods: {
        ...mapActions([
            'convert',
        ]),
    },
}
</script>
