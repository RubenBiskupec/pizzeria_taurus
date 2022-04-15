<script>

import { HttpService } from "@/services/HttpService";

export default {
  name: "SignUp",
  data() {
    return {
      signUpNotification: '',
      signUpErrors: [],
      signUpFistName: null,
      signUpLastName: null,
      signUpPassword: null,
      signUpConfirmationPassword: null,
      signUpEmail: null,
      signUpCellphoneNumber: null,
      signUpAddress: null,

      httpService: new HttpService(),
    }
  },
  methods: {
    signUp: function () {
      this.signUpErrors = [];
      this.signUpNotification = '';
      let isFormValid = this.validateForm();

      if (isFormValid) {

        const signUpFormData = {
          email: this.signUpEmail,
          password: this.signUpPassword,
          first_name: this.signUpFistName,
          last_name: this.signUpLastName,
          address: this.signUpAddress,
          cellphone_number: this.signUpCellphoneNumber
        }

        this.httpService.signUp(signUpFormData, this.signUpSuccessCallback, this.signUpErrorCallback);
      }
    },
    validateForm: function() {
      if (this.signUpEmail === "" || this.signUpEmail == null) {
        this.signUpErrors.push("Inserire l'Email");
      }
      if (this.signUpPassword == null || this.signUpPassword.length < 8) {
        this.signUpErrors.push("La password deve essere almeno 8 caretteri");
      }
      if (this.signUpPassword != this.signUpConfirmationPassword) {
        this.signUpErrors.push("Le password non coincidono");
      }
      if (this.signUpFistName === "" || this.signUpFistName == null) {
        this.signUpErrors.push("Inserire il Nome");
      }
      if (this.signUpLastName === "" || this.signUpLastName == null) {
        this.signUpErrors.push("Inserire il Cognome");
      }
      if (this.signUpEmail === "" || this.signUpEmail == null) {
        this.signUpErrors.push("Inserire l'Email");
      }
      if (this.signUpCellphoneNumber === "" || this.signUpCellphoneNumber == null) {
        this.signUpErrors.push("Inserire il Numero di telefono");
      }
      if (this.signUpAddress === "" || this.signUpAddress == null) {
        this.signUpErrors.push("Inserire l'Indirizzo");
      }
      return !this.signUpErrors.length;
    },
    signUpSuccessCallback: function (data) {
      this.signUpNotification = "Account creato con successo. Accedi!";
    },
    signUpErrorCallback: function (error) {
      // TODO gestici i diversi tipi di errore
      this.signUpErrors.push("Qualcosa e' andato storto. Per favore riprova.");
      console.log(JSON.stringify(error));
    },
    setTab(tab) {
      this.$emit("setTab", tab);
    }
  }
}
</script>

<template>
  <v-card-text>
    <v-container>

      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Nome"
            v-model="signUpFistName"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Cognome"
            v-model="signUpLastName"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Email"
            v-model="signUpEmail"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Password"
            v-model="signUpPassword"
            required
            type="password"
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Conferma Password"
            v-model="signUpConfirmationPassword"
            required
            type="password"
            outlined
            dense
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Numero di telefono"
            v-model="signUpCellphoneNumber"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            label="Indirizzo"
            v-model="signUpAddress"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="secondary"
        v-on:click="signUp"
      >
        Registrati
      </v-btn>
    </v-card-actions>
    <v-divider class="my-4"></v-divider>

    <v-row
      v-if="signUpNotification != ''"
      class="px-4 py-2 v-row-sign-up"
    >
      <v-col cols="12"
        class="px-4 py-2 my-2 rounded accent"
      >
        {{ signUpNotification }}
      </v-col>
    </v-row>
     <v-divider
      v-if="signUpNotification != ''"
      class="my-4"
    ></v-divider>

    <v-row
      v-if="signUpErrors.length"
      class="px-4 py-2 v-row-sign-up"
    >
      <v-col
        cols="12"
        v-for="error in signUpErrors"
        v-bind:key="error"
        class="px-4 py-2 my-2 rounded primary"
      >
        {{ error }}
      </v-col>
    </v-row>
    <v-divider
      v-if="signUpErrors.length"
      class="my-4"
    ></v-divider>

    <v-container>
      <v-row>
        <v-col cols="7">
          Hai gia' un account?
        </v-col>
        <v-spacer></v-spacer>
        <v-col
          cols="5"
          align="right"
        >
          <v-btn
            small
            v-on:click="setTab(0)"
          >Accedi</v-btn>
        </v-col>
      </v-row>
    </v-container>

  </v-card-text>
</template>

<style scoped>

.v-row-sign-up {
  color: white;
  padding: 12px !important;
}

</style>