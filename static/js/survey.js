/*------------------------포매팅함수------------------------*/
function format() { var args = Array.prototype.slice.call (arguments, 1); 
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) { return args[index]; }); }


/*------------------------초기화------------------------*/
$('.question').hide();

$('h3').eq(1).hide(); //두번째 h3 선택질문 설명 문구 가리기

$('input[type=submit]').hide();


/*------------------------다음/이전 기능------------------------*/
var answer_cnt = 1;
var $question_list = $('.question');
var nextClickCnt = 1;   

$question_list.eq(answer_cnt).show();
//이전or다음 버튼을 연속 클릭 했을 시 애니메이션 빠르게 적용하기위해 nextClickCnt사용
$('.next').on('click', function(){
    if(answer_cnt != 22){
        setTimeout(function(){
            $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
            answer_cnt += 1;
            nextClickCnt += 10;
        }, 0);
        setTimeout(function(){
            nextClickCnt -= 10;
            $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
        }, 700);

        // $question_list.eq(answer_cnt).fadeOut(600);
        // answer_cnt += 1;
        // $question_list.eq(answer_cnt).delay(700).fadeIn(600);
    }
    reloadProgressBar();
})

$('.next, .previous').on('mouseover', function(){
    this.animate()
})

$('.previous').on('click', function(){
    if(answer_cnt != 0) {
        setTimeout(function(){
            $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
            answer_cnt -= 1;
            nextClickCnt += 10;
        }, 0);
        setTimeout(function(){
            nextClickCnt -= 10;
            $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
        }, 700);
        // $question_list.eq(answer_cnt).fadeOut(600);
        // answer_cnt -= 1;
        // $question_list.eq(answer_cnt).delay(700).fadeIn(600);
    }
    reloadProgressBar();
})

/*------------------------진행바 구현------------------------*/
//1. 필수 문항/ 선택 문항 구분 필요
/*--------------------------------------------------------*/

$('.front-bar > .text').css('opacity', '0')
function reloadProgressBar(){
    //질문 수에 따라 진행바 길이 조절
    $('.front-bar').animate( {
        width: format('{0}%', answer_cnt*5)
      }, 400/nextClickCnt, 'swing' );
    console.log("질문 현황", answer_cnt);
    //진행상황 글자가 넘쳐서 front-bar가 어느정도 길어지면 나오게
    if(answer_cnt >= 3){
        console.log("실행");
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "1"
            }, 600, "swing");
        }, 10);
    }
    if(answer_cnt < 3){
        console.log("실행");
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "0"
            }, 600, "swing");
        }, 10);
    }
}

/*------------------------버튼 hover 구현------------------------*/
$("input[type=radio]+label").on("mouseover", function(){
    console.log("실행");
   
})