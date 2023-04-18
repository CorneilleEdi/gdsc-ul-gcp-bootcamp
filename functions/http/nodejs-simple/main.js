const functions = require('@google-cloud/functions-framework');

functions.http('handler', (req, res) => {
    let word = req.query.word;
    if (word) {
        word = word.split('').reverse().join('');
        return res.status(200).json({word});
    } else {
        return res.status(400).send('No word provided!');
    }
});
