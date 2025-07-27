<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Responsive Landing Page</title>
  <style>
    /* Reset default margin and padding */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
    }

    header {
      position: fixed;
      top: 0;
      width: 100%;
      background: #333;
      padding: 15px 0;
      z-index: 1000;
      transition: background 0.3s, box-shadow 0.3s;
    }

    .nav-links {
      list-style: none;
      display: flex;
      justify-content: center;
    }

    .nav-links li {
      margin: 0 20px;
    }

    .nav-links a {
      text-decoration: none;
      color: white;
      font-size: 18px;
      transition: color 0.3s;
    }

    .nav-links a:hover {
      color: #ffcc00;
    }

    .scrolled {
      background: #222;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
    }

    .hero {
      margin-top: 80px;
      height: 100vh;
      background: linear-gradient(to right, #4facfe, #00f2fe);
      color: white;
      text-align: center;
      padding: 100px 20px;
    }

    .hero h1 {
      font-size: 48px;
      margin-bottom: 20px;
    }

    .hero p {
      font-size: 20px;
    }

    @media (max-width: 768px) {
      .nav-links {
        flex-direction: column;
        align-items: center;
      }

      .nav-links li {
        margin: 10px 0;
      }
    }
  </style>
</head>
<body>

  <header id="navbar">
    <nav>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="hero">
    <h1>Welcome to Our Landing Page</h1>
    <p>This is a responsive landing page with a sticky and interactive navigation menu.</p>
  </section>

  <script>
    window.addEventListener('scroll', () => {
      const navbar = document.getElementById('navbar');
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  </script>

</body>
</html>
