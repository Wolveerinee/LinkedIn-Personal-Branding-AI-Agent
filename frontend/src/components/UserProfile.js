import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './UserProfile.css';

function UserProfile() {
  const [profile, setProfile] = useState({
    name: '',
    headline: '',
    about: '',
    skills: '',
    experience: '',
    education: '',
    interests: ''
  });

  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    // For now, we'll use mock data
    setProfile({
      name: 'John Doe',
      headline: 'Software Engineer at XYZ Corp',
      about: 'Passionate about AI and machine learning with 5+ years of experience in software development.',
      skills: 'Python, JavaScript, Machine Learning, Data Science, React',
      experience: 'Software Engineer at XYZ Corp (2020-Present)\nSenior Developer at ABC Inc (2018-2020)',
      education: 'MSc Computer Science, ABC University (2018)\nBSc Computer Science, DEF College (2016)',
      interests: 'Technology, Innovation, Professional Development'
    });
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real application, you would send this data to your backend API
    console.log('Profile updated:', profile);
    setIsEditing(false);
  };

  return (
    <div className="user-profile">
      <h1>User Profile</h1>
      
      {!isEditing ? (
        <div className="profile-view">
          <div className="profile-header">
            <div className="profile-avatar">
              <div className="avatar-placeholder">JD</div>
            </div>
            <div className="profile-info">
              <h2>{profile.name}</h2>
              <p className="headline">{profile.headline}</p>
            </div>
          </div>
          
          <div className="profile-section">
            <h3>About</h3>
            <p>{profile.about}</p>
          </div>
          
          <div className="profile-section">
            <h3>Skills</h3>
            <p>{profile.skills}</p>
          </div>
          
          <div className="profile-section">
            <h3>Experience</h3>
            <p className="experience">{profile.experience}</p>
          </div>
          
          <div className="profile-section">
            <h3>Education</h3>
            <p className="education">{profile.education}</p>
          </div>
          
          <div className="profile-section">
            <h3>Interests</h3>
            <p>{profile.interests}</p>
          </div>
          
          <button className="btn" onClick={() => setIsEditing(true)}>
            Edit Profile
          </button>
        </div>
      ) : (
        <form className="profile-edit" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={profile.name}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="headline">Headline</label>
            <input
              type="text"
              id="headline"
              name="headline"
              value={profile.headline}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="about">About</label>
            <textarea
              id="about"
              name="about"
              value={profile.about}
              onChange={handleInputChange}
              rows="4"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="skills">Skills</label>
            <input
              type="text"
              id="skills"
              name="skills"
              value={profile.skills}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="experience">Experience</label>
            <textarea
              id="experience"
              name="experience"
              value={profile.experience}
              onChange={handleInputChange}
              rows="4"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="education">Education</label>
            <textarea
              id="education"
              name="education"
              value={profile.education}
              onChange={handleInputChange}
              rows="4"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="interests">Interests</label>
            <input
              type="text"
              id="interests"
              name="interests"
              value={profile.interests}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-actions">
            <button type="submit" className="btn">Save Changes</button>
            <button 
              type="button" 
              className="btn btn-secondary" 
              onClick={() => setIsEditing(false)}
            >
              Cancel
            </button>
          </div>
        </form>
      )}
    </div>
  );
}

export default UserProfile;