import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
    themes: {
      light: {
        primary: "#D31837",
        secondary: "#DDB752",
        background: "#ffa759",
        accent: "#76B543",
        error: "#E87600",
      },
    },
  },
});

// #a66c48