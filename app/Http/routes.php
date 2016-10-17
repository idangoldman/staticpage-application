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
use Spatie\Newsletter\NewsletterFacade as Newsletter;
use Illuminate\Http\Request;

Route::auth();

Route::get('/', function () {
    return redirect('/welcome');
});

Route::get('/welcome', function ( Request $request ) {
    $viewData = array(
        'has_subscribed' => $request->cookie('subscribed'),
        'google_analytics_id' => config('app.google_analytics_id'),
        'addthis_pubid' => config('app.addthis_pubid'),
    );

    return view( 'welcome', $viewData );
});

Route::get('/home', function ( Request $request ) {
    $viewData = array(
        'has_subscribed' => $request->cookie('subscribed'),
        'google_analytics_id' => config('app.google_analytics_id'),
        'addthis_pubid' => config('app.addthis_pubid'),
    );

    return view( 'home', $viewData );
})->middleware('auth');

Route::post('/newsletter', function () {
    $email = Input::get('email');
    $subscribed = 0;
    $five_days = ( 60 * 60 * 24 * 5 );

    if ( filter_var( $email, FILTER_VALIDATE_EMAIL ) ) {
        Newsletter::subscribe( $email );
        $subscribed = 1;
    }

    return redirect('/thank-you')->withCookie( cookie( 'subscribed', $subscribed, $five_days ) );
});

Route::get('/thank-you', function () {
    $viewData = array(
        'google_analytics_id' => config('app.google_analytics_id'),
        'addthis_pubid' => config('app.addthis_pubid'),
    );

    return view( 'thank-you', $viewData );
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
})->middleware('auth');
