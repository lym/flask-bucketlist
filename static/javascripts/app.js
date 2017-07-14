var app = (function ($) {
  // application setup
  var config  = $('#config');
  var app     = JSON.parse(config.text());
  // router needs to wait for DOM to be ready
  $(document).ready(function () {
    var router = new app.router();

    // Lets make iCheck available

    $('input').iCheck({
        checkboxClass: 'icheckbox_square-blue',
        radioClass: 'iradio_square-blue',
        increaseArea: '20%' // optional
      });
  });

  return app;
})(jQuery);
