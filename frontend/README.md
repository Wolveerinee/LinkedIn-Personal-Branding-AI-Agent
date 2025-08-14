# LinkedIn Personal Branding AI Agent - Frontend

This is the frontend application for the LinkedIn Personal Branding AI Agent, built with React.

## Features

- User profile management
- Content creation and editing
- Content calendar for scheduling posts
- Analytics dashboard with performance metrics
- Responsive design for all device sizes

## Prerequisites

- Node.js (version 14 or higher)
- npm (version 6 or higher) or yarn

## Getting Started

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Navigate to the frontend directory:

   ```
   cd frontend
   ```

3. Install dependencies:

   ```
   npm install
   ```

   or

   ```
   yarn install
   ```

4. Start the development server:

   ```
   npm start
   ```

   or

   ```
   yarn start
   ```

5. Open your browser and visit `http://localhost:3000`

## Project Structure

```
src/
  ├── components/       # React components
  ├── services/         # API service files
  ├── assets/           # Images, icons, and other assets
  ├── styles/           # Global styles and theme files
  ├── utils/            # Utility functions
  ├── App.js            # Main App component
  └── index.js          # Entry point
```

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in development mode.
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.

### `npm run build`

Builds the app for production to the `build` folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.
Your app is ready to be deployed!

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## API Integration

The frontend connects to the backend API at `http://localhost:8000/api/v1/` by default. Update the API URL in the service files if your backend is hosted elsewhere.

## Deployment

The frontend can be deployed to any static hosting service like Netlify, Vercel, or GitHub Pages. Run `npm run build` to create a production build.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a pull request

## License

This project is licensed under the MIT License.
