<template>
    <div>
      <h2>Customize Styles</h2>
      <FormKit type="form" @submit="addNewField">
        <FormKit
          type="color"
          value="#00FF00"
          label="Select Font Color"
          v-model="customization.color"
        />
        <FormKit
          type="select"
          label="Select Font Style"
          :options="fontOptions"
          @input="onFontSelect"
        />
        <FormKit 
          type="select"
          label="Layout"
          :options="layoutOptions"
          v-model="customization.layout"
          />
        <h2>Add Field</h2>
        <FormKit 
          type="text"
          label="New Field Label"
          v-model="newField.label"
        />
      </FormKit>
    </div>
  </template>
  
  <script>
      const loadGoogleFont = (font) => {
  const link = document.createElement('link');
  link.href = `https://fonts.googleapis.com/css?family=${font.replace(' ', '+')}&display=swap`;
  link.rel = 'stylesheet';
  document.head.appendChild(link);
};
    async function fetchGoogleFonts() {
      const isProduction = process.env.NODE_ENV === 'production';
      const baseUrl = isProduction ? '/api/fonts' : 'https://www.googleapis.com/webfonts/v1/webfonts';
      const apiKey = isProduction ? '' : import.meta.env.VITE_GOOGLE_FONTS_KEY;

      const response = await fetch(`${baseUrl}?key=${apiKey}`);
      const data = await response.json();
      return data.items.map(fonts => ({
        label: fonts.family,
        value: fonts.family
      }));
    }
  export default {
    props: {
      customization: {
        type: Object,
        required: true,
      },
      formSchema: {
      type: Array,
      required: true
    }
    },
    data() {
      return {
        // Options for the select dropdowns
        newField: {
        type: 'text',
        label: '',
        step: 'usageDetails',
        validation: ''
        },
        fontOptions: [],
        layoutOptions: ["Single Step", "Multi Step"]
      };
    },
    mounted() {
      fetchGoogleFonts().then(fonts => {
        this.fontOptions = fonts;
      });
    },
    methods: {
      onFontSelect(font) {
        loadGoogleFont(font);
        this.customization.font = font;
      },
      addNewField() {
        this.$emit('addField', this.newField);  // Emit the event to the parent
        this.newField = { type: 'text', label: '', step: 'usageDetails', validation: ''};  // Reset the form
      }
    }
  };
  </script>
  