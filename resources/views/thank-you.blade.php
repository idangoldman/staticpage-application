@extends('layouts.master')
@section('title', 'Thank you from StaticPages! =]')

@section('content')
    <article class="article">
        <h1 class="title">
            Thank You.
        </h1>

        <h2 class="sub-title">
            We promise to update you with the product release email.
        </h2>
    </article>
@endsection

@push('footer')
    @include('3rd-party.google-analytics', [ 'ga_id' => $google_analytics_id ])
@endpush