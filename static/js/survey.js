/*------------------------포매팅함수------------------------*/
function format() { var args = Array.prototype.slice.call (arguments, 1); 
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) { return args[index]; }); }


/*------------------------초기화------------------------*/
$('.question').hide();

$('h3').eq(1).hide(); //두번째 h3 선택질문 설명 문구 가리기

$('input[type=submit], .submit').hide();

$('.previous').css('opacity', '0');

let q_num = 22; //질문 개수

//range 설명 초기화
var range_list = $("input[type=range]");

$.each(range_list, function(index, item){
    var rg_children = $(this).parent().prev().children();
    rg_children.css("opacity", "0");
    if(index == 0)
    rg_children.eq(3).css("opacity", "1");
    else{
    $(this).val(0);
    rg_children.eq(0).css("opacity", "1");
    }

});

/*------------------------다음/이전 기능------------------------*/
//1. 반려동물 부분... user에 따라서 비활성화 혹은 아예 안보이게
/*--------------------------------------------------------*/

var answer_cnt = 0;
var $question_list = $('.question');
var nextClickCnt = 1;   

$question_list.eq(answer_cnt).show();
//절대 제 코드를 해석하지 못할겁니다. 이게 바로 코드 난독화...🙄
//재사용성...어쩔거야....
//이전or다음 버튼을 연속 클릭 했을 시 애니메이션 빠르게 적용하기위해 nextClickCnt사용
//이렇게 하지말고...next누를 때마다 이전 요소를 전부 fadeOut시키고 마지막 요소를 fadeIn 시키는 방법은?
$('.next').on('click', function(){
    // if (vaildation() == true){
        if(answer_cnt == 0) {
            $('.previous').animate({
                opacity: '1'
            }, 200);
        }
        setTimeout(function(){
            if(answer_cnt < 13) //setTimeOut이 다른 함수들보다 늦게 실행되므로 <13지정을 안하면 맨 마지막에 13번째 요소를 fadeOut해버린다...
                $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
            if(answer_cnt==1 && $('input[name=room-type]:checked').val()=='1') //자취생이면
                answer_cnt++;
            else if(answer_cnt==12 && $('input[name=room-type]:checked').val()=='0'){//긱사생이면
                answer_cnt++;
                setScrollType(true);
                reloadProgressBar(answer_cnt+1);
            }
            answer_cnt += 1;
            nextClickCnt += 10;
        }, 0);
        setTimeout(function(){
            nextClickCnt -= 10;
            $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
        }, 700);
        if(answer_cnt == 13){
            setScrollType(false);
        }
        setTimeout(function(){
            if(answer_cnt < 12)
                reloadProgressBar(answer_cnt);
        }, 0)
    // }
})

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
    var scrollPosition = $(".question.share").offset().top;
    $("html, body").animate({
        scrollTop: scrollPosition
    }, 500).delay(1000);
    $question_list.css("margin-bottom", "40px");
    //제출버튼 보이게
    $('input[type=submit], .submit').show();
}

$('.previous').on('click', function(){
    if(answer_cnt == 1) {
        $(this).animate({
            'opacity': '0',
        }, 200);
    }
    if(answer_cnt != 0) {
        setTimeout(function(){
            $question_list.eq(answer_cnt).fadeOut(600/nextClickCnt);
            if(answer_cnt==3 && $('input[name=room-type]:checked').val()=='1')
                answer_cnt--;
            answer_cnt -= 1;
            nextClickCnt += 10;
        }, 0);
        setTimeout(function(){
            nextClickCnt -= 10;
            $question_list.eq(answer_cnt).fadeTo(600/nextClickCnt, 1);
        }, 700);
    }
    setTimeout(function(){
        reloadProgressBar(answer_cnt);
    }, 20)
})

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
function changeFrontBarWidth(width){
    $('.front-bar').animate( {
        width: format('{0}%', width)
      }, 400, 'swing' );
}

$('.front-bar > .text').css('opacity', '0')
var pb_width_block = 100 / 13;
//질문 수에 따라 진행바 길이 조절
function reloadProgressBar(pb_cnt){
    //흰색 바 조정해주는 함수
    changeFrontBarWidth(pb_width_block * answer_cnt);
    //진행상황 글자가 넘쳐서 front-bar가 어느정도 길어지면 나오게
    if(answer_cnt + 1 >= 3){
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "1"
            }, 600, "swing");
        }, 10);
    }
    
    //진행바 텍스트 애니메이션
    if(answer_cnt + 1< 3){
        setTimeout(function(){
            $('.front-bar > .text').animate( {
                opacity: "0"
            }, 600, "swing");
        }, 10);
    }
}

/*------------------------range bar 설명 구현------------------------*/

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

let $anw_arr = $(".answer");

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

