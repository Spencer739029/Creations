const quotes = [
  "The only limit to our realization of tomorrow is our doubts of today.",
  "In the middle of every difficulty lies opportunity.",
  "Life is 10% what happens to us and 90% how we react to it.",
  "Success is not final, failure is not fatal: It is the courage to continue that counts.",
  "Believe you can and you're halfway there.",
  "Don't watch the clock; do what it does. Keep going.",
  "Hardships often prepare ordinary people for an extraordinary destiny.",
  "You miss 100% of the shots you don't take.",
  "Do something today that your future self will thank you for.",
  "Start where you are. Use what you have. Do what you can.",
  "Dream big and dare to fail.",
  "It's not whether you get knocked down, it's whether you get up.",
  "The future belongs to those who believe in the beauty of their dreams.",
  "Your time is limited, don’t waste it living someone else’s life.",
  "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
  "Work hard in silence, let your success be your noise.",
  "You don’t have to be great to start, but you have to start to be great.",
  "Push yourself, because no one else is going to do it for you.",
  "Great things never come from comfort zones.",
  "Little things make big days.",
  "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
  "Do not watch the clock. Do what it does. Keep going. – Sam Levenson",
  "Everything you can imagine is real. – Pablo Picasso",
  "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
  "Believe you can and you're halfway there. – Theodore Roosevelt",
  "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
  "Act as if what you do makes a difference. It does. – William James",
  "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
  "Don't count the days, make the days count. – Muhammad Ali",
  "It always seems impossible until it's done. – Nelson Mandela",
  "Try to be a rainbow in someone's cloud. – Maya Angelou",
  "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
  "Turn your wounds into wisdom. – Oprah Winfrey",
  "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
  "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
  "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. – Roy T. Bennett",
  "With the new day comes new strength and new thoughts. – Eleanor Roosevelt",
  "The best way to predict the future is to create it. – Peter Drucker",
  "You miss 100% of the shots you don’t take. – Wayne Gretzky",
  "If you want to lift yourself up, lift up someone else. – Booker T. Washington",
  "Limit your 'always' and your 'nevers'. – Amy Poehler",
  "Nothing is impossible. The word itself says 'I'm possible!' – Audrey Hepburn",
  "You do not find the happy life. You make it. – Camilla Eyring Kimball",
  "Be yourself; everyone else is already taken. – Oscar Wilde",
  "Life is short, and it's up to you to make it sweet. – Sarah Louise Delany",
  "In a gentle way, you can shake the world. – Mahatma Gandhi",
  "You must be the change you wish to see in the world. – Mahatma Gandhi",
  "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
  "I never dream of success. I work for it. – Estée Lauder",
  "Be so good they can’t ignore you. – Steve Martin"
];

const usedIndexes = new Set()
const quoteElement = document.getElementById("quote")

function generateQuote() {
  if (usedIndexes.size >= quotes.length){
    usedIndexes.clear()
  }

  while (true) {
    const randomIdx = Math.floor(Math.random() * quotes.length)

    if (usedIndexes.has(randomIdx)) continue

    const quote = quotes[randomIdx]
    quoteElement.innerHTML = quote;
    usedIndexes.add(randomIdx)
    break
  }
}