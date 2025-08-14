import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">LinkedIn AI Agent</Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/" className="nav-link">Dashboard</Link>
        </li>
        <li className="nav-item">
          <Link to="/profile" className="nav-link">Profile</Link>
        </li>
        <li className="nav-item">
          <Link to="/calendar" className="nav-link">Content Calendar</Link>
        </li>
        <li className="nav-item">
          <Link to="/analytics" className="nav-link">Analytics</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;