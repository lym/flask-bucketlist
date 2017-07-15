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
    templateName: '#bucketlists-index-template',
    initialize  : function (options) {
      var self = this;
      TemplateView.prototype.initialize.apply(this, arguments);
      app.bucketlists.fetch({
        success: function () {
          self.render();
        }
      });
    },

    getContext  : function () {
      return {bucketlists: app.bucketlists || null};
    }
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

  var SignupView = FormView.extend({
    id: 'signup',
    templateName: '#signup-template',
    submit: function (event) {
      var data = {};
      // Call parent class' submit method
      FormView.prototype.submit.apply(this, arguments);
      data = this.serializeForm(this.form);
      console.log(data);
      $.post(app.registerURL, data)
        .success($.proxy(this.registerSuccess, this))
        .fail($.proxy(this.registerFailure, this));
    },
    registerSuccess: function (data) {
      // TODO: Message with, "An email has been sent to your inbox, click link
      // to confirm account regn.
      // app.session.save(data.token);
      // this.done();
      this.done();  // trigger 'done' event
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

  var BucketlistCreateView = FormView.extend({
    templateName: '#bucketlist-create-view',
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

  var NewItemView = FormView.extend({
    templateName: '#item-create-view',
    initialize: function (bucketlistId) {
      this.bucketlistId = bucketlistId;
      FormView.prototype.initialize.apply(this, arguments);
    },
    submit: function (event) {
      var data = {};
      // Call parent class' submit method
      FormView.prototype.submit.apply(this, arguments);
      data = this.serializeForm(this.form);
      console.log(data);
      $.post(app.itemsURL, data)
        .success($.proxy(this.loginSuccess, this))
        .fail($.proxy(this.loginFailure, this));
    },
    getContext: function () {
      console.log(this.bucketlistId);
      return {'bucketlistId': this.bucketlistId};
    }
  });

  var BucketlistShowView = TemplateView.extend({
    templateName: '#bucketlist-view',
    events: {'click button.add-item': 'renderNewItemForm'},
    initialize: function (options) {
      var self = this;
      TemplateView.prototype.initialize.apply(this, arguments);
      this.bucketlistId = options.bucketlistId;
      this.bucketlist = null;
      self.bucketlist = app.bucketlists.push({id: self.bucketlistId});
      self.bucketlist.fetch({
        url: '/bucketlists/?item=' + self.bucketlistId,
        success: function () {
          self.render();
        }
      });
    },
    getContext: function () {
      return {bucketlist: this.bucketlist};
    },
    renderNewItemForm: function (event) {
      console.log('Attempting to add item...')
      var view  = new NewItemView(this.bucketlist.get('id'));
      var link  = $(event.currentTarget);
      event.preventDefault();
      link.before(view.el);
      link.hide();
      view.render();
      view.on('done', function () {
        link.show();
      });

    }
  });

  app.views.HomepageView        = HomepageView;
  app.views.LoginView           = LoginView;
  app.views.SignupView          = SignupView;
  app.views.HeaderView          = HeaderView;
  app.views.BucketlistCreateView = BucketlistCreateView;
  app.views.BucketlistShowView   = BucketlistShowView;
})(jQuery, Backbone, _, app);
