const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    publicPath: "http://0.0.0.0:8080/",
    outputDir: './dist/',
    chainWebpack: config => {
        config.optimization
            .splitChunks(false)

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://localhost:8000/')
            .headers({"Access-Control-Allow-Origin": ["\*"]})
            .proxy('http://0.0.0.0:8000/')
            .historyApiFallback(true)
    }
};