const form = document.getElementById('build-editor');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const meleePerkOne = document.getElementById('meleePerkOneSelected').value;
    const meleePerkTwo = document.getElementById('meleePerkTwoSelected').value;
    const meleeBlessingOne = document.getElementById('meleeBlessingOneSelected').value;
    const meleeBlessingTwo = document.getElementById('meleeBlessingTwoSelected').value;
    const rangedPerkOne = document.getElementById('rangedPerkOneSelected').value;
    const rangedPerkTwo = document.getElementById('rangedPerkTwoSelected').value;
    const rangedBlessingOne = document.getElementById('rangedBlessingOneSelected').value;
    const rangedBlessingTwo = document.getElementById('rangedBlessingTwoSelected').value;
    const curioOnePerkOne = document.getElementById('curioOnePerkOneSelected').value;
    const curioOnePerkTwo = document.getElementById('curioOnePerkTwoSelected').value;
    const curioOnePerkThree = document.getElementById('curioOnePerkThreeSelected').value;
    const curioFirstBlessing = document.getElementById('curioOneBlessingSelected').value;
    const curioTwoPerkOne = document.getElementById('curioTwoPerkOneSelected').value;
    const curioTwoPerkTwo = document.getElementById('curioTwoPerkTwoSelected').value;
    const curioTwoPerkThree = document.getElementById('curioTwoPerkThreeSelected').value;
    const curioSecondBlessing = document.getElementById('curioTwoBlessingSelected').value;
    const curioThreePerkOne = document.getElementById('curioThreePerkOneSelected').value;
    const curioThreePerkTwo = document.getElementById('curioThreePerkTwoSelected').value;
    const curioThreePerkThree = document.getElementById('curioThreePerkThreeSelected').value;
    const curioThirdBlessing = document.getElementById('curioThreeBlessingSelected').value;
    const buildName = document.getElementById('build-name').value;
    const level5Talent = document.getElementById('level5Selected').value;
    const level10Talent = document.getElementById('level10Selected').value;
    const level15Talent = document.getElementById('level15Selected').value;
    const level20Talent = document.getElementById('level20Selected').value;
    const level25Talent = document.getElementById('level25Selected').value;
    const level30Talent = document.getElementById('level30Selected').value;
    if (buildName === '') {
        snackbar('error', 'Build name cannot be empty', 3000);
        return;
    } else if (buildName.length > 100 || buildName.length < 5) {
        snackbar('error', 'Build name must be between 5-100 characters', 3000);
        document.getElementById('build-name').value = '';
        return;
    } else if (meleePerkOne === '') {
        snackbar('error', 'Please select a melee perk', 3000);
        return;
    } else if (meleePerkTwo === '') {
        snackbar('error', 'Please select a melee perk', 3000);
        return;
    } else if (meleeBlessingOne === '') {
        snackbar('error', 'Please select a melee blessing', 3000);
        return;
    } else if (meleeBlessingTwo === '') {
        snackbar('error', 'Please select a melee blessing', 3000);
        return;
    } else if (meleeBlessingOne === meleeBlessingTwo) {
        snackbar('error', 'Please select two different melee blessings', 3000);
        return;
    } else if (rangedPerkOne === '') {
        snackbar('error', 'Please select a ranged perk', 3000);
        return;
    } else if (rangedPerkTwo === '') {
        snackbar('error', 'Please select a ranged perk', 3000);
        return;
    } else if (rangedBlessingOne === '') {
        snackbar('error', 'Please select a ranged blessing', 3000);
        return;
    } else if (rangedBlessingTwo === '') {
        snackbar('error', 'Please select a ranged blessing', 3000);
        return;
    } else if (rangedBlessingOne === rangedBlessingTwo) {
        snackbar('error', 'Please select two different ranged blessings', 3000);
        return;
    } else if (curioFirstBlessing === '' || curioOnePerkOne === '' || curioOnePerkTwo === '' || curioOnePerkThree === '' ) {
        snackbar('error', 'Please select a blessing or perk (first curio)', 3000);
        return;
    } else if (curioOnePerkOne === curioOnePerkTwo || curioOnePerkOne === curioOnePerkThree || curioOnePerkTwo === curioOnePerkThree) {
        snackbar('error', 'Please select different curio perks (first curio)', 3000);
        return;
    } else if (curioSecondBlessing === '' || curioTwoPerkOne === '' || curioTwoPerkTwo === '' || curioTwoPerkThree === '' ) {
        snackbar('error', 'Please select a blessing or perk (second curio)', 3000);
        return;
    } else if (curioTwoPerkOne === curioTwoPerkTwo || curioTwoPerkOne === curioTwoPerkThree || curioTwoPerkTwo === curioTwoPerkThree) {
        snackbar('error', 'Please select three different perks (second curio)', 3000);
        return;
    } else if (curioThirdBlessing === '' || curioThreePerkOne === '' || curioThreePerkTwo === '' || curioThreePerkThree === '' ) {
        snackbar('error', 'Please select a blessing or perk (third curio)', 3000);
        return;
    } else if (curioThreePerkOne === curioThreePerkTwo || curioThreePerkOne === curioThreePerkThree || curioThreePerkTwo === curioThreePerkThree) {
        snackbar('error', 'Please select three different perks (third curio)', 3000);
        return;
    } else if (level5Talent === '') {
        snackbar('error', 'Please select a level 5 talent', 3000);
        return;
    } else if (level10Talent === '') {
        snackbar('error', 'Please select a level 10 talent', 3000);
        return;
    } else if (level15Talent === '') {
        snackbar('error', 'Please select a level 15 talent', 3000);
        return;
    } else if (level20Talent === '') {
        snackbar('error', 'Please select a level 20 talent', 3000);
        return;
    } else if (level25Talent === '') {
        snackbar('error', 'Please select a level 25 talent', 3000);
        return;
    } else if (level30Talent === '') {
        snackbar('error', 'Please select a level 30 talent', 3000);
        return;
    }

    const quill = document.getElementById('editor');
    const quillValue = quill.children[0].innerHTML;
    // check if the word scripts is in the quill value
    if (quillValue.includes('<script>')) {
        snackbar('error', 'Please do not use scripts in the build description you bozo', 3000);
        return;
    } else if (quillValue.includes('<SCRIPT>')) {
        snackbar('error', 'Please do not use scripts in the build description you bozo', 3000);
        return;
    } else if (quillValue.includes('</script>')) {
        snackbar('error', 'Please do not use scripts in the build description you bozo', 3000);
        return;
    } else if (quillValue.includes('</SCRIPT>')) {
        snackbar('error', 'Please do not use scripts in the build description you bozo', 3000);
        return;
    }
    document.getElementById('quillEditor').value = quillValue;
    form.submit();
});