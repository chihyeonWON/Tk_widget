# Tk_widget
tkinter와 Python언어를 사용하여 위젯의 위치를 마음대로 조정해보는 연습

## 1. pack() 함수 사용법 (tk_pack.py)   

먼저 실습을 진행할 창을 하나 만들어줍니다.   
```python
from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")


win.mainloop()
```

버튼을 아무 옵션없이 생성하면 다음과 같이 Top에 위치하게됩니다.

```python
btn = Button(win)
btn.config(text="버튼")
btn.pack()
```   

![pack_default](https://user-images.githubusercontent.com/58906858/151921436-91f0ec45-ff01-490b-b8e4-b6796ffdbb85.png)   

### pack함수 안에 side 옵션으로 bottom, left, right를 줄 수 있습니다.   

다음은 pack함수 안에 side 옵션으로 bottom을 준 결과창입니다.   
![pack_bottom](https://user-images.githubusercontent.com/58906858/151921606-7f6ab8c6-914b-498b-9e4a-e944b97074d2.png)   

### pad 옵션으로 간격을 지정해 줄 수 있습니다.   

padx와 pady로 값을 줘서 지정할 수 있는데 padx는 위젯의 양옆에 간격을 주고 pady는 위젯의 위아래로 간격을 줍니다.  
   
사용의 예시로 버튼을 한개 더 만들어서 pady옵션의 값으로 40을 주면 다음과 같이 위아래로 간격이 생깁니다.   
```python
btn = Button(win)
btn.config(text="버튼")
btn.pack()

btn1 = Button(win)
btn1.config(text="버튼1")
btn1.pack(pady=40)
```   
![pack_pady](https://user-images.githubusercontent.com/58906858/151922377-166f587d-e30b-4a62-a2d3-f6ec57d57eff.png)   
   
## 2. grid() 함수 사용법 (tk_grid.py)   

마찬가지로 실습을 할 창을 하나 만들어줍니다.
```python
먼저 실습을 진행할 창을 하나 만들어줍니다.   
```python
from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")


win.mainloop()
```   

### grid 함수의 column과 row 옵션으로 위젯이 위치할 지점을 정할 수 있습니다. (column은 오른쪽에서 왼쪽 기준, row는 위쪽에서 아래쪽 기준)   
   
다음은 grid 함수의 column과 row의 값에 0을 넣은 모습입니다.      
![grid_default](https://user-images.githubusercontent.com/58906858/151923645-2a4cc82d-4f7c-4ef2-97fe-41a1aa6bb377.png)
   
다음은 column의 값에 2 row의 값에 0을 넣은 버튼을 하나 더 추가한 모습입니다.   
```python
btn2 = Button(win)
btn2.config(text="(1,0)")
btn2.grid(column=2, row=0)
```   
![grid_col2](https://user-images.githubusercontent.com/58906858/151924218-7e455d6c-e842-4002-9a79-81d1421e15c3.png)   
   
### grid 함수도 pack 함수처럼 pad로 간격을 지정해 줄 수 있습니다.(이번엔 생략)   
   
### grid 함수의 특징으로 (0,1)을 지정하지 않고 (0,2)를 지정해주면 어떻게 되는 지 알아보겠습니다.   

```python
btn1 = Button(win)
btn1.config(text="(0,0)")
btn1.grid(column=0, row=0)

btn2 = Button(win)  
btn2.config(text="(1,0)")
btn2.grid(column=2, row=0)

btn3 = Button(win)
btn3.config(text="(0,3)")
btn3.grid(column=0, row=3)
```

다음과 같이 (0,1) 위치에 (0,3)이 들어가는 것을 알 수 있습니다. 이것이 grid 함수의 특징입니다.   
![grid_col0row3](https://user-images.githubusercontent.com/58906858/151924718-b82629ff-9e06-4a2b-9c47-f1599fbf2e5a.png)

### 셀 병합하기 rowspan, columnspan   

grid 함수의 rowspan, columnspan을 이용하면 셀을 병합할 수 있습니다.   
```python
btn4 = Button(win)
btn4.config(text="셀병합")
btn4.grid(column=0, row=0, columnspan=1)
```   
버튼을 하나 더 만들고 columnspan의 값으로 1을 주면 공간의 위치는 0,0 인데 오른쪽으로 한 칸 병합하는 것입니다.      
![grid_columnspan](https://user-images.githubusercontent.com/58906858/151925935-23b1d627-69f9-4e63-a312-9ca633847a02.png)   
   
## 3. place() 함수 사용법 (tk_place.py)   

마찬가지로 실습을 할 창을 하나 만들어줍니다.
```python
from tkinter import *  # tkinter에서 모든 함수를 들고 옵니다.
win = Tk()
win.geometry("400x200")
win.title("place")
win.option_add("*Font", "궁서 20")

win.mainloop()
```   
### place 함수는 x와 y에 값을 넣어서 창의 크기와 관계없이 절대적으로 위치를 지정할 수 있습니다.   
   
다음은 버튼의 place 함수의 옵션 x와 y 값에 0을 넣은 모습입니다.
```python
btn = Button(win)
btn.config(text="(0,0)")
btn.place(x=0, y=0)
```   
   
![place_x0y0](https://user-images.githubusercontent.com/58906858/151926971-755d2768-da09-4c66-a1c5-e4cab9fd84bb.png)   

버튼을 한 개 더 만들고 place 함수의 옵션 x, y 값으로 50, 100을 넣은 모습입니다.
   
```python
btn1 = Button(win)
btn1.config(text="(50,100)")
btn1.place(x=50, y=100)
```   

![place_x50y100](https://user-images.githubusercontent.com/58906858/151927261-5b006f59-0645-4c48-88dd-f5b725ebe870.png)

이와 같이 옵션 x, y 에 값을 지정해 주어 창 크기와 관계없이 절대적으로 위치를 지정합니다.

### relx, rely 옵션으로 창 크기에 대해 상대적인 위치를 지정할 수 있습니다.   
   
relx와 rely 옵션에 값을 넣을 때는 창의 크기를 1로 가정하고 0과 1사이의 값을 넣어줘야 합니다.

다음은 버튼을 만들고 옵션 relx와 rely의 값으로 0.5, 0.5 값을 준 결과창입니다.
```python
btn2 = Button(win)
btn2.config(text="(0.5,0.5)")
btn2.place(relx=0.5, rely=0.5)
```   
![place_relx0 5rely0 5](https://user-images.githubusercontent.com/58906858/151927734-4b82d5a4-a487-463d-bb4d-6c8e9a9566ee.png)

이 창을 무작위로 크게 늘려보겠습니다.   
![place_rel abs](https://user-images.githubusercontent.com/58906858/151927943-f0f92110-6dc4-4f25-9cb6-f9bfe2cf0a2a.png)

절대좌표인 옵션 x, y를 사용한 0,0과 50,100은 창의 크기와 관계없이 절대적으로 위치가 고정되어있음을 알 수 있지만   
상대좌표인 옵션 relx, rely를 사용한 0.5,0.5는 창의 크기예 비례해서 위치가 변경되었음을 알 수 있습니다.

ps.초보자인 경우에는 상대좌표와 절대좌표인 place 함수를 이용하기보다는 pack 함수를 사용해서 기능을 만든 뒤에 위치를 지정하는 등 세부적으로 꾸며 나가는 방법이 더 좋을 것이라고 생각됩니다.   
프로그램이 얼추 완성된 후에는 grid 함수와 place 함수를 이용해 추가적으로 배치하는 방법이 더 깔끔한 프로그램의 위젯의 배치를 구현할 수 있을 것입니다.



   

