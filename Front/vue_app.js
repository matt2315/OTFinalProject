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
      message1: "try",
      ticket_template: null,
      t_id: localStorage.getItem('tid'),
      t_mTitle: localStorage.getItem('mTitle'),
      t_tQuantity: localStorage.getItem('tQuantity'),
      t_tPrice: localStorage.getItem('tPrice'),
      t_tDatePurchased: localStorage.getItem('tDatePurchased'),
      showcart: false,
      showcart2: false,
      testMessage: null,
      u_qty:null,
      u_title: null,
      o_id: null,
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
        setTimeout(location.reload.bind(location), 250);
      },

      addTuyongLumpiaToCart: function()
      {
        axios.post('http://localhost:5000/purchaseTix2',
      {
        movieTitle: "Tuyong Lumpia",
        TuyongLumpiaQuantity: this.TuyongLumpiaQuantity
      })
      .then(response => {this.message1 = response.data;})
        setTimeout(location.reload.bind(location), 250);
      },

      addGinataangManiToCart: function()
      {
        axios.post('http://localhost:5000/purchaseTix3',
      {
        movieTitle: "Ginataang Mani",
        GinataangManiQuantity: this.GinataangManiQuantity
      })
      .then(response => {this.message1 = response.data;})
        setTimeout(location.reload.bind(location), 250);
      },
      refresh: function()
      {
      axios.get('http://localhost:5000/cart')
      .then(response => {this.ticket_template = response.data;});
      },
      viewcart: function()
      {
        this.showcart = true
      },
      update: function(key)
      {
        this.showcart = true
        axios.get('http://localhost:5000/update_qty',
        {params: {
          id: key
        }})
        .then(response =>
          {
          this.u_qty = response['data']['qty'];
          this.u_title = response['data']['title'];
          })
      },
      cancelupdate: function()
      {
        this.showcart = false;
        this.showcart2 = false;
      },
      updateTicket: function()
      {
        axios.get('http://localhost:5000/update_Ticket',
      {
        params:
        {
            u_qty: this.u_qty,
            u_title: this.u_title
        }

      })
      .then (response => {this.testMessage = response.data})
      alert("Ticket Updated")
      setTimeout(location.reload.bind(location), 250);
    },
    deleteTicket: function()
    {
      axios.get('http://localhost:5000/delete_ticket',
      {
          u_title: this.u_title
      })
      .then (response => {this.testMessage = response.data})
      alert("Ticket Deleted")
      setTimeout(location.reload.bind(location), 250);
    },
    purchase: function()
    {
      this.showcart2 = true
      axios.get('http://localhost:5000/purchaseNow')
      .then(response => {this.testMessage = response.data});
    }
    }
  }
)
