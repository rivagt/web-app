// import React, { Component } from 'react';
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';  // nuevo

import App from './App.jsx';

ReactDOM.render((
  // new
  <Router>
    <App />
  </Router>
), document.getElementById('root'))
