function toggleAddFacultyForm() {
    $('#alertMessage').hide()
    $('#newFaculty').toggle()
    $('#editFaculty').hide()
}

function editFaculty(id, name, email, role) {
    $('#newFaculty').hide()
    $('#alertMessage').hide()
    if (document.getElementById('idToEdit').innerHTML == id) {
        $('#editFaculty').toggle()
    } else {
        $('#editFaculty').show()
    }
    document.getElementById('editName').value = name
    document.getElementById('editEmail').value = email
    document.getElementById('editRole').value = role
    $('#idToEdit').html(id)
}

$(document).ready(function () {
    $('#addForm').submit(function (event) {
        $.ajax({
            type: 'POST',
            url: '/course_sched/faculty_manager/add/',
            csrfmiddlewaretoken: '{{ csrf_token }}',
            data: $('#addForm').serialize(),
            dataType: 'json',
            success: function (data) {
                if (data.isEmailTaken) {
                    $('#alertMessage').html('A user with that email already exists!')
                } else {
                    $('#alertMessage').html('Successfully added user!')
                    document.getElementById("addForm").reset();
                }
                $('#alertMessage').show()
                $('#facultyTable').load(document.URL + ' #facultyTable')
                $('#newFaculty').hide()
                $('#editFaculty').hide()
            },
        });
        return false;
    });

    $('#editForm').submit(function (event) {
        $.ajax({
            type: 'POST',
            url: '/course_sched/faculty_manager/edit/',
            csrfmiddlewaretoken: '{{ csrf_token }}',
            data: $('#editForm').serialize() + '&id=' + document.getElementById('idToEdit').innerHTML,
            dataType: 'json',
            success: function (data) {
                if (data.isEmailTaken) {
                    $('#alertMessage').html('A user with that email already exists!')
                } else {
                    $('#alertMessage').html('Successfully edited user!')
                    document.getElementById("editForm").reset();
                }
                $('#alertMessage').show()
                $('#facultyTable').load(document.URL + ' #facultyTable')
                $('#newFaculty').hide()
                $('#editFaculty').hide()
            },
        });
        return false;
    });
});

$(document).on("click", ".deleteForm", function (event) {
    $.ajax({
        type: 'POST',
        url: '/course_sched/faculty_manager/delete/',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        data: 'id=' + document.getElementById('idToEdit').innerHTML,
        dataType: 'json',
        success: function (data) {
            if (data.userExists) {
                $('#alertMessage').html('User sucessfully deleted!')
                document.getElementById("editForm").reset();
            } else {
                $('#alertMessage').html('Error: Could not delete user!')
            }
            $('#alertMessage').show()
            $('#facultyTable').load(document.URL + ' #facultyTable')
            $('#newFaculty').hide()
            $('#editFaculty').hide()
        },
    });
    return false;
});