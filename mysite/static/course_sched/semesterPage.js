function toggleAddCourse() {
    $("#alertMessage").hide()
    $("#newCourse").toggle()
}
$(document).ready(function () {
    $("#addForm").submit(function (event) {
        $.ajax({
            type: "POST",
            url: "/course_sched/semester_manager/add_course/",
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: $("#addForm").serialize(),
            dataType: "json",
            // data: $("#addForm").serialize(),
            success: function (data) {
                console.log('adfasfasd')
                if (data.isEmailTaken) {
                    $('#alertMessage').html('A class with this CRN already exists!')
                } else {
                    $('#alertMessage').html('Successfully added course!')
                }
                $('#alertMessage').show()
                $('#f_table').load(document.URL + ' #f_table')
                $("#newCourse").hide()
            },
            error: function (data) {
                console.log('bad error')
            }
        });
        return false; //<---- move it here
    });
});
// function addFaculty(path) {
//     var form = document.getElementById("addForm")
//     form.onsubmit = function (e) {
//         console.log('adding the faculty')
//         e.preventDefault()
//         var data = {
//             name: document.getElementById("name").value,
//             email: document.getElementById("email").value,
//             role: document.getElementById("role").value,
//         }
//         var xhr = new XMLHttpRequest()
//         xhr.open("POST", '/course_sched/faculty_manager/add/', true)
//         xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
//         xhr.send(JSON.stringify(data))
//         xhr.onloadend = function () {
//             console.log(xhr)
//             toggleAddFacultyForm()
//             $('#f_table').load(document.URL + ' #f_table')
//             console.log('done updating')
//         }
//     }
// }