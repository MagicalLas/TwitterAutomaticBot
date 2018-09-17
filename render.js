const views = require('koa-views');
const path = require('path');

module.exports = views(path.join(__dirname, '/../TwitterAutomaticBot/views'), {
  map: { html: 'swig' }
});