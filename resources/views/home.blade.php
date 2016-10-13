@extends('welcome')

@section('title', 'Home of StaticPages')

@section('footer')
    <script src="{{ URL::asset('js/app.js') }}"></script>

    <iframe class="iframe-side-kick" src="/side-kick"
        frameborder="0" border="0" cellspacing="0">
    </iframe>
@endsection
