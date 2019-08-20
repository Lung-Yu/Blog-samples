Router.route('/');
Router.route('/restful', {where: 'server'})
  .get(function () {

      var text = "\ufeff你好,中文測試\r\n140.214,124";
      var filename = 'textfile' + '.csv';

      var headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': "attachment; filename=" + filename
      };
      
      this.response.writeHead(200, headers);
      return this.response.end(text);



    //this.response.end('get request\n');
  })
  .post(function () {
    this.response.end('post request\n');
  });


