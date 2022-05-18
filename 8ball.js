function eightball(){
    username = prompt("What is your name?");
    console.log(`Welcome, ${username}, to Aryan's eight-ball service`);
    question = prompt("What is the question that you are asking?");
    console.log(`${username} is asking, " ${question} " . Let's figure out what the eight-ball has to say`)
    number = Math.floor(Math.random(1,8))
    console.log(number)
}