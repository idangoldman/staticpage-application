@extends('layouts.master')
@section('title', '403 =[')

@section('content')
    <article class="article">
        <h1 class="title">
            403
        </h1>

        <h2 class="sub-title">
            Ooops you got us, access restricted.
        </h2>

        <p class="description">
            If you want, you can always try and ask us to give you an <a href="{{ url('/404') }}">access key</a> to this informantion.
        </p>
    </article>
@endsection