/*------------------------포매팅함수------------------------*/
function format() { var args = Array.prototype.slice.call (arguments, 1); 
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) { return args[index]; }); }


/*------------------------전체 초기화------------------------*/
$('.question').hide();

$('h3').eq(1).hide(); //두번째 h3 선택질문 설명 문구 가리기

$('input[type=submit], .submit').hide();

$('.previous').css('opacity', '0');

const q_num = 22; //질문 개수

//range 설명 초기화 - 첫번째는 
const range_list = $("input[type=range]");

$.each(range_list, function(index, item){
    let rg_children = $(this).parent().prev().children();
    rg_children.css("opacity", "0");
    if(index == 0)
    rg_children.eq(3).css("opacity", "1");
    else{
    $(this).val(0);
    rg_children.eq(0).css("opacity", "1");
    }

});


/*------------------------다음/이전 기능------------------------*/
//1. 반려동물 부분... user에 따라서 비활성화 혹은 아예 안보이게 => 완료
/*--------------------------------------------------------*/

//////////////////변수선언+초기화//////////////////
let answer_cnt = 0;
//첫번째 질문 보이게
const $question_list = $('.question');
$question_list.eq(answer_cnt).show();

//////////////////함수정의//////////////////
function nextFade(q_cur){
    //연속으로 누를 시이전 리스트에 실행중인 fadeOut은 모두 종료
    let $q_slice = $question_list.slice(0, q_cur);
    $q_slice.stop(true,true);
    //천천히 누를땐 순서대로 fadeout,in
    $question_list.eq(q_cur-1).fadeOut(500);
    $question_list.eq(q_cur).delay(600).fadeIn(500);
}

function previousFade(q_cur){
    //연속으로 누를 시이전 리스트에 실행중인 fadeOut은 모두 종료
    let $q_slice = $question_list.slice(q_cur+1, q_num+1);
    $q_slice.stop(true,true);
    //천천히 누를땐 순서대로 fadeout,in
    $question_list.eq(q_cur+1).fadeOut(500);
    $question_list.eq(q_cur).delay(600).fadeIn(500);
}

//질문을 스크롤형으로 변환하는 함수
function setScrollType(dormitoryOpt){
    //다음·이전 버튼 없애기
    $(".next, .previous").animate({
        'opacity': '0'
    });
    $(".container").css('height', 'auto');
    //모든 문항 보이게
    $.each($question_list, function(index, item){
        $(this).fadeIn(500);
    })
    //기숙사생이면 자취전용 항목 감추기
    if(dormitoryOpt == true){
        $(".not-dormitory").hide();
    }
    else{
        $(".dormitory-only").hide();
    }
    //선택문항 설명 문구 보이게
    $('h3').eq(1).show(); 
    //선택문항으로 스크롤하기
    let scrollPosition = $(".question.share").offset().top;
    $("html, body").animate({
        scrollTop: scrollPosition
    }, 500).delay(1000);
    $question_list.css("margin-bottom", "40px");
    //제출버튼 보이게
    $('input[type=submit], .submit').show();
}

//////////////////이벤트리스너//////////////////
//이전or다음 버튼을 연속 클릭 했을 시 애니메이션 빠르게 적용하기위해 nextClickCnt사용
//이렇게 하지말고...next누를 때마다 이전 요소를 전부 fadeOut시키고 마지막 요소를 fadeIn 시키는 방법은?
$('.next').on('click', function(){
    //큰 if는 유효성 검사.
    // if (vaildation() == true){
        if(answer_cnt == 0) {
            $('.previous').animate({
                opacity: '1'
            }, 200);
        }

        if(answer_cnt==1 && $('input[name=room-type]:checked').val()=='1') //자취생이면
            answer_cnt++;
        else if(answer_cnt==12 && $('input[name=room-type]:checked').val()=='0'){//긱사생이면 마지막질문(animal) 그냥 넘겨버리기
            answer_cnt++;
            setScrollType(true);
            reloadProgressBar(answer_cnt+1);
            return;
        }
        else if(answer_cnt == 13){
            setScrollType(false);
        }
        answer_cnt += 1;
        nextFade(answer_cnt);
        reloadProgressBar(answer_cnt);
    // }
})

$('.previous').on('click', function(){
    if(answer_cnt == 1) {
        $(this).animate({
            'opacity': '0',
        }, 200);
    }
    if(answer_cnt != 0) {
        answer_cnt--;
        previousFade(answer_cnt);
    }
    setTimeout(function(){
        reloadProgressBar(answer_cnt);
    }, 20)
})

//css애니메이션으로 바꾸기.
$('.next, .previous').on('mouseover', function(){
    $(this).animate({
        'font-size' : '20px'
        // color: '#000'
    }, 50, "swing");
})

$('.next, .previous').on('mouseleave', function(){
    $(this).animate({
        'font-size' : '15px'
        // color: '#fff'
    }, 100, "swing");
})

/*------------------------진행바 구현------------------------*/
//1. 필수 문항/ 선택 문항 구분 필요
/*--------------------------------------------------------*/

//////////////////변수선언+초기화//////////////////
$('.front-bar > .text').css('opacity', '0')
const pb_width_block = 100 / 13;

//////////////////함수정의//////////////////
function changeFrontBarWidth(width){
    $('.front-bar').stop(true, true);
    $('.front-bar').animate( {
        width: format('{0}%', width)
      }, 400, 'swing' );
}

//질문 수에 따라 진행바 길이 조절
function reloadProgressBar(pb_cnt){

    //흰색 바 조정해주는 함수
    changeFrontBarWidth(pb_width_block * answer_cnt);

    //진행상황 글자가 넘쳐서 front-bar가 어느정도 길어지면 나오게
    if(answer_cnt + 1 >= 3){
        $('.front-bar > .text').animate( {
            opacity: "1"
        }, 600, "swing");
    } 
    //진행바가 다시 작아지면 텍스트 감추기
    if(answer_cnt + 1 < 3){
        $('.front-bar > .text').animate( {
            opacity: "0"
        }, 600, "swing");
    }
}

/*------------------------range bar 설명 구현------------------------*/

//////////////////이벤트리스너//////////////////
$("input[type=range]").on('input', function(){
    var index = $("input[type=range]").index(this);
    var rg_cur = $(this).val();
    var rg_children = $(".range-detail").eq(index).children();
    rg_children.css("opacity", "0");
    rg_children.eq(rg_cur).css("opacity", "1");
});

/*------------------------유효성 검사------------------------*/
//값을 선택해야 넘어가도록
//여기선 anw = answer

//////////////////변수선언+초기화//////////////////
let $anw_arr = $(".answer");

//////////////////함수정의//////////////////
function vaildation(){ 
    var rt = true;
    var anw_cur = $anw_arr.eq(answer_cnt);
    var anw_cur_type = anw_cur.children().eq(0).attr("type");
    var anw_cur_name = anw_cur.children().eq(0).attr("name");
    //라디오 버튼 값이 null이면 false
    if(anw_cur_type == "radio"){
        if($('input[name="'+anw_cur_name+'"]:checked').val() == null) rt = false;
    }
    //checkbox랑 text가 같이 있는 경우 하나도 체크되어 있지 않고 텍스트도 비어 있으면 false
    else if(anw_cur_type == "checkbox"){
        var anw_checkbox_arr = anw_cur.children("input[type=checkbox]");
        var checkbox_cnt = 0;
        $.each(anw_checkbox_arr, function(index, item){
            if(item.checked) checkbox_cnt++;
        })
        if (anw_cur.children("input[type=text]").val().length != 0) checkbox_cnt++;
        if(checkbox_cnt == 0) rt = false;
    }
    //text or number 의 길이가 0이면 false
    else if(anw_cur_type == "text" || anw_cur_type == "number"){
        if (anw_cur.children("input[type=text], input[type=number]").val().length == 0) rt = false;
    }
    //time값의 길이가 0이면 false
    else if(anw_cur_type == "time"){
        var time_list = anw_cur.children("input[type=time]");
        $.each(time_list, function(index, item){
            if($(this).val().length == 0) rt = false;
        })
    }
    return rt;
}

