const path = require('path');
const merge = require('webpack-merge');
const { CleanWebpackPlugin }= require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

const common = require('./webpack.common');

module.exports = merge(common, {
  mode: 'production',
  output: {
    path: path.resolve(__dirname, './main/static/main/dist'),
    filename: '[name].[contentHash].js'
  },
  optimization: {
    minimizer: [
      new OptimizeCssAssetsPlugin(),
      new TerserPlugin()
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      path: path.resolve(__dirname, './main/static/main/dist'),
      filename: '[name].[contentHash].css'
    }),
    new CleanWebpackPlugin(),
    new BundleTracker({
      path: path.resolve(__dirname, './dist'),
      filename: './stats.json'
    })
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  }
});
