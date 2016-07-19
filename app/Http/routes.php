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

    return view('layouts.side-kick', [ 'svg_icons' => $inline_svg ]);
});