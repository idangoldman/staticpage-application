<!DOCTYPE html>
<html><head>

    <meta charset="UTF-8" />
    <title>It's your friendly side-kick!</title>
    <link href="{{ URL::asset('css/side-kick.css') }}" rel="stylesheet" type="text/css" />
    <meta name="csrf-token" content="{{ csrf_token() }}" />

</head><body>
    {!! $svg_icons !!}

    <section class="side-kick"></section>

    <script> var initialData = {!! $initial_data !!}; </script>
    <script src="{{ URL::asset('js/side-kick.js') }}"></script>

</body></html>
