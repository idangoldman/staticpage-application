@servers( [ 'web' => 'idan@frank.blah.co.il' ] )

@setup
    $domain = "staticpages.info";
    $environment = isset( $env ) ? $env : "testing";

    // $release = "release_" . date("YmdHis");
    $release_current = "release_20160803032313";
    $release = $release_current;

    $repository = "git@github.com:idanm/static-pages.git";

    $base_folder = "/var/www/" . $domain;
    $current = $base_folder . "/home";
    $release_folder = $base_folder . "/releases";
@endsetup

@macro('deploy')
    fetch_repository
    compile_frontend
    {{-- update_permissions --}}
    {{-- update_symlinks --}}
    {{-- compile_backend --}}
@endmacro

@task('fetch_repository', ['on' => 'web'])
    [ -d {{ $release_folder }} ] || mkdir {{ $release_folder }};
    cd {{ $release_folder }};
    git clone -b master {{ $repository }} {{ $release }};
@endtask

@task('compile_backend', ['on' => 'web'])
    cd {{ $release_folder }}/{{ $release }};
    composer install --prefer-dist;
@endtask

@task('compile_frontend', ['on' => 'web'])
    cd {{ $release_folder }}/{{ $release }};
    {{-- npm install; --}}
    {{-- npm install -g bower gulp; // install manually --}}
    {{-- bower install; --}}
    gulp;
@endtask

@task('update_permissions', ['on' => 'web'])
    cd {{ $release_folder }};
    chgrp -R www-data {{ $release }};
    chmod -R ug+rwx {{ $release }};
@endtask

@task('update_symlinks', ['on' => 'web'])
    ln -nfs {{ $release_folder }}/{{ $release }} {{ $current }};
    chgrp -h www-data {{ $current }};
@endtask