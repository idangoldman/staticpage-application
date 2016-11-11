@extends('layouts.master')

@section('content')
    <article class="article">
        <h1 class="title">
            Thank You.
        </h1>

        <h2 class="sub-title">
            We promise to update you with the product release email.
        </h2>

        @include( '3rd-party.addthis', [ 'addthis_pubid' => $addthis_pubid ] )

    </article>
@endsection

@push('footer')
    @include( '3rd-party.google-analytics', [ 'ga_id' => $google_analytics_id ] )
@endpush