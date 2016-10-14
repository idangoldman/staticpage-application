<!DOCTYPE html>
<html><head>

    <meta charset="UTF-8" />
    <title>@yield('title')</title>
    <link href="{{ URL::asset('css/app.css') }}" rel="stylesheet" type="text/css" />
    {{-- <meta name="csrf-token" content="{{ csrf_token() }}" /> --}}

    @stack('header')

</head><body>

    <section class="static-page background">
        @yield('content')
    </section>

    @stack('footer')

</body></html>