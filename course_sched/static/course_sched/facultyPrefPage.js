function toggleAddFacultyForm() {
    $("#alertMessage").hide()
    $("#newFaculty").show()
}
$(document).ready(function () {
    $("#addForm").submit(function (event) {
        $.ajax({
            type: "POST",
            url: "/course_sched/faculty_manager/add/",
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: JSON.stringify($("#addForm").serialize()),
            dataType: "json",
            // data: $("#addForm").serialize(),
            success: function (data) {
                if (data.isEmailTaken) {
                    $('#alertMessage').html('A user with that email already exists!')
                } else {
                    $('#alertMessage').html('Successfully added user!')
                }
                $('#alertMessage').show()
                $('#f_table').load(document.URL + ' #f_table')
                $("#newFaculty").hide()
            },
        });
        return false; //<---- move it here
    });
});