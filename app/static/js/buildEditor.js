const visibilityModal = document.getElementById('visibilityModal');
visibilityModal.addEventListener('hidden.bs.modal', (e) => {
    // var e = document.getElementById("visibility-select");
    // document.getElementById('visibilitySelected').value = e.value;
});

const meleeModal = document.getElementById('meleeModal');
meleeModal.addEventListener('hidden.bs.modal', (e) => {
    // var e = document.getElementById("weapon-select");
    // document.getElementById('weaponSelected').value = e.value;
    // // set flask variable to match weapon
    // var flask = document.getElementById("flask-select");
});

const rangedModal = document.getElementById('rangedModal');
rangedModal.addEventListener('hidden.bs.modal', (e) => {
    // var e = document.getElementById("ranged-select");
    // document.getElementById('rangedSelected').value = e.value;
});

// Curio One Modals

const curioOneModal = document.getElementById('curioOneModal');
curioOneModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioOne-select");
    document.getElementById('curioOneSelected').value = e.value;
});

const curioOneBlessingModal = document.getElementById('curioOneBlessingModal');
curioOneModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioOneBlessing-select");
    document.getElementById('curioOneBlessingSelected').value = e.value;
});

const curioOnePerkOneModal = document.getElementById('curioOnePerkOneModal');
curioOnePerkOneModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioOnePerkOne-select");
    document.getElementById('curioOnePerkOneSelected').value = e.value;
});

const curioOnePerkTwoModal = document.getElementById('curioOnePerkTwoModal');
curioOnePerkTwoModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioOnePerkTwo-select");
    document.getElementById('curioOnePerkTwoSelected').value = e.value;
});

const curioOnePerkThreeModal = document.getElementById('curioOnePerkThreeModal');
curioOnePerkThreeModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioOnePerkThree-select");
    document.getElementById('curioOnePerkThreeSelected').value = e.value;
});

// Curio Two Modals

const curioTwoModal = document.getElementById('curioTwoModal');
curioTwoModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioTwo-select");
    document.getElementById('curioTwoSelected').value = e.value;
});

const curioTwoBlessingModal = document.getElementById('curioTwoBlessingModal');
curioTwoModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioTwoBlessing-select");
    document.getElementById('curioTwoBlessingSelected').value = e.value;
});

const curioTwoPerkOneModal = document.getElementById('curioTwoPerkOneModal');
curioTwoPerkOneModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioTwoPerkOne-select");
    document.getElementById('curioTwoPerkOneSelected').value = e.value;
});

const curioTwoPerkTwoModal = document.getElementById('curioTwoPerkTwoModal');
curioTwoPerkTwoModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioTwoPerkTwo-select");
    document.getElementById('curioTwoPerkTwoSelected').value = e.value;
});

const curioTwoPerkThreeModal = document.getElementById('curioTwoPerkThreeModal');
curioTwoPerkThreeModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioTwoPerkThree-select");
    document.getElementById('curioTwoPerkThreeSelected').value = e.value;
});

// Curio Three Modals 

const curioThreeModal = document.getElementById('curioThreeModal');
curioThreeModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioThree-select");
    document.getElementById('curioThreeSelected').value = e.value;
});

const curioThreeBlessingModal = document.getElementById('curioThreeBlessingModal');
curioThreeModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioThreeBlessing-select");
    document.getElementById('curioThreeBlessingSelected').value = e.value;
});

const curioThreePerkOneModal = document.getElementById('curioThreePerkOneModal');
curioThreePerkOneModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioThreePerkOne-select");
    document.getElementById('curioThreePerkOneSelected').value = e.value;
});

const curioThreePerkTwoModal = document.getElementById('curioThreePerkTwoModal');
curioThreePerkTwoModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioThreePerkTwo-select");
    document.getElementById('curioThreePerkTwoSelected').value = e.value;
});

const curioThreePerkThreeModal = document.getElementById('curioThreePerkThreeModal');
curioThreePerkThreeModal.addEventListener('hidden.bs.modal', (e) => {
    var e = document.getElementById("curioThreePerkThree-select");
    document.getElementById('curioThreePerkThreeSelected').value = e.value;
});

// Melee Perks

const meleePerkOneModal = document.getElementById('meleePerkOneModal');
meleePerkOneModal.addEventListener('hidden.bs.modal', (e) => {
    // var e = document.getElementById("meleePerkOne-select");
    // document.getElementById('meleePerkOneSelected').value = e.value;
});

const meleePerkTwoModal = document.getElementById('meleePerkTwoModal');
meleePerkTwoModal.addEventListener('hidden.bs.modal', (e) => {
    // var e = document.getElementById("meleePerkTwo-select");
    // document.getElementById('meleePerkTwoSelected').value = e.value;
});

// Ranged Perks 

const rangedPerkOneModal = document.getElementById('rangedPerkOneModal');
rangedPerkOneModal.addEventListener('hidden.bs.modal', (e) => {
});

const rangedPerkTwoModal = document.getElementById('rangedPerkTwoModal');
rangedPerkTwoModal.addEventListener('hidden.bs.modal', (e) => {
});


// Melee Blessings 

const meleeBlessingOneModal = new bootstrap.Modal(document.getElementById('meleeBlessingOneModal'), {
    keyboard: true
});

const meleeBlessingTwoModal = new bootstrap.Modal(document.getElementById('meleeBlessingTwoModal'), {
    keyboard: true
});


// Ranged Blessings 

const rangedBlessingOneModal = new bootstrap.Modal(document.getElementById('rangedBlessingOneModal'), {
    keyboard: true
});

const rangedBlessingTwoModal = new bootstrap.Modal(document.getElementById('rangedBlessingTwoModal'), {
    keyboard: true
});


const level5Cards = document.querySelectorAll('.level5-card');
level5Cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level5Cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

const level10cards = document.querySelectorAll('.level10-card');
level10cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level10cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

const level15cards = document.querySelectorAll('.level15-card');
level15cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level15cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

const level20cards = document.querySelectorAll('.level20-card');
level20cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level20cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

const level25cards = document.querySelectorAll('.level25-card');
level25cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level25cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

const level30cards = document.querySelectorAll('.level30-card');
level30cards.forEach((card) => {
    card.addEventListener('click', (e) => {
        level30cards.forEach((card) => {
            if (card.classList.contains('selectedCard')) {
                card.classList.remove('selectedCard');
            }
        });
        card.classList.toggle('selectedCard');
    });
});

