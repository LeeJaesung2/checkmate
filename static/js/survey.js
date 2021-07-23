/*------------------------포매팅함수------------------------*/
function format() { var args = Array.prototype.slice.call (arguments, 1); 
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) { return args[index]; }); }


/*------------------------초기화------------------------*/
$('.question').hide();

$('h3').eq(1).hide(); //두번째 h3 선택질문 설명 문구 가리기

// console.log($('.container').eq(2));

/*------------------------다음/이전 기능------------------------*/
answer_cnt = 0;
$question_list = $('.question')
$question_list.eq(answer_cnt).show();

$('.next').on('click', function(){
    if(answer_cnt != 19){
        $question_list.eq(answer_cnt).fadeOut(600);
        answer_cnt += 1;
        // setTimeout(function(){$question_list.eq(answer_cnt).fadeTo(600, 1);}, 600); //이러케해두댐
        $question_list.eq(answer_cnt).delay(700).fadeIn(600);
    }
    reloadProgressBar();
})

$('.next, .previous').on('mouseover', function(){
    this.animate()
})

$('.previous').on('click', function(){
    if(answer_cnt != 0) {
        $question_list.eq(answer_cnt).fadeOut(600);
        answer_cnt -= 1;
        $question_list.eq(answer_cnt).delay(700).fadeIn(600);
    }
    reloadProgressBar();
})

/*------------------------진행바 구현------------------------*/
//1. 필수 문항/ 선택 문항 구분 필요
/*--------------------------------------------------------*/
function reloadProgressBar(){
    $('.front-bar').animate( {
        width: format('{0}%', answer_cnt*5)
      }, 400, 'swing' );
    
}