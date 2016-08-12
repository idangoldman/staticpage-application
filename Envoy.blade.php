@servers( [ 'web' => 'idan@frank.blah.co.il' ] )

@setup
    $domain = "staticpages.info";
    $release = "release_" . date("YmdHis");
    $repository = "git@github.com:idanm/static-pages.git";

    $base_folder = "/var/www/" . $domain;
    $current = $base_folder . "/current";
    $release_folder = $base_folder . "/releases";
@endsetup

@macro('deploy')
    fetch_repository
    compile_backend
    compile_frontend
    update_symlinks
@endmacro

@task('fetch_repository', ['on' => 'web'])
    [ -d {{ $release_folder }} ] || mkdir {{ $release_folder }};
    cd {{ $release_folder }};
    git clone -b master {{ $repository }} {{ $release }};
@endtask

@task('compile_backend', ['on' => 'web'])
    cd {{ $release_folder }}/{{ $release }};
    composer install --prefer-dist;
    cp .env.example .env;
    php artisan key:generate;
@endtask

@task('compile_frontend', ['on' => 'web'])
    cd {{ $release_folder }}/{{ $release }};
    npm install;
    {{-- npm install -g bower gulp; // install manually --}}
    bower install;
    gulp;
@endtask

@task('update_symlinks', ['on' => 'web'])
    ln -nfs {{ $release_folder }}/{{ $release }} {{ $current }};
@endtask