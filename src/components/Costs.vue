<template>
    <div v-if="costs" class="col-12">
        <div class="heading-6">{{ $t('costs') }}</div>
        <div v-for="cost in costs" :key="cost.id" class="row g-1">
            <div class="col-auto d-flex align-items-center">
                <img :src="require(`../assets/interface/${cost.id}.png`)" width="12" height="12" />
            </div>
            <div class="col">
                <small class="text-light">{{ $t(cost.id) }}</small>
            </div>
            <div class="col-auto">
                <small v-if="!cost.timer || cost.timer > -2" class="text-light">{{ numeralFormat(cost.count, '0.[0]a') }}</small>
                <small v-if="cost.timer <= -2" class="text-danger">{{ numeralFormat(cost.count, '0.[0]a') }}</small>
            </div>
            <div class="col-auto text-end" style="width:75px">
                <small v-if="(!cost.timer && cost.timer != 0) || cost.timer < 0" class="text-normal">---</small>
                <small v-if="cost.timer == 0" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                <small v-if="cost.timer > 0" class="text-timer">{{ numeralFormat(cost.timer, '00:00:00') }}</small>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'costs' ],
}
</script>
