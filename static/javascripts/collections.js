(function ($, Backbone, _, app) {
  app.collections.Bucketlists = Backbone.Collection.extend({
    model: app.models.Bucketlist,
    url: '/bucketlists/'
  });
  app.collections.Items = Backbone.Collection.extend({
    model: app.models.Items,
    url: '/items/'
  });
  app.collections.Users = Backbone.Collection.extend({
    model: app.models.Users,
    url: '/users/'
  });
  app.bucketlists = new app.collections.Bucketlists();
  app.items       = new app.collections.Items();
  app.users       = new app.collections.Users();
})(jQuery, Backbone, _, app);
