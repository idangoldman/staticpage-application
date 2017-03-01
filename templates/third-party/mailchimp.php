<?php

define('API_KEY', '{{ api_key }}');
define('LIST_ID', '{{ list_id }}');
define('USERNAME', '{{ username }}');
define('SUCCESSFUL_SUBMISSION', '{{ successful_submission }}');
define('REDIRECT_URL', '{{ redirect_url }}');
define('MESSAGE', '{{ message }}');

$to_print_message = false;


function generate_csrf_token() {
    if ( ! isset( $_SESSION['csrf_token'] ) ) {
        $_SESSION['csrf_token'] = base64_encode( openssl_random_pseudo_bytes( 32 ) );
    }
}

function is_valid_csrf_token() {
    return isset( $_POST['csrf_token'] ) &&
        $_POST['csrf_token'] === $_SESSION['csrf_token'];
}

function csrf_token() {
    echo $_SESSION['csrf_token'];
}

function hide_form() {
    global $to_print_message;

    if ( $to_print_message ) {
        echo 'display: none;';
    }
}

function print_message() {
    global $to_print_message;

    if ( $to_print_message ) {
        echo '<h2 class="message">' . MESSAGE . '</h2>';
    }
}

function subscribe( $email ) {
	$auth = base64_encode( USERNAME . ':' . API_KEY );
    $url = 'https://' . explode( '-', API_KEY )[ 1 ] . '.api.mailchimp.com/3.0/lists/' . LIST_ID . '/members/';
	$json_data = json_encode(array(
		'email_address' => $email,
		'status' => 'subscribed'
	));
    $headers = array(
        'Content-Type: application/json',
		'Authorization: Basic ' . $auth
    );

	$curl = curl_init();
	curl_setopt( $curl, CURLOPT_URL, $url );
	curl_setopt( $curl, CURLOPT_HTTPHEADER, $headers );
	curl_setopt( $curl, CURLOPT_USERAGENT, 'PHP-MCAPI/3.0' );
	curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $curl, CURLOPT_TIMEOUT, 10 );
	curl_setopt( $curl, CURLOPT_POST, true  );
	curl_setopt( $curl, CURLOPT_SSL_VERIFYPEER, false );
	curl_setopt( $curl, CURLOPT_POSTFIELDS, $json_data );

    try {
        $result = curl_exec( $curl );
        $json = json_decode( $result, true );
    } catch ( Exception $e ) {
        return false;
    }

    if ( $json['status'] === 'subscribed' ||
         $json['title'] === 'Member Exists' ) {
        return true;
    } else {
        return false;
    }

    return $valid;
};


session_start();
generate_csrf_token();

if ( $_SERVER['REQUEST_METHOD'] === 'POST' && is_valid_csrf_token() ) {
    if ( filter_var( $_POST['email'], FILTER_VALIDATE_EMAIL ) &&
         subscribe( $_POST['email'] ) ) {

        switch( SUCCESSFUL_SUBMISSION ) {
            case 'successful-submission-message':
                if ( ! empty( MESSAGE ) ) {
                    $to_print_message = true;
                }
                break;
            case 'successful-submission-redirect':
                if ( ! empty( REDIRECT_URL ) ) {
                    header( 'Location: ' . REDIRECT_URL, true );
                    exit();
                }
                break;
        }
    }
}

?>
