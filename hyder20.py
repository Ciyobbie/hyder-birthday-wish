from flask import Flask, render_template_string

app = Flask(__name__)

# The HTML, CSS, and JS all in one template string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday Hyder! 🎂</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;600&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffe6f2 0%, #fff0f5 100%);
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            overflow-x: hidden;
        }

        .container {
            background: rgba(255, 255, 255, 0.9);
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            max-width: 90%;
            width: 400px;
            backdrop-filter: blur(5px);
            margin: 20px;
        }

        h1 {
            font-family: 'Pacifico', cursive;
            color: #ff66b2;
            font-size: 2.2rem;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }

        .generic-wish {
            color: #666;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 25px;
            font-style: italic;
            border-bottom: 1px solid #ffe6f2;
            padding-bottom: 20px;
        }

        .personal-message {
            color: #555;
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 30px;
            white-space: pre-line;
            font-weight: 500;
        }

        .signature {
            font-weight: 600;
            color: #ff3366;
            margin-top: 10px;
            display: block;
        }

        .heart {
            color: #ff3366;
            font-size: 3rem;
            animation: pulse 1s infinite;
            display: inline-block;
            margin-top: 10px;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-10px);}
            60% {transform: translateY(-5px);}
        }

        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.2);}
            100% {transform: scale(1);}
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Happy Birthday Hyder! 🎂</h1>
        
        <!-- Original Generic Wish -->
        <div class="generic-wish">
            Wishing you a day filled with love, laughter, and all your favorite things. May the day be as beautiful as you.<br>
            May this year bring you endless joy and success.
        </div>

        <!-- Your Personal Message -->
        <div class="personal-message">
            happy 20th birthday Hyder <br>
            its sad we couldnt celebrate together as we always do<br>
            but know that am happy for u.
            <span class="signature">much love from yobbie</span>
        </div>

        <div class="heart">❤️</div>
    </div>

    <!-- Confetti Script -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        window.onload = function() {
            var duration = 4 * 1000;
            var animationEnd = Date.now() + duration;
            var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

            function randomInRange(min, max) {
              return Math.random() * (max - min) + min;
            }

            var interval = setInterval(function() {
              var timeLeft = animationEnd - Date.now();

              if (timeLeft <= 0) {
                return clearInterval(interval);
              }

              var particleCount = 50 * (timeLeft / duration);
              confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
              confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
            }, 250);
        };
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)