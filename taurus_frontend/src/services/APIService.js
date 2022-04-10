import axios from "axios";

export default {
  getMenuEntity(menuEntity, callback) {
    let url = this.backendPath + this.menuDict[menuEntity];
      axios
        .get(url, {
          headers: {
            "Access-Control-Allow-Origin": "*"
          }
        })
        .then(response => {
          callback(response.data);
        })
        .catch(error => {
          console.log("Error occured ", error)
        })
  }
}
