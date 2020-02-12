new Vue({
    el: '#starting',
    delimiters: ['${', '}'],
    data: {
      currentSort: 'timestamp',
      currentSortDir: 'desc',
      tweets: [],
      loading: false,
      message: null,
      newTweet: {'message': null, 'name': null},
    },
    computed: {
      // a computed getter
      sortedTweets() {
        return this.tweets
            .sort((a, b) => {
              if (this.currentSortDir === 'asc') {
                return a[this.currentSort] >= b[this.currentSort];
              }
              return a[this.currentSort] <= b[this.currentSort];
            })
      },
    },
    mounted: function () {
      this.getTweets();
    },
    methods: {
      getTweets: function () {
        this.loading = false;
        this.$http.get('/api/tweet/')
            .then((response) => {
              this.tweets = response.data;
              this.loading = false;
            })
            .catch((err) => {
              this.loading = true;
              console.log(err);
            })
      },
      addTweet: function () {
        this.loading = true;
        this.$http.post('/api/tweet/', this.newTweet)
            .then((response) => {
              this.loading = false;
              this.getTweets();
              this.newTweet = {};
            })
            .catch((err) => {
              this.loading = false;
              console.log(err);
            })
      },
      sort: function (col) {
        // if you click the same label twice
        if (this.currentSort == col) {
          this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
        } else {
          this.currentSort = col;
        } // end if
      }, // sort
    }
  });