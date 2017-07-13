var app = (function ($) {
  // application setup
  var config  = $('#config');
  var app     = JSON.parse(config.text());
  // router needs to wait for DOM to be ready
  $(document).ready(function () {
    var router = new app.router();
  });

  return app;
})(jQuery);
