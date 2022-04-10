import axios from 'axios';

export class HttpService {

  constructor() {
    this.backendPath = process.env.VUE_APP_BACKEND_PATH;

    this.usersPath = "users/";
    this.authPath = "auth/";
    this.tokenPath = "token/";
    this.loginPath = "login/";

    this.statusPath = "statuses/";
    this.ordersPath = "orders/";
    this.reviewsPath = "reviews/"

    this.ingredientsPath = "ingredients/";
    this.pizzaTypesPath = "pizza_types/";
    this.sizesPath = "sizes/";
    this.doughsPath = "doughs/";
    this.menuPizzasPath = "menu_pizzas/";
    this.customPizzasPath = "custom_pizzas/";
    this.halfMeterPizzasPath = "half_meter_pizzas/";
    this.beveragesPath = "beverages/";

    this.menuDict = {
      Ingredient: "ingredients/",
      PizzaType: "pizza_types/",
      Size: "sizes/",
      Dough: "doughs/",
      MenuPizza: "menu_pizzas/",
      CustomPizza: "custom_pizzas/",
      HalfMeterPizza: "half_meter_pizzas/",
      Beverage: "beverages/",
    }

  }

  signUp(signUpFormData, successCallback, errorCallback) {
    let url = this.backendPath + this.authPath + this.usersPath;
    axios
      .post(url, signUpFormData)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
          errorCallback(error);
      });
  }

  logIn(logInFormData, successCallback, errorCallback) {
    let url = this.backendPath + this.authPath + this.tokenPath + this.loginPath;
    axios
      .post(url, logInFormData)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
          errorCallback(error);
      });
  }

  async getMenuEntity(menuEntity) {
    let url = this.backendPath + this.menuDict[menuEntity];
    let entities = []
    try {
      entities = await axios
      .get(url, {})
    } catch (error) {
      console.log(error, menuEntity);
    }
    return entities.data;

  }



}