<title>{{ $title }}</title>
<meta name="description" content="{{ $description }}"/>
<meta name="robots" content="{{ $robots }}"/>
<link rel="canonical" href="{{ $link }}" />
<link rel="shortlink" href="{{ $shortlink }}">

{{-- Google+ --}}
{{-- <html class="no-js" lang="" itemscope itemtype="http://schema.org/Article">
<link rel="author" href="">
<link rel="publisher" href=""> --}}
<meta itemprop="name" content="{{ $name }}">
<meta itemprop="description" content="{{ $description }}">
<meta itemprop="image" content="{{ $google_image_link }}">

{{-- Facebook --}}
{{-- <meta property="fb:app_id" content=""> --}}
{{-- <meta property="article:author" content=""> --}}
<meta property="og:locale" content="{{ $local }}" />
<meta property="og:type" content="{{ $facebook_type }}" />
<meta property="og:title" content="{{ $title }}" />
<meta property="og:description" content="{{ $description }}" />
<meta property="og:url" content="{{ $link }}" />
<meta property="og:site_name" content="{{ $name }}" />
<meta property="og:image" content="{{ $facebook_image_link }}" />

{{-- Twitter --}}
{{-- <meta name="twitter:creator" content="@individual_account"> --}}
{{-- <meta name="twitter:site" content="@site_account"> --}}
<meta name="twitter:card" content="{{ $twitter_card }}" />
<meta name="twitter:description" content="{{ $description }}" />
<meta name="twitter:title" content="{{ $title }}" />
<meta name="twitter:image" content="{{ $twitter_image_link }}" />