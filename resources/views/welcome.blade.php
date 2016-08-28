@extends('layouts.master')
@section('title', 'Welcome to StaticPages.')

@section('content')
    <article class="article">
        <h1 class="title">
            StaticPages
        </h1>

        <h2 class="sub-title">
            <!-- StaticPages brand new way to build landing pages better. -->
            Working on creating a “Coming Soon Page” shop. <br />
            We know ironic.
        </h2>

        <p class="description">
            We are a team of keyboard kids who turned out to be good people and professionals located around the world trying to create the best product we can. Stay tuned by subscribing to our mailing list and we promise to update you with the product release.
        </p>
    </article>

    <form action="subscribe" method="post" class="subscription">
        {{ csrf_field() }}
        <input class="email" name="email" placeholder="email@domain.com" />
        <button type="submit" class="submit">Keep me posted!</button>
    </form>

@endsection
