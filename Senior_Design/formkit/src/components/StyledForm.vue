<script setup>
import { ref } from 'vue'

const step = ref('contactInfo')
const stepNames = ['contactInfo', 'usageDetails']

const camel2title = (str) =>
  str
    .replace(/([A-Z])/g, (match) => ` ${match}`)
    .replace(/^./, (match) => match.toUpperCase())
    .trim()
</script>

<template>
  <div>
    <h2>Dynamic Form</h2>
    <div id="singlestep" v-show="customization.layout==='Single Step'">
    <FormKit type="form">
      <template v-for="(field, index) in formSchema" :key="index">
        <FormKit v-bind="field" />
        <label>
          <input type="checkbox" @input="requiredToggle(index, $event)" />
          Required
        </label>
      </template>
    </FormKit>
    </div>
    <div id="multistep" v-show="customization.layout==='Multi Step'">
    <FormKit type="form">
    <ul class="steps">
      <li
        v-for="stepName in stepNames"
        class="step"
        @click="step = stepName"
        :data-step-active="step === stepName"
      >
        {{ camel2title(stepName) }}
      </li>
    </ul>

    <div class="form-body">
      <section v-show="step === 'contactInfo'">
        <FormKit type="group" id="contactInfo" name="contactInfo">
          <template v-for="(field, index) in formSchema" :key="index">
            <FormKit v-if="field['step'] === 'contactInfo'" v-bind="field" />
            <label v-if="field['step'] === 'contactInfo'">
              <input type="checkbox" @input="requiredToggle(index, $event)" />
              Required
            </label>
          </template>
        </FormKit>
      </section>

      <section v-show="step === 'usageDetails'">
        <FormKit id="usageDetails" type="group" name="usageDetails">
          <template v-for="(field, index) in formSchema" :key="index">
            <FormKit v-if="field['step'] === 'usageDetails'" v-bind="field" />
            <label v-if="field['step'] === 'usageDetails'">
          <input type="checkbox" @input="requiredToggle(index, $event)" />
          Required
        </label>
          </template>
        </FormKit>
      </section>
    </div>
  </FormKit>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    customization: {
      type: Object,
      required: true
    },
    formSchema: {
      type: Array,
      required: true
    }
  },
  methods: {
    requiredToggle(index, input) {
        if (input.target.checked === true ){
          this.formSchema[index].validation = "required";
        }
        else {
          this.formSchema[index].validation = "";
        }
      },
  }
};
</script>
<style scoped>
  /* @import 'https://cdn.formk.it/web-assets/multistep-form.css'; */
  .formkit-outer :deep(.formkit-label) {
    color: v-bind('customization.color');
    font-family: v-bind('customization.font');
  }
  
</style>