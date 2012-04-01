$(document).ready(function() {
    oldhtml = null;
    entries = null;
      $('#page a img').not('.nowrap').wrap('<div class="divImg">');
      $('#page img').not('#page a img').not('.nowrap').wrap('<div class="divImg"><a href="#" onclick="openImage(this); return false;">');

      entries = null;
      oldhtml = null;
      function htmlEscape(str) {
        return str.replace(/&/g,'&amp;').
            replace(/>/g,'&gt;').
            replace(/</g,'&lt;').
            replace(/"/g,'&quot;');
      }
      function prettyDate(d) {
        var m_names = new Array("December", "January", "February", "March",
          "April", "May", "June", "July", "August", "September",
          "October", "November");
        var curr_date = d.getDate();
        var sup = "";
        if (curr_date == 1 || curr_date == 21 || curr_date ==31) {
           sup = "st";
        }
        else if (curr_date == 2 || curr_date == 22) {
           sup = "nd";
        }
        else if (curr_date == 3 || curr_date == 23) {
           sup = "rd";
        }
        else {
           sup = "th";
        }

        var curr_month = d.getMonth();
        var curr_year = d.getFullYear();

        return m_names[curr_month] + " " + curr_date + "<SUP>" + sup + "</SUP> "+ curr_year;
      }
      // from http://stackoverflow.com/questions/2731579/convert-an-xml-schema-date-string-to-a-javascript-date
      var xmlDateToJavascriptDate = function(xmlDate) {
  var re = /^([0-9]{4,})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?(Z|([+-])([0-9]{2}):([0-9]{2}))?$/;
  var match = xmlDate.match(re);
  if (!match)
    return null;

  var all = match[0];
  var year = match[1];  var month = match[2];  var day = match[3];
  var hour = match[4];  var minute = match[5]; var second = match[6];
  var milli = match[7];
  var z_or_offset = match[8];  var offset_sign = match[9];
  var offset_hour = match[10]; var offset_minute = match[11];

  if (offset_sign) { // ended with +xx:xx or -xx:xx as opposed to Z or nothing
    var direction = (offset_sign == "+" ? 1 : -1);
    hour =   parseInt(hour)   + parseInt(offset_hour)   * direction;
    minute = parseInt(minute) + parseInt(offset_minute) * direction;
  }
  var utcDate = Date.UTC(year, month, day, hour, minute, second, (milli || 0));
  return new Date(utcDate);
}

      function findEntries(q) {
        var matches = [];
        var rq = new RegExp(q, 'im');
        for (var i = 0; i < entries.length; i++) {
          var entry = entries[i];
          var title = $(entry.getElementsByTagName('title')[0]).text();
          var link = $(entry.getElementsByTagName('link')[0]).attr('href');
          var content = $(entry.getElementsByTagName('content')[0]).text();
          if (rq.test(title) || rq.test(link) || rq.test(content)) {
            var updated = prettyDate(xmlDateToJavascriptDate($(entry.getElementsByTagName('updated')[0]).text()));
            matches.push({'title':title, 'link':link, 'date':updated});
          }
        }
        var html = '<h3 style="text-align:center; margin-bottom:40px;"><a href="#" onclick="window.location.hash=\'\'; return false;"><img style="height:8px; margin:3px 3px;" src="/images/closelabel.png" /></a> Search Results for "'+htmlEscape(q)+'"</h3><div id="results">';
        for (var i = 0; i < matches.length; i++) {
          var match = matches[i];
          html += '<div class="posting" style="margin: 0; padding: 0;"><div class="postheader"><h1 class="subject"><a href="'+match.link+'">'+htmlEscape(match.title);
          html += '</a></h1><span class="date">'+match.date+'</span></div><div style="clear:both;"></div></div>';
        }
        html += '</div>';
        $('#blogbody').html(html);
      }

      $('#search_form').submit(function(e) {
        var query = $('#query').val();
        window.location.hash = 'search='+escape(query.replace(/\s/g, '+'));
        e.preventDefault();
      });

      $(window).bind('hashchange', function(e) {
          var query = $.param.fragment();
          if (/[#]*search=(.*)/.test(query)) {
      query = $.param.fragment().replace('+', ' ').replace('search=', '');
      $('#query').val(query);
       if (query) {
        if (oldhtml == null) {
          oldhtml = $('body').html();
        }
        $('body').html('<div id="loader"></div>');
              $('footer').hide();
              $('#query').blur().attr('disabled', true);
              if (entries == null) {
                $.ajax({url:'/atom/full/index.xml?r='+(Math.random()*99999999999), dataType:'xml', success: function(data) {
                  entries = data.getElementsByTagName('entry');
                  findEntries(query);
                } });
              } else {
                findEntries(query);
              }
              $('#query').blur().attr('disabled', false);
      }
          } else {
              if (oldhtml == null) {
                  oldhtml = $('body').html();
              }
              $('body').html(oldhtml);
              $('footer').show();
              $('#query').blur();
              oldhtml = null;
          }
});

$(window).trigger( 'hashchange' );
  });
  function openImage(link) {
      document.location = $("> img", $(link)).attr('src');
  }