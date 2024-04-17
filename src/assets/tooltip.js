window.dccFunctions = window.dccFunctions || {};
window.dccFunctions.dateParser = function(value) {
    var decimal = Math.round((value - Math.floor(value) + 1/12)*12)
    var num = Math.floor(value)
    return decimal.toString() + '/' + num.toString() ;
}