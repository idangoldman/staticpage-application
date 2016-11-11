@extends('layouts.master')

@section('content')
    <article class="article">
        <h1 class="title">
            StaticPages
        </h1>

        <h2 class="sub-title">
            Working on creating a "Coming Soon Page" shop. <br />
            We know ironic.
        </h2>

        <p class="description">
            We are a team of keyboard kids who turned out to be good people and professionals located around the world trying to create the best product we can.

            @if ( ! $has_subscribed )
                Stay tuned by subscribing to our mailing list and we promise to update you with the product release.
            @endif
        </p>

        @if ( $has_subscribed )
            @include( '3rd-party.addthis', [ 'addthis_pubid' => $addthis_pubid ] )
        @endif
    </article>

    @if ( ! $has_subscribed )
        <form action="newsletter" method="post" class="newsletter">
            {{ csrf_field() }}
            <input class="email" name="email" placeholder="email@domain.com" />
            <button type="submit" class="submit">Keep me posted!</button>
        </form>
    @endif
@endsection

@push('footer')
    @include('3rd-party.google-analytics', [ 'ga_id' => $google_analytics_id ])
    <script src="{{ URL::asset('js/app.js') }}"></script>
@endpush