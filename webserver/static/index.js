var logdiv = $("#moodlog");
var actions;
var moods;

$.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/api/logs/',
    success: function (response) {
        for (let moodlog of response) {

            logdiv.append(`
                <p>${moodlog.note}</p>
                <span class="tag">Mood: ${moodlog.mood.emoji} ${moodlog.mood.title}</span>
                <span class="tag">Action: ${moodlog.action.emoji} ${moodlog.action.title}</span>
                <hr>
            `);
        };
    }
});


$.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/api/moods/',
    success: function (response) {
        moods = response;

        for (let mood of moods) {
            $("#umood").append(`<option value=${mood.id}> ${mood.emoji} ${mood.title}</option>`)
        };
    }
});



$.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/api/actions/',
    success: function (response) {
        actions = response;
        for (let action of actions) {
            $("#uaction").append(`<option value=${action.id}> ${action.emoji} ${action.title}</option>`)
        };
    }
});


$("#submit").on("click", function () {
    let moodid = $("#umood").find(":selected").val();
    let actionid = $("#uaction").find(":selected").val();

    moodobj = moods.filter((obj) => obj.id == moodid)[0];
    actionobj = actions.filter((obj) => obj.id == actionid)[0];

    let note = $("#unote").val();
    let postdata = {};
    postdata.mood = moodobj;
    postdata.action = actionobj;
    postdata.note = note;

    $.ajax({
        type: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        url: 'http://127.0.0.1:8000/api/logs/',
        data: JSON.stringify([postdata]),
        success: function (response) {
            console.log(response);
        }
    });
});