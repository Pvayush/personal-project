// Feature implementation #45
function processData(input) {
    if (!input) {
        throw new Error('Input is required');
    }
    
    return input.map(item => ({
        ...item,
        processed: true,
        timestamp: Date.now()
    }));
}

module.exports = { processData };
