// base component
import baseBox from 'side-kick/components/base-box';

// child components
import selectFieldComponent from 'side-kick/components/select-field';
import urlFieldComponent from 'side-kick/components/url-field';


const socialLinksFeature = baseBox.mixin(function box() {
  this.attributes({
    iconStyleField: '.social_links_icon_style',
    facebookLinkField: '.social_links_facebook_link',
    instagramLinkField: '.social_links_instagram_link',
    linkedinLinkField: '.social_links_linkedin_link',
    twitterLinkField: '.social_links_twitter_link',
    youtubeLinkField: '.social_links_youtube_link',
  });

  this.after('initialize', function initialize() {
    // Icon Style
    this.attachChild(selectFieldComponent, this.select('iconStyleField'), {
      fieldName: 'social_links_icon_style',
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('facebookLinkField'), {
      fieldName: 'social_links_facebook_link',
      toValidate: ['url'],
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('instagramLinkField'), {
      fieldName: 'social_links_instagram_link',
      toValidate: ['url'],
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('linkedinLinkField'), {
      fieldName: 'social_links_linkedin_link',
      toValidate: ['url'],
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('twitterLinkField'), {
      fieldName: 'social_links_twitter_link',
      toValidate: ['url'],
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('youtubeLinkField'), {
      fieldName: 'social_links_youtube_link',
      toValidate: ['url'],
    });
  });
});

socialLinksFeature.attachTo('.feature.social-links');
