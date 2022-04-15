<script>
import axios from "axios";
import { HttpService } from "@/services/HttpService";


export default {
  name: "LogIn",
  data() {
    return {
      logInNotification: '',
      logInErrors: [],
      logInEmail: null,
      logInPassword: null,

      httpService: new HttpService(),
    }
  },
  methods: {
    logIn: function () {
      this.logInErrors = [];
      let isLogInValid = this.validateLogIn();
      if (isLogInValid) {

        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");

        const logInFormData = {
          email: this.logInEmail,
          password: this.logInPassword
        }

        this.httpService.logIn(logInFormData, this.logInSuccessCallback, this.logInErrorCallback);
      }
    },
    validateLogIn: function () {
      if (this.logInEmail === "" || this.logInEmail == null) {
        this.logInErrors.push("Inserire l'Email");
      }
      if (this.logInPassword == null || this.logInPassword.length < 8) {
        this.logInErrors.push("La password deve essere almeno 8 caretteri");
      }
      return !this.logInErrors.length;
    },
    logInSuccessCallback: function (responseData) {
      const token = responseData.auth_token;
      this.$store.dispatch("setToken", token);
      this.logInNotification = "Accesso eseguito correttamente!";
      this.$router.push("account");
    },
    logInErrorCallback: function (error) {
      this.logInErrors.push("Qualcosa e' andato storto. Per favore riprova.");
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
        >
          <v-text-field
            label="Email"
            v-model="logInEmail"
            required
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
        >
          <v-text-field
            label="Password"
            type="password"
            v-model="logInPassword"
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
        v-on:click="logIn"
      >
        Accedi
      </v-btn>
    </v-card-actions>
    <v-divider class="my-4"></v-divider>

    <v-row
      v-if="logInNotification != ''"
      class="px-4 py-2 v-row-sign-up"
    >
      <v-col cols="12"
        class="px-4 py-2 my-2 rounded accent"
      >
        {{ logInNotification }}
      </v-col>
    </v-row>
     <v-divider
      v-if="logInNotification != ''"
      class="my-4"
    ></v-divider>

    <v-container>
      <v-row>
        <v-col cols="7">
          Non hai un account?
        </v-col>
        <v-spacer></v-spacer>
        <v-col
          cols="5"
          align="right"
        >
          <v-btn
            small
            v-on:click="setTab(1)"
          >Registrati</v-btn>
        </v-col>
      </v-row>
  <!--              <v-row>-->
  <!--                <v-col>-->
  <!--                  Password dimenticata?-->
  <!--                </v-col>-->
  <!--                <v-spacer></v-spacer>-->
  <!--                <v-col-->
  <!--                  cols="5"-->
  <!--                  align="right"-->
  <!--                >-->
  <!--                  <v-btn-->
  <!--                    small-->
  <!--                  >Recupera credenziali</v-btn>-->
  <!--                </v-col>-->
  <!--              </v-row>-->
    </v-container>
  </v-card-text>
</template>

<style scoped>

</style>