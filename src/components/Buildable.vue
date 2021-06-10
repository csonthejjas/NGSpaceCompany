<template>
    <div class="col">
        <div class="row gx-2">
            <div class="col-auto">
                <div class="timeline-marker">
                
                    <i v-if="!data[id].unlocked" class="fas fa-fw fa-lock text-muted"></i>
                    <i v-if="(data[id].unlocked && data[id].max && data[id].count < data[id].max) || (data[id].unlocked && !data[id].max)" class="fas fa-fw fa-lock-open"></i>
                    <i v-if="data[id].unlocked && data[id].max && data[id].count >= data[id].max" class="fas fa-fw fa-check text-success"></i>
                    
                </div>
            </div>
            <div class="col">
            
                <div v-if="!data[id].unlocked" class="card card-body">
                    <span class="text-muted">{{ $t('locked') }}</span>
                </div>
                
                <div v-if="data[id].unlocked && data[id].max && data[id].count >= data[id].max" class="card card-body">
                    <span class="h6 text-light mb-0">{{ $t(data[id].id) }}</span>
                </div>
                
                <div v-if="(data[id].unlocked && data[id].max && data[id].count < data[id].max) || (data[id].unlocked && !data[id].max)" class="card card-body">
                    <div class="row g-3">
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div class="col-12">
                                    <div class="row g-1">
                                        <div class="col">
                                            <span class="h6 text-light">{{ $t(data[id].id) }}</span>
                                        </div>
                                        <div v-if="!data[id].max || data[id].max > 1" class="col-auto">
                                            <small class="text-normal me-1">x</small>
                                            <span :class="{ 'text-light':data[id].count > 0, 'text-normal':data[id].count <= 0 }">{{ numeralFormat(data[id].count, '0.[0]a') }}</span>
                                            <small v-if="data[id].max && data[id].max > 1" class="ms-1 text-normal">/{{ data[id].max }}</small>
                                        </div>
                                        <div class="col-12 small">
                                            <span class="text-normal">{{ $t(data[id].id + '_desc') }}</span>
                                        </div>
                                    </div>
                                </div>
                            
                                <div v-if="id == 'nanoswarm'" class="col-12">
                                    <div class="small">{{ $t('selectResource') }}</div>
                                    <select class="form-control" v-model="selected" @change="switchNano(selected)">
                                        <option value="energy">{{ $t('energy') }}</option>
                                        <option value="plasma">{{ $t('plasma') }}</option>
                                        <option value="meteorite">{{ $t('meteorite') }}</option>
                                        <option value="carbon">{{ $t('carbon') }}</option>
                                        <option value="oil">{{ $t('oil') }}</option>
                                        <option value="metal">{{ $t('metal') }}</option>
                                        <option value="gem">{{ $t('gem') }}</option>
                                        <option value="wood">{{ $t('wood') }}</option>
                                        <option value="silicon">{{ $t('silicon') }}</option>
                                        <option value="uranium">{{ $t('uranium') }}</option>
                                        <option value="lava">{{ $t('lava') }}</option>
                                        <option value="lunarite">{{ $t('lunarite') }}</option>
                                        <option value="methane">{{ $t('methane') }}</option>
                                        <option value="titanium">{{ $t('titanium') }}</option>
                                        <option value="gold">{{ $t('gold') }}</option>
                                        <option value="silver">{{ $t('silver') }}</option>
                                        <option value="hydrogen">{{ $t('hydrogen') }}</option>
                                        <option value="helium">{{ $t('helium') }}</option>
                                        <option value="ice">{{ $t('ice') }}</option>
                                        <option value="science">{{ $t('science') }}</option>
                                        <option value="fuel">{{ $t('fuel') }}</option>
                                        <option value="antimatter">{{ $t('antimatter') }}</option>
                                    </select>
                                </div>
                                
                            </div>
                        </div>
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div v-if="data[id].stats" class="col-12">
                                    <div class="heading-6">{{ $t('stats') }}</div>
                                    <div class="row g-1">
                                        <div class="col-4">
                                            <span class="small text-normal">{{ $t('power') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(data[id].stats.power, '0.[0]a') }}</span>
                                        </div>
                                        <div class="col-4">
                                            <span class="small text-normal">{{ $t('defense') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(data[id].stats.defense, '0.[0]a') }}</span>
                                        </div>
                                        <div class="col-4">
                                            <span class="small text-normal">{{ $t('speed') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(data[id].stats.speed, '0.[0]a') }}</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div v-if="data[id].storage && data[id].storage.count > 0" class="col-12">
                                    <div class="heading-6">{{ $t('storage') }}</div>
                                    <div class="row g-1">
                                        <div class="col-auto d-flex align-items-center">
                                            <img :src="require(`../assets/interface/${data[id].storage.id}.png`)" width="12" height="12" />
                                        </div>
                                        <div class="col">
                                            <small class="text-light">{{ $t(data[id].storage.id) }}</small>
                                        </div>
                                        <div class="col-auto">
                                            <small class="text-success">+{{ numeralFormat(data[id].storage.count, '0.[0]a') }}</small>
                                        </div>
                                    </div>
                                </div>
                                
                                <div v-if="data[id].outputs" class="col-12">
                                    <div class="heading-6">{{ $t('production') }}</div>
                                    <div v-for="output in data[id].outputs" :key="output.id" class="row g-1">
                                        <div class="col-auto d-flex align-items-center">
                                            <img :src="require(`../assets/interface/${output.id}.png`)" width="12" height="12" />
                                        </div>
                                        <div class="col">
                                            <small class="text-light">{{ $t(output.id) }}</small>
                                        </div>
                                        <div class="col-auto">
                                            <small class="text-success">+{{ numeralFormat(output.count * data[output.id].boost, '0.[0]a') }}</small>
                                            <small class="text-normal ms-1">/s</small>
                                        </div>
                                    </div>
                                    <div v-for="input in data[id].inputs" :key="input.id" class="row g-1">
                                        <div class="col-auto d-flex align-items-center">
                                            <img :src="require(`../assets/interface/${input.id}.png`)" width="12" height="12" />
                                        </div>
                                        <div class="col">
                                            <small class="text-light">{{ $t(input.id) }}</small>
                                        </div>
                                        <div class="col-auto">
                                            <small v-if="input.id == 'energy'" class="text-warning">-{{ numeralFormat(input.count, '0.[0]a') }}</small>
                                            <small v-if="input.id != 'energy'" class="text-warning">-{{ numeralFormat(input.count, '0.[0]a') }}</small>
                                            <small class="text-normal ms-1">/s</small>
                                        </div>
                                    </div>
                                </div>

                                <costs :costs="data[id].costs" />
                                
                                <div class="col-12">
                                    <div class="row gx-1 gy-3">
                                        <div v-if="data['techDestruction'].count > 0 && data[id].destroyable" class="col-auto">
                                            <button class="btn" @click="destroy(id, 1)">
                                                <span class="text-danger">{{ $t('destroy') }}</span>
                                            </button>
                                        </div>
                                        <div class="ms-auto col-auto">
                                            <button class="btn" @click="build(id, 1)">
                                                {{ $t(btnText) }}
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
    props: [ 'id', 'btnText' ],
    components: {
        'costs': Costs,
    },
    computed: mapState([
        'data',
    ]),
    methods: {
        ...mapActions([
            'build', 'destroy', 'switchNano',
        ]),
    },
}
</script>
