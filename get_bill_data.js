let billData = [];

let gasBills = document.querySelectorAll('span.Configurablestyled__TitleWrapper-sc-1ausqcq-10 span.Configurablestyled__Title-sc-1ausqcq-8 span');

for (let i = 0; i < gasBills.length; i++) {
  if (gasBills[i].innerText === 'Gas') {
    let bill = gasBills[i].parentNode.parentNode;
    let startDate = bill.querySelector('.indexstyled__StyledConsumptionQuantity-sc-z53iik-0.indexstyled__StyledConsumptionRange-sc-z53iik-1.geBygj').innerText.split(' - ')[0];
    let endDate = bill.querySelector('.indexstyled__StyledConsumptionQuantity-sc-z53iik-0.indexstyled__StyledConsumptionRange-sc-z53iik-1.geBygj').innerText.split(' - ')[1];
    let value = bill.querySelector('.Configurablestyled__Amount-sc-1ausqcq-7.hmsJrd').innerText;
    billData.push({
      'start_date': startDate,
      'end_date': endDate,
      'value': value
    });
  }
}

console.log(JSON.stringify(billData));
