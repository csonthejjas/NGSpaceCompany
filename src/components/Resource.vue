<template>
    <div class="col">
        <div class="row gx-2">
            <div class="col-auto">
                <div class="timeline-marker">
                    <i class="fas fa-fw fa-lock-open"></i>
                </div>
            </div>
            <div class="col">
                <div class="card card-body">
                    <div class="row g-3">
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div class="col-12">
                                    <div class="row g-1">
                                        <div class="col">
                                            <span class="h6 text-light">{{ $t('overview') }}</span>
                                        </div>
                                        <div class="col-auto">
                                            <span :class="{ 'text-light':(data[id].count > 0 && (!data[id].storage || data[id].count < data[id].storage)), 'text-normal':data[id].count <= 0, 'text-success':data[id].storage && data[id].count >= data[id].storage }">{{ numeralFormat(data[id].count, '0.[0]a') }}</span>
                                            <small v-if="data[id].storage" class="text-normal ms-1">/{{ numeralFormat(data[id].storage, '0.[0]a') }}</small>
                                        </div>
                                        <div v-if="data[id].storage" class="col-12">
                                            <div class="row g-1">
                                                <div class="col small">
                                                    <span>{{ $t('remainingTimeFullStorage') }}</span>
                                                </div>
                                                <div class="col-auto text-end" style="width:75px">
                                                    <small v-if="data[id].storageTimer < 0" class="text-normal">---</small>
                                                    <small v-if="data[id].storageTimer == 0" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                                                    <small v-if="data[id].storageTimer > 0 && data[id].storageTimer <= (3600 * 24 * 2)" class="text-timer">{{ numeralFormat(data[id].storageTimer, '00:00:00') }}</small>
                                                    <small v-if="data[id].storageTimer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div v-if="data[id].toggle" class="col-12 text-end">
                                    <button class="btn" @click="toggle(id)">
                                        {{ $t('toggle' + data[id].toggle) }}
                                    </button>
                                </div>
                                
                            </div>
                        </div>
                        <div v-if="data[id].gain" class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <costs :costs="data[id].costs" />
                                
                                <div class="col-12">
                                    <div class="row g-1">
                                        <div class="ms-auto col-auto">
                                            <button class="btn" @click="gain(id)">
                                                {{ $t('gain') }} {{ data[id].gain }}
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Costs from './Costs.vue'

import { mapState, mapActions } from 'vuex'

export default {
    props: [ 'id' ],
    components: {
        'costs': Costs,
    },
    computed: mapState([
        'data',
    ]),
    methods: {
        ...mapActions([
            'toggle', 'gain',
        ]),
    },
}
</script>
