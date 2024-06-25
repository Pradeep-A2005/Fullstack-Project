function cal() {
    let num1 = document.getElementsByName("num1")[0].value;
    let num2 = document.getElementsByName("num2")[0].value;
    let num3 = document.getElementsByName("num3")[0].value;
    let num4 = document.getElementsByName("num4")[0].value;
    let num5 = document.getElementsByName("num5")[0].value;
    let num6 = document.getElementsByName("num6")[0].value;
    let num7 = document.getElementsByName("num7")[0].value;
    let num8 = document.getElementsByName("num8")[0].value;
    let num9 = document.getElementsByName("num9")[0].value;
    let num10 = document.getElementsByName("num10")[0].value;
    let sum = Number(num1) + Number(num2)+ Number(num3)+Number(num4)+Number(num5)
    +Number(num6)+Number(num7)+Number(num8)+Number(num9)+Number(num10);
    document.getElementsByName("totalMarks")[0].value = sum;
}
    

function calo() {
    let n1 = document.getElementsByName("n1")[0].value;
    let n2 = document.getElementsByName("n2")[0].value;
    let n3 = document.getElementsByName("n3")[0].value;
    let n4 = document.getElementsByName("n4")[0].value;
    let n5 = document.getElementsByName("n5")[0].value;
    let n6 = document.getElementsByName("n6")[0].value;
    let sum2 = Number(n1) + Number(n2) + Number(n3) + Number(n4) + Number(n5) + Number(n6);
    document.getElementsByName("Mark")[0].value = sum2;
}


