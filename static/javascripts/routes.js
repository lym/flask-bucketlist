(function ($, Backbone, _, app) {
  var ApplicationRouter = Backbone.Router.extend({
    routes: {
      '': 'home',
      'bucketlists_index' : 'bucketlistsIndex',
      'bucketlist_create' : 'bucketlistCreate',
      'bucketlist'        : 'bucketlistShow',
      'user_create'       : 'userCreate'
    },
    initialize: function (options) {
      this.contentElement = '.wrapper';
      this.current        = null;
      this.header         = new app.views.HeaderView();
      $('body').prepend(this.header.el)
      this.header.render();
      Backbone.history.start();
    },
    home: function () {
      var view = new app.views.HomepageView({
        el: this.contentElement
      });
      this.render(view);
    },

    // Redefine the route function to enforce authentication of every view/page
    route: function (route, name, callback) {
      var login;
      callback = callback || this[name];
      callback = _.wrap(callback, function (original) {
        var args = _.without(arguments, original);
        if (app.session.authenticated()) {
          original.apply(this, args);
        } else {
          // We are dealing with a non-logged-in user
          $(this.contentElement).hide();
          $('header').hide();
          login = new app.views.LoginView();
          $(this.contentElement).after(login.el);
          login.on('done', function () {
            $('header').show();
            this.header.render();
            $(this.contentElement).show();
            original.apply(this, args);
          }, this);
          login.render();
        }
      });
      return Backbone.Router.prototype.route.apply(
        this, [route, name, callback]
      );
    },
    render: function (view) {
      if (this.current) {
        this.current.undelegateEvents();
        this.current.$el = $();
        this.current.remove();
      }
      this.current = view;
      this.current.render();
    },
    bucketlistsIndex: function () {
      var view = new app.views.BucketlistsIndexView({el: this.contentElement});
      this.render(view);

    },
    bucketlistCreate: function () {
      var view = new app.views.BucketlistCreateView({el: this.contentElement});
      this.render(view);
    },
    bucketlistShow: function () {
      var view = new app.views.BucketlistShowView({el: this.contentElement});
      this.render(view);
    },
    userCreate: function () {
      var view = new app.views.UserRegistrationView({el: this.contentElement});
      this.render(view);
    },
  });
  app.router = ApplicationRouter;
})(jQuery, Backbone, _, app);
