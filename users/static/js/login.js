SUCCESS = 1
USER_EXISTS = -1
INVALID_USERNAME = -2
INVALID_PASSWORD = -3
INVALID_EMAIL = -4

MAX_NAME_LENGTH = 30

function json_request(page, dict, success, failure) {
    $.ajax({
        type: 'POST',
        url: page,
        data: JSON.stringify(dict),
        contentType: "application/json",
        dataType: "json",
        success: success,
        error: failure
    });
}

function update(data) {
    switch(data.errCode) {
        case SUCCESS:
            $.cookie("username", username);
            // go to newsfeed for user
            window.location.replace("/user/notifications");
            break;
        case USER_EXISTS:
            $('#errorMessage').html('This username is already taken. Please try again.');
            break;
        case INVALID_USERNAME:
            $('#errorMessage').html('Username cannot be more than 30 characters long. Please try again.');
            break;
        case INVALID_PASSWORD:
            $('#errorMessage').html('Password must be non-empty. Please try again.');
            break;
        case INVALID_EMAIL:
            $('#errorMessage').html('Please use a valid e-mail address.');
            break;
    }    
}

$(document).ready(function(){
    // if they're already logged in, go to their notifications page
    if($.cookie("username")) {
        window.location.replace("/user/notifications");
    }

    $('#loginButton').click(function() {
        username = $('#username').val();
        password = $('#password').val();
        json_request("/user/login", {user: user, password: password}, update);
        return false;
    });

    $('#createAccountButton').click(function() {
        firstname = $('#firstname').val();
        lastname = $('#lastname').val();
        email = $('#email').val();
        username = $('#username2').val();
        password = $('#password').val();
        json_request("/user/add", {firstname: firstname, lastname: lastname, email: email, username: username, password: password, email: email}, update);
        return false;
    });

// clears form data when modals are closed
    $('#closeButton').click(function() {
        $('#username').val("");
        $('#password').val("");
    });

    $('#closeButton2').click(function() {
        $('#firstname').val("");
        $('#lastname').val("");
        $('#email').val("");
        $('#username2').val("");
        $('#password').val("");
    });

// frontend form checking
    $("#firstname").blur(function() {
    var x = $('#firstname').val();
    if (x.length > MAX_NAME_LENGTH) {
        $("#errorMessage").html("First name cannot be more than 30 characters.");
        $('#errorMessage').show();
    } else if (x.length == 0) {
        $("#errorMessage").html("First name cannot be left blank.");
        $('#errorMessage').show();
    } else {
        $('#errorMessage').hide();
    }
  });

    $("#lastname").blur(function() {
    var x = $('#lastname').val();
    if (x.length > MAX_NAME_LENGTH) {
        $("#errorMessage").html("Last name cannot be more than 30 characters.");
        $('#errorMessage').show();
    } else if (x.length == 0) {
        $("#errorMessage").html("Last name cannot be left blank.");
        $('#errorMessage').show();
    } else {
        $('#errorMessage').hide();
    }
  });

    $("#username2").blur(function() {
    var x = $('#username2').val();
    if (x.length > MAX_NAME_LENGTH) {
        $("#errorMessage").html("Username cannot be more than 30 characters.");
        $('#errorMessage').show();
    } else if (x.length == 0) {
        $("#errorMessage").html("Username cannot be left blank.");
        $('#errorMessage').show();
    } else {
        $('#errorMessage').hide();
    }
  });

    $("#email").blur(function() {
    var x = $('#email').val();
    if (x.indexOf('@') === -1) {
        $("#errorMessage").html("Please enter a valid e-mail address.");
        $('#errorMessage').show();
    } else {
        $('#errorMessage').hide();
    }
  });

}); //end of $(document).ready(function()
