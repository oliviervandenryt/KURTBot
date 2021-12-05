// --PARAMETERS--

// -Time slots-
let times = [
    ["14:00:00", "19:00:00"],
    ["10:00:00", "14:00:00"],
    ["19:00:00", "00:00:00"],
    ["08:00:00", "10:00:00"]
];
// -Seat ID-
let sid = '012345';
// -User ID-
let user = 'rxxxxxxx';
// -Days in advance (def. 4)-
let days_in_advance = 4;
// -Subject-
let subject = 'Study';
// --CODE, DO NOT TOUCH--

// Create date function & object
Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}
var date = new Date();
var usedDate = date.addDays(days_in_advance);

// Encode subject
let subject_base = btoa(subject);
// Get session-id
var newSessionID;
let sessionFetch = await fetch(`https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/WebProxy/WebProxy.svc/CallService?webserviceUrl=https://wsrts.ghum.kuleuven.be/service1.asmx/GetSessionID2?CurrentUID=${user}`);
newSessionID = await sessionFetch.json();
// Reserve function
var reserve = async _ => {
    // Loops over each timeslot
    for (var i = 0; i < times.length; i++) {
        var currentTimes = times[i];
        const starttime = currentTimes[0];
        const endtime = currentTimes[1];
        console.log('Starting with ' + starttime + '-' + endtime);
        // Compensating for end at the next day
        if (endtime == "00:00:00") {
            var usedDate2 = usedDate.addDays(1);
        } else {
            var usedDate2 = usedDate;
        }
        // Generating GET-URL string
        var stringDate = usedDate.getFullYear() + '-' +
            String(usedDate.getMonth() + 1).padStart(2, '0') + '-' +
            String(usedDate.getDate()).padStart(2, '0');
        var stringDate2 = usedDate2.getFullYear() + '-' +
            String(usedDate2.getMonth() + 1).padStart(2, '0') + '-' +
            String(usedDate2.getDate()).padStart(2, '0');
        let url = `https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc/CallWebservice?webserviceUrl=/CreateReservation4?CurrentUID=${user}%26SelectedResourceID=${sid}%26SelectedBeginDatestring=${stringDate}%20${starttime}%26SelectedEndDatestring=${stringDate2}%20${endtime}%26Subject=${subject_base}%26Body=%26OtherUsers=%26Answer=%26ImpersonatedUID=%26SessionID=${newSessionID}`;
        // Sending request to server
        (async () => {
            const res = await fetch(url);
            const data = await res.text();
            // Retries when response is too short
            console.log(data);
            if (data.length < 5) {
                alert(starttime + ' - ' + endtime + ': FAILED, trying again\n');
                const res = await fetch(url);
                const data = await res.json();
                console.log(data);
                }
            else {
                console.log(starttime + ' - ' + endtime + ':\n' + data.slice(54, -9) + '\n');
            }
        })();
    }
}

reserve();
