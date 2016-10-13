@extends('layouts.master')
@section('title', '404 =[')

@section('content')
    <article class="article">
        <h1 class="title">
            404
        </h1>

        <h2 class="sub-title">
            Ooops you got us, we don't have<br/>
            the page you are asking for.
        </h2>

        <p class="description">
            If you want, you can <a href="{{ url('/register') }}">register</a> this page and create it yourself.
        </p>
    </article>
@endsection