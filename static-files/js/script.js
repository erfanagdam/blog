$(function() {
  $(".faq-list-item").click(function() {
    var $faqContent = $(this).find(".faq-content");
    if ($faqContent.hasClass("open")) {
      $faqContent.removeClass("open");
      $faqContent.slideUp();

      $(this)
        .find("span")
        .html('<svg xmlns="http://www.w3.org/2000/svg" width="18" height="12"><path fill="none" stroke="#5267DF" stroke-width="3" d="M1 1l8 8 8-8"/></svg>');
    } else {
      $faqContent.addClass("open");
      $faqContent.slideDown();

      $(this)
        .find("span")
        .html('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="15"><path fill="#5267DF" fill-rule="evenodd" d="M8 5.379L13.303.075l2.122 2.122L10.12 7.5l5.304 5.303-2.122 2.122L8 9.62l-5.303 5.304-2.122-2.122L5.88 7.5.575 2.197 2.697.075 8 5.38z"/></svg>');
    }
  });
});
