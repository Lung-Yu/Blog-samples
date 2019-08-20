import { Meteor } from 'meteor/meteor';


Meteor.startup(function () {
    Meteor.methods({
      getCurrentTime: function () {
        console.log('on server, getCurrentTime called');
        return new Date();
      },

      welcome: function (name) {
        console.log('on server, welcome called with name: ', name);
        if(name==undefined || name.length<=0) {
          throw new Meteor.Error(404, "Please enter your name");
        }
        return "Welcome " + name;
      },

    save_csv:function(name){
        console.log('on server, welcome called with name: ', name);
    var text = "This is the awesome text.";
      var filename = 'textfile' + '.txt';

      var headers = {
        'Content-Type': 'text/plain',
        'Content-Disposition': "attachment; filename=" + filename
      };

      //response.writeHead(200, headers);
      //return this.response.end(text);


    }
    });
});
