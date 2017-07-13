(function ($, Backbone, _, app) {
  /* View to handle all the homepage rendering logic
   */

  // Generic template view
  var TemplateView = Backbone.View.extend({
    templateName: '',
    initialize: function () {
      this.template = _.template($(this.templateName).html());
    },
    render: function () {
      var context = this.getContext();
      var html    = this.template(context);
      this.$el.html(html);
    },
    getContext: function () {
      return {};
    }
  });

  // Generic form view
  var FormView = TemplateView.extend({
    events: {'submit form': 'submit'},
    errorTemplate: _.template('<span class"error"><%- msg %></span>'),
    clearErrors: function () {
      $('.error', this.form).remove();
    },
    showErrors: function (errors) {
      _.map(errors, function (fieldErrors, name) {
        var field = $(':input[name=' + name + ']', this.form);
        var label = $('label[for=' + field.attr('id') + ']', this.form);
        if (label.length === 0) {
          label = $('label', this.form).first();
        }
        function appendError(msg) {
          label.before(this.errorTemplate({msg: msg}));
        }
        _.map(fieldErrors, appendError, this);
      }, this);
    },
    serializeForm: function (form) {
      return _.object(_.map(form.serializeArray(), function (item) {
        return [item.name, item.value];
      }));
    },
    submit: function (event) {
      console.log('submitting....');
      event.preventDefault();
      this.form = $(event.currentTarget);
      this.clearErrors();
    },
    failure: function (xhr, status, error) {
      var errors = xhr.responseJSON;
      this.showErrors(errors);
    },
    done: function (event) {
      if (event) {
        event.preventDefault();
      }
      this.trigger('done');
      this.remove();
    }
  });

  var HomepageView = TemplateView.extend({
    templateName: '#home-template',
  });

  var LoginView = FormView.extend({
    id: 'login',
    templateName: '#login-template',
    submit: function (event) {
      var data = {};
      // Call parent class' submit method
      FormView.prototype.submit.apply(this, arguments);
      data = this.serializeForm(this.form);
      console.log(data);
      $.post(app.loginURL, data)
        .success($.proxy(this.loginSuccess, this))
        .fail($.proxy(this.loginFailure, this));
    },
    loginSuccess: function (data) {
      app.session.save(data.token);
      this.done();
    }
  });

  var HeaderView = TemplateView.extend({
    tagName: 'header',
    templateName: '#header-template',
    events: {
      'click .logout': 'logout',
    },
    getContext: function () {
      return {authenticated: app.session.authenticated()}
    },
    logout: function (event) {
      event.preventDefault();
      app.session.delete();
      window.location = '/'
    }
  });

  var BucketlistsIndexView = TemplateView.extend({
    templateName: '#bucketlists-index-template',
  });

  var BucketlistCreateView = FormView.extend({
    templateName: '#bucketlist-create-view',
    // events: {'click button.create-list': 'createList'},
    submit: function (event) {
      var data = {};
      // Call parent class' submit method
      FormView.prototype.submit.apply(this, arguments);
      data = this.serializeForm(this.form);
      console.log(data);
      $.post(app.bucketlistsURL, data)
        .success($.proxy(this.loginSuccess, this))
        .fail($.proxy(this.loginFailure, this));
    },
  });

  var UserRegistrationView = FormView.extend({
    templateName: '#user-create-view',
    submit: function (event) {
      var data = {};
      // Call parent class' submit method
      FormView.prototype.submit.apply(this, arguments);
      data = this.serializeForm(this.form);
      console.log(data);
      $.post(app.usersURL, data)
        .success($.proxy(this.loginSuccess, this))
        .fail($.proxy(this.loginFailure, this));
    },
  });

  var BucketlistShowView = TemplateView.extend({
    templateName: '#bucketlist-view'
  });

  app.views.HomepageView        = HomepageView;
  app.views.LoginView           = LoginView;
  app.views.HeaderView          = HeaderView;
  app.views.BucketlistsIndexView = BucketlistsIndexView;
  app.views.BucketlistCreateView = BucketlistCreateView;
  app.views.BucketlistShowView   = BucketlistShowView;
  app.views.UserRegistrationView = UserRegistrationView;
})(jQuery, Backbone, _, app);
