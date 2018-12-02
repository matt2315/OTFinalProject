var logIn = new Vue
(
  {
    el: "#loginVue",
    data:
    {
      username: null,
      password: null,
      message: 'hehe'
    },
    methods:
    {
        logIn: function ()
        {
          axios.get('http://localhost:5000/logIn',
          {
              params:
              {
                username: this.username,
                password: this.password
              }
          })
          .then(response => {this.message = response.data})
      },
      signUp: function()
      {
        if (this.username && this.password)
        {
          axios.post('http://localhost:5000/signUp',
          {
              username: this.username,
              password: this.password
          })
          .then(response => {this.message = response.data})
        }
      }
    }
  }
)

var purchaseTix = new Vue
(
  {
    el: "#purchaseVue",
    data:
    {
      movieTitle: null,
      silipQuantity: null,
      TuyongLumpiaQuantity: null,
      GinataangManiQuantity:null,
      message: "try"
    },
    methods:
    {
      addSilipToCart: function()
      {
        axios.post('http://localhost:5000/purchaseTix',
      {
        movieTitle: "Silip",
        silipQuantity: this.silipQuantity,
      })
        .then(response => {this.message = response.data})
      }
    }
  }
)
