
const render = require('./render');
const router = require('koa-router')();
const koaBody = require('koa-body');

const Koa = require('koa');
const app = module.exports = new Koa();

app.use(render);
app.use(koaBody());

router.get('/', list);
async function list(ctx) {
    await ctx.render('new.html');
};

app.use(router.routes());



if (!module.parent) app.listen(3000);