import $ from 'jquery';
import { component, utils } from 'flightjs';

const PAGE_UPDATE_URL = window.page_update_url;
const SITE_DOWNLOAD_URL = window.site_download_url;
const PAGE_MANAGE_URL = window.page_manage_url;

const setCsrfHeader = function setCsrfHeader() {
  // code from: https://flask-wtf.readthedocs.io/en/stable/csrf.html
  const csrftoken = $('meta[name=csrf-token]').attr('content');

  $.ajaxSetup({
    beforeSend(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      }
    },
  });
};

const apiCalls = component(function apiCalls() {
  this.siteDownload = function siteDownload() {
    $.ajax({
      url: SITE_DOWNLOAD_URL,
      type: 'GET',
      success: function requestSuccess(response) {
        this.trigger(document, 'siteDownload_success', response.data);
      }.bind(this),
      error: function requestError(jqXHR) {
        this.trigger(document, 'siteDownload_error', jqXHR.responseJSON);
      }.bind(this),
    });
  };

  this.updateField = function updateField(event, field) {
    const eventName = `${event.type}_${field.name}`;

    utils.throttle($.ajax(this.updateFieldRequestConfig(eventName, field)));
  };

  this.updateFieldRequestConfig = function updateFieldRequestConfig(eventName, field) {
    let config = {
      url: PAGE_UPDATE_URL,
      type: 'POST',
      success: function requestSuccess(response) {
        this.trigger(document, `${eventName}_success`, response.data);
      }.bind(this),
      error: function requestError(jqXHR) {
        this.trigger(document, `${eventName}_error`, jqXHR.responseJSON);
      }.bind(this),
    };

    let fileConfig = {};
    let jsonConfig = {};

    if (field.base64) {
      const requestData = new FormData();
      requestData.append(field.name, field.value);

      fileConfig = {
        data: requestData,
        dataType: 'json',
        processData: false,
        contentType: false,
      };

      config = utils.merge({}, config, fileConfig);
    } else {
      jsonConfig = {
        data: JSON.stringify(field),
        contentType: 'application/json',
      };

      config = utils.merge({}, jsonConfig, config);
    }

    return config;
  };

  this.pageManage = function pageManage(event, {
    action = 'GET',
    id = null,
    name = undefined,
    template = undefined
  }) {
    const url = PAGE_MANAGE_URL + (id ? `/${id}` : '');
    const data = JSON.stringify({ name, template });

    switch(action) {
      case 'create_page':
        action = 'POST';
        break;
      case 'rename_page':
        action = 'PUT';
        break;
      default:
      case 'delete_page':
        action = 'DELETE';
        break;
    }

    $.ajax({
      url, data,
      type: action,
      contentType: 'application/json',
      success: function requestSuccess(response) {
        this.trigger(document, 'pageManage_success', response.data);
      }.bind(this),
      error: function requestError(jqXHR) {
        this.trigger(document, 'pageManage_error', jqXHR.responseJSON);
      }.bind(this),
    });
  },

  this.after('initialize', function initialize() {
    setCsrfHeader();

    this.on(document, 'updateField', this.updateField);
    this.on(document, 'siteDownload', this.siteDownload);
    this.on(document, 'pageManage', this.pageManage);
  });
});

apiCalls.attachTo(document);
