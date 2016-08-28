<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
    return redirect('/welcome');
});

Route::get('/welcome', function () {
    return view('welcome');
});

Route::get('/home', function () {
    return view('home');
});

Route::post('/subscribe', function () {
    $email = Input::get('email');

    return redirect('/thank-you');
});

Route::get('/thank-you', function () {
    return view('thank-you');
});

Route::get('/side-kick', function () {
    $svg = new DOMDocument();
    $svg->load( public_path('svg/sprite.svg') );
    $svg->documentElement->setAttribute( 'class', 'svg-icons' );
    $inline_svg = $svg->saveXML( $svg->documentElement );

    $viewData = array(
        'svg_icons' => $inline_svg,
        'initial_data' => json_encode( array(
            'pageInfo' => array(
                'title' => 'Page Info',
                'fields' => array(
                    array(
                        'id' => 'name',
                        'placeholder' => 'Static page example',
                        'title' => 'name',
                        'type' => 'text',
                        'value' => '',
                        'message' => ''
                    ),
                    array(
                        'id' => 'type',
                        'title' => 'type',
                        'type' => 'select',
                        'options' => array(
                            array( 'key' => 'coming-soon', 'value' => 'Coming Soon' ),
                            array( 'key' => 'thank-you', 'value' => 'Thank You' )
                        ),
                        'value' => '',
                        'message' => ''
                    ),
                    array(
                        'id' => 'logo',
                        'title' => 'logo',
                        'type' => 'image-upload',
                        'value' => '',
                        'fileName' => '',
                        'message' => 'Upload gif, jpg, and png only, up to 1MB.'
                    )
                )
            )
        ) )
    );

    return view( 'layouts.side-kick', $viewData );
});

Route::auth();
