import React from 'react';

// This component renders the Get Started button.
// The label has been updated to "Let's dive in" as per SCRUM-54.
// Existing click handlers are preserved via the onClick prop.

const GetStartedButton = ({ onClick, ...props }) => {
  return (
    <button onClick={onClick} {...props}>
      Let's dive in
    </button>
  );
};

export default GetStartedButton;
