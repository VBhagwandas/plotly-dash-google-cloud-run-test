Paddle.Environment.set('sandbox');
Paddle.Setup({ vendor: 3137 });

Paddle.Audience.Popup({
  vendorName: 'Your Company Name',
  triggers: {
    exitIntent: false,
    scrollDepth: false,
    timed: 10
  },
  strings: {
    heading: "Stay up to date!",
    subHeading: "Never miss a new feature, release, announcement or deal. Sign up to our newsletter today!",
    cta: "Sign me up!"
  }
});
