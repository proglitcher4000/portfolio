from random import randint
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QVBoxLayout, QGroupBox, QLabel, QRadioButton,QHBoxLayout, QPushButton
#создай приложение для запоминания информации

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3) :
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('MemoryCard')
main_win.resize(600,400)

questionLabel = QLabel('Какой национальности не существует')
radioGroupBox = QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')

answers = [rbtn1,rbtn2,rbtn3,rbtn4]

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn1)
ButtonGroup.addButton(rbtn2)
ButtonGroup.addButton(rbtn3)
ButtonGroup.addButton(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

ansGroupBox = QGroupBox('Результат теста')

anstext = QLabel('Правильно/Неправильно')
resulttext = QLabel('Правильный ответ')
ansVLine = QVBoxLayout()
ansVLine.addWidget(anstext, alignment=Qt.AlignCenter)
ansVLine.addWidget(resulttext, alignment=Qt.AlignCenter)

ansGroupBox.setLayout(ansVLine)

radioGroupBox.setLayout(layout_ans1)

score = 0
n = 0
r = 0


scoretext = QLabel('Количество правильных ответов'+str(score))
ntext = QLabel('Количество правильных ответов'+str(score))
scoretext = QLabel('Количество правильных ответов'+str(score))
button = QPushButton('Ответить')

vline = QVBoxLayout()
vline.addWidget(questionLabel, alignment=Qt.AlignCenter)
vline.addWidget(radioGroupBox, alignment=Qt.AlignCenter)
vline.addWidget(ansGroupBox, alignment=Qt.AlignCenter)
ansGroupBox.hide()
hline3 = QHBoxLayout()
hline3.addStretch(1)
hline3.addWidget(button,stretch=1,alignment=Qt.AlignCenter)
vline.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(vline)

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    questionLabel.setText(q.question)
    resulttext.setText(q.right_answer)
    show_question()


def show_result():
    radioGroupBox.hide()
    ansGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    radioGroupBox.show()
    ansGroupBox.hide()
    button.setText('Ответить')
    ButtonGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    ButtonGroup.setExclusive(True)
    show_question()

def start_test():
    if button.text() == 'Ответить':
        global n,vf
        n += 1
        ntext.setText('Количество вопросов:',+str(n))
        if answers[0].isChecked():
            anstext.setText('ПРАВИЛЬНО')
            show_result()
            scoreText.setText('')
        else:
            anstext.setText('Неправильно')
            show_result()
            global score
        r = round(scotr/n * 100,2)
        rtext.setText('Рейтинг: '+str(r)+'8')
    else:
        ask( question_list[randint(0, len(question_list)-1)])


question_list = []
q = Question('1+0','1', '2', '0','10')
question_list.append(q)
q = Question('4+4+4+4','4444','16','320','4')
question_list.append(q)
q = Question('Конфета это', 'Жевачка', 'Печенье', 'Вафля', 'Леденец')
question_list.append(q)
q = Question('Самый популярный бренд это', 'Louis Vilton', 'Gucci', 'Prada', 'Supreme')
question_list.append(q)
q = Question('8-8','0','1','80','101')
question_list.append(q)
q = Question('8-8','0','1','80','101')
question_list.append(q)
q = Question('9999', '9,9,9,9','99,99','9, 99,9','9 9 9 9')
question_list.append(q)

button.clicked.connect(start_test)

ask( question_list[randint(0, len(question_list)-1)])


main_win.show()

app.exec_()