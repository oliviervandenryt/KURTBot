// --PARAMETERS--

// -Time slots-
let times = [
    ["14:00:00", "19:00:00"],
    ["10:00:00", "14:00:00"],
    ["19:00:00", "00:00:00"],
    ["08:00:00", "10:00:00"]
];
// -Seat ID-
let sid = 'XXXXXX';
// -User ID-
let user = 'rXXXXXXX';
// -Days in advance (def. 4)-
let days_in_advance = 4;
// -Subject-
let subject = 'Study'
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
let subject_base = btoa(subject)
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
        let url = `https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc/CallWebservice?webserviceUrl=/CreateReservation4?CurrentUID=${user}%26SelectedResourceID=${sid}%26SelectedBeginDatestring=${stringDate}%20${starttime}%26SelectedEndDatestring=${stringDate2}%20${endtime}%26Subject=${subject_base}%26Body=%26OtherUsers=%26Answer=%26ImpersonatedUID=%26SessionID=`;
        // Sending request to server
        (async () => {
            const res = await fetch(url);
            const data = await res.json();
            // Retries when response is too short
            if (data.length < 5) {
                alert(starttime + ' - ' + endtime + ': FAILED, trying again\n');
                const res = await fetch(url);
                const data = await res.json();
                alert(starttime + ' - ' + endtime + ':\n' + data.slice(54, -9) + '\n');
                if (data.length < 5) {
                    alert(starttime + ' - ' + endtime + ': FAILED again, try other seat\n');
                    alert(starttime + ' - ' + endtime + ':\n' + data.slice(54, -9) + '\n');
                } else {
                    alert(starttime + ' - ' + endtime + ':\n' + data.slice(54, -9) + '\n');
                }
            } else {
                alert(starttime + ' - ' + endtime + ':\n' + data.slice(54, -9) + '\n');
            }
        })();
    }
}

reserve();
