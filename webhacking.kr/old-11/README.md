# _Old-11_

**Category:** _Web_

**Source:** _Webhacking.kr_

**Points:** _300_

**Author:** _galaxy(김경환)_

**Description:** 

> ![img](resource/prob.png)

## Point
정규표현식

## Write-up

감사하게도 source를 제공해주니 source를 봤습니다.

pat에 정규표현식을 넣고 preg_match로 get으로 받은 val과 비교하여

정규표현식에 해당되면 solve를 보여줍니다.

regexr.com에서 정규표현식을 넣으면 나름 해석도 해주고

값을 입력했을 경우 일치하는지도 찾아줍니다.

각 부분을 간략하게 설명하자면

[1-3] : 1~3중 하나가 존재해야함
[a-f]{5} : a~f중의 값이 5번 연속으로 나와야함
_  : _
.* : .이 0개 이상
```$_SERVER[REMOTE_ADDR](나의 공인ip) : ip가 들어가야함```
.* : .이 0개 이상
\tp\ta\ts\ts : \tp\ta\ts\ts이 존재

i.e. "1abcde_14.63.23.206	p	a	s	s"을 val에 값으로 보내주면 solve를 보여줍니다.

## References
https://regexr.com/
