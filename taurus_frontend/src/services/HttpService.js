import axios from 'axios';

export class HttpService {

  constructor() {
    this.backendPath = process.env.VUE_APP_BACKEND_PATH;

    this.authPath = "auth/";
    this.usersPath = "users/";
    this.mePath = "me/";
    this.tokenPath = "token/";
    this.loginPath = "login/";
    this.logoutPath = "logout/";

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
    this.todayPath = "today/";
    this.completePath = "/complete/"

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

  logOut(successCallback, errorCallback) {
    let url = this.backendPath + this.authPath + this.tokenPath + this.logoutPath;
    axios
      .post(url)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
          errorCallback(error);
      });
  }

  async getUserInfo() {
    let url = this.backendPath + this.usersPath + this.mePath;
    let userInfo = {};
    try {
      userInfo = await axios
      .get(url);
    } catch (error) {
      console.log(error)
    }
    return userInfo.data;
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

  createCustomPizza(customPizza, customPizzaLong, successCallback, errorCallback) {
    let url = this.backendPath + this.customPizzasPath;
    debugger
    axios
      .post(url, customPizza)
      .then(response => {
        successCallback(response.data, customPizzaLong);
      })
      .catch(error => {
        errorCallback(error);
      });
  }

  createOrder(order, successCallback, errorCallback) {
    let url = this.backendPath + this.ordersPath;
    axios
      .post(url, order)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
        errorCallback(error);
      });
  }

  async getOrderUserList() {
    let url = this.backendPath + this.ordersPath + this.mePath;
    let orderList = [];
    try {
      orderList = await axios
      .get(url, {})
    } catch (error) {
      console.log(error);
    }
    return orderList.data;
  }

  async getTodayOrders() {
    let url = this.backendPath + this.ordersPath + this.todayPath;
    let orderList = [];
    try {
      orderList = await axios
      .get(url, {})
    } catch (error) {
      console.log(error);
    }
    return orderList.data;
  }

  async getOrdersByDate(start_date, end_date) {
    // es. http://localhost:8000/api/v1/orders/?delivery_date%3C=2022-04-15&delivery_date%3E=2022-04-10
    let url = this.backendPath + this.ordersPath + "?delivery_date>=" + start_date + "&delivery_date<=" + end_date;
    let orderList = [];
    try {
      orderList = await axios
      .get(url, {})
    } catch (error) {
      console.log(error);
    }
    return orderList.data;
  }

  completeOrder(order, successCallback) {
    let url = this.backendPath + this.ordersPath + order.id + this.completePath;
    axios
      .post(url, order)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
        return error;
      });
  }

  submitReview(reviewForm, successCallback, errorCallback) {
    let url = this.backendPath + this.reviewsPath;
    axios
      .post(url, reviewForm)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
        errorCallback(error);
      });
  }

  updateReview(reviewForm, successCallback, errorCallback) {
    let url = this.backendPath + this.reviewsPath + reviewForm.id;
    axios
      .put(url, reviewForm)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
        errorCallback(error);
      });
  }

  deleteReview(id, successCallback, errorCallback) {
    let url = this.backendPath + this.reviewsPath + id;
    axios
      .delete(url, id)
      .then(response => {
        successCallback(response.data);
      })
      .catch(error => {
        errorCallback(error);
      });
  }

  async getReviews() {
    let url = this.backendPath + this.reviewsPath;
    let reviews = [];
    try {
      reviews = await axios
      .get(url, {})
    } catch (error) {
      console.log(error);
    }
    return reviews.data;
  }

  async getReview(orderId) {
    let url = this.backendPath + this.reviewsPath + this.ordersPath + orderId;
    let review = {};
    try {
      review = await axios
      .get(url, {})
    } catch (error) {
      console.log(error);
    }
    return review.data;
  }





}