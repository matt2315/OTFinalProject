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
      message1: "try"
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
        .then(response => {this.message1 = response.data;})
      },

      addTuyongLumpiaToCart: function()
      {
        axios.post('http://localhost:5000/purchaseTix2',
      {
        movieTitle: "Tuyong Lumpia",
        TuyongLumpiaQuantity: this.TuyongLumpiaQuantity
      })
      .then(response => {this.message1 = response.data;})
      },

      addGinataangManiToCart: function()
      {
        axios.post('http://localhost:5000/purchaseTix3',
      {
        movieTitle: "Ginataang Mani",
        GinataangManiQuantity: this.GinataangManiQuantity
      })
      .then(response => {this.message1 = response.data;})
      }

      }
    }
)

var showCart = new Vue
(
  {
    el:"#showingCart",
    data:
    {
      ticket_template:
      {
        ticket_id: '',
        movie_title: '',
        ticket_quantity: '',
        ticket_price: '',
        ticket_date_purchased: ''
      },
      t_id: localStorage.getItem('tid'),
      t_mTitle: localStorage.getItem('mTitle'),
      t_tQuantity: localStorage.getItem('tQuantity'),
      t_tPrice: localStorage.getItem('tPrice'),
      t_tDatePurchased: localStorage.getItem('tDatePurchased')
    },
    methods:
    {
      refresh: function()
      {
        console.log('anytext')
        axios.get('http://localhost:5000/cart')
        .then(response => {this.ticket_template = response.data;})
      }

    }
  }
)
