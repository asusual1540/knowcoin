import { Link } from 'react-router-dom';
import logo from '../assets/logo.svg';
import '../App.css';
import { useEffect, useState } from 'react';
import {API_BASE_URL} from '../config';


function App() {
  const [walletInfo, setWalletInfo] = useState({})

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
      .then(response => response.json())
      .then(json => setWalletInfo(json))
  }, [])

  const {address, balance} = walletInfo


  return (
    <div className="App">
      <div className="App-container">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <h3>Welcome to KnowCoin</h3>
        <br/>
        <Link to="/blockchain">Recent KnowCoin Transactions</Link>
        <Link to="/conduct-transaction">Send KnowCoin</Link>
        <Link to="/transaction-pool">Mine KnowCoin</Link>
        <br/>
        <div className="WaletInfo">
          <div>Address : {address}</div>
          <div>Balance : {balance}</div>
        </div>
      </div>

    </div>
  );
}

export default App;
