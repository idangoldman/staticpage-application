<!DOCTYPE html>
<html><head>

    <meta charset="UTF-8" />

    {{-- @include( '3rd-party.social', $meta_data ) --}}

    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {{-- <meta name="theme-color" content="#ff69b4"> --}}
    <link href="{{ URL::asset('css/app.css') }}" rel="stylesheet" type="text/css" />
    {{-- <link rel="apple-touch-icon" href="apple-touch-icon.png"> --}}

    @stack('header')

</head><body>
    {{-- <!--[if lte IE 9]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
    <![endif]--> --}}

    <section class="static-page background">
        @yield('content')
    </section>

    @stack('footer')

</body></html>