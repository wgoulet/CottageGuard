import logo from './logo.svg';
import './App.css';
import React from 'react';
import ReactDOM from 'react-dom';
import OAuth2Login from 'react-simple-oauth2-login';

function App() {
  const onSuccess = response => console.log(response);
  const onFailure = response => console.error(response);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <OAuth2Login
          authorizationUrl="https://dev-8623542.okta.com/oauth2/default/v1/authorize"
          responseType="code"
          scope="openid"
          clientId="0oa3gtqcwmMDECDNa5d7"
          redirectUri="http://localhost:3000/oauth-callback"
          onSuccess={onSuccess}
          onFailure={onFailure}/>
      </header>
    </div>
  );
}

export default App;
