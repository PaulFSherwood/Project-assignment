/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.2.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QWidget *left_menu_widget;
    QVBoxLayout *verticalLayout;
    QFrame *frame_3;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QFrame *frame_4;
    QVBoxLayout *verticalLayout_2;
    QPushButton *pushButton;
    QPushButton *pushButton_5;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label_2;
    QFrame *frame_6;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QFrame *frame_2;
    QVBoxLayout *verticalLayout_4;
    QFrame *header_frame;
    QHBoxLayout *horizontalLayout_3;
    QFrame *frame_10;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *pushButton_6;
    QLabel *label_6;
    QFrame *frame_11;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_7;
    QFrame *header_nav;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *min_btn;
    QPushButton *max_btn;
    QPushButton *close_btn;
    QFrame *frame_8;
    QVBoxLayout *verticalLayout_7;
    QStackedWidget *stackedWidget;
    QWidget *percentage_bar_chart;
    QVBoxLayout *verticalLayout_8;
    QFrame *frame_15;
    QVBoxLayout *verticalLayout_9;
    QLabel *label_9;
    QFrame *frame_16;
    QGridLayout *gridLayout;
    QWidget *temperature_bar_chart;
    QVBoxLayout *verticalLayout_11;
    QFrame *frame_17;
    QVBoxLayout *verticalLayout_10;
    QLabel *label_10;
    QFrame *frame_18;
    QGridLayout *gridLayout_2;
    QWidget *nested_donuts;
    QVBoxLayout *verticalLayout_13;
    QFrame *frame_19;
    QVBoxLayout *verticalLayout_12;
    QLabel *label_11;
    QFrame *frame_20;
    QGridLayout *gridLayout_3;
    QWidget *line_charts;
    QVBoxLayout *verticalLayout_15;
    QFrame *frame_21;
    QVBoxLayout *verticalLayout_14;
    QLabel *label_12;
    QFrame *frame_22;
    QGridLayout *gridLayout_4;
    QWidget *bar_charts;
    QVBoxLayout *verticalLayout_17;
    QFrame *frame_23;
    QVBoxLayout *verticalLayout_16;
    QLabel *label_13;
    QFrame *frame_24;
    QGridLayout *gridLayout_5;
    QFrame *frame_9;
    QHBoxLayout *horizontalLayout_6;
    QFrame *frame_13;
    QVBoxLayout *verticalLayout_6;
    QLabel *label_8;
    QFrame *frame_14;
    QFrame *size_grip;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 600);
        MainWindow->setStyleSheet(QString::fromUtf8("@font-face {\n"
"	font-family: Verdana;\n"
"}\n"
"* {\n"
"	color: #ffffff;\n"
"	font-family: Verdana;\n"
"	font-size: 12px;\n"
"	border: nine;\n"
"	background: none;\n"
"}\n"
"#centralwidget {\n"
"	background-color: rgb(33, 43, 51);\n"
"}\n"
"#left_menu_widget, #percentage_bar, #nested_donuts,\n"
"#line_charts, #bar_charts, #temperature_bar_chart\n"
"{\n"
"	background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"#header_frame, #frame_3, #frame_5 {\n"
"	background-color: rgb(61, 80, 95);\n"
"}\n"
"#frame_4 QPushButton {\n"
"	padding: 10px;\n"
"	border-raidus: 5px;\n"
"	background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#header_nav QPushButton {\n"
"	background-color: rgb(61, 80, 95);\n"
"	border-radius: 15px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#frame_11 QPushButton {\n"
"	background-color: rgb(61, 80, 95);\n"
"	border-radius: 15px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#frame_11 QPushButton:hover {\n"
"	background-color: rgb(120, 157, 186);\n"
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        left_menu_widget = new QWidget(centralwidget);
        left_menu_widget->setObjectName(QString::fromUtf8("left_menu_widget"));
        verticalLayout = new QVBoxLayout(left_menu_widget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame_3 = new QFrame(left_menu_widget);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frame_3);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(frame_3);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);


        verticalLayout->addWidget(frame_3);

        frame_4 = new QFrame(left_menu_widget);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame_4);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        pushButton = new QPushButton(frame_4);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout_2->addWidget(pushButton);

        pushButton_5 = new QPushButton(frame_4);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));

        verticalLayout_2->addWidget(pushButton_5);

        pushButton_2 = new QPushButton(frame_4);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        verticalLayout_2->addWidget(pushButton_2);

        pushButton_3 = new QPushButton(frame_4);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        verticalLayout_2->addWidget(pushButton_3);

        pushButton_4 = new QPushButton(frame_4);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        verticalLayout_2->addWidget(pushButton_4);


        verticalLayout->addWidget(frame_4);

        frame_5 = new QFrame(left_menu_widget);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(frame_5);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        label_2 = new QLabel(frame_5);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_7->addWidget(label_2);


        verticalLayout->addWidget(frame_5);

        frame_6 = new QFrame(left_menu_widget);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(frame_6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        label_3 = new QLabel(frame_6);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout_3->addWidget(label_3);

        label_4 = new QLabel(frame_6);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        verticalLayout_3->addWidget(label_4);

        label_5 = new QLabel(frame_6);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        verticalLayout_3->addWidget(label_5);


        verticalLayout->addWidget(frame_6);


        horizontalLayout->addWidget(left_menu_widget);

        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(frame_2);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        header_frame = new QFrame(frame_2);
        header_frame->setObjectName(QString::fromUtf8("header_frame"));
        header_frame->setFrameShape(QFrame::StyledPanel);
        header_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(header_frame);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        frame_10 = new QFrame(header_frame);
        frame_10->setObjectName(QString::fromUtf8("frame_10"));
        frame_10->setFrameShape(QFrame::StyledPanel);
        frame_10->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(frame_10);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        pushButton_6 = new QPushButton(frame_10);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));

        horizontalLayout_4->addWidget(pushButton_6);

        label_6 = new QLabel(frame_10);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_4->addWidget(label_6);


        horizontalLayout_3->addWidget(frame_10);

        frame_11 = new QFrame(header_frame);
        frame_11->setObjectName(QString::fromUtf8("frame_11"));
        frame_11->setFrameShape(QFrame::StyledPanel);
        frame_11->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(frame_11);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        label_7 = new QLabel(frame_11);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        verticalLayout_5->addWidget(label_7);


        horizontalLayout_3->addWidget(frame_11);

        header_nav = new QFrame(header_frame);
        header_nav->setObjectName(QString::fromUtf8("header_nav"));
        header_nav->setFrameShape(QFrame::StyledPanel);
        header_nav->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(header_nav);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        min_btn = new QPushButton(header_nav);
        min_btn->setObjectName(QString::fromUtf8("min_btn"));

        horizontalLayout_5->addWidget(min_btn);

        max_btn = new QPushButton(header_nav);
        max_btn->setObjectName(QString::fromUtf8("max_btn"));

        horizontalLayout_5->addWidget(max_btn);

        close_btn = new QPushButton(header_nav);
        close_btn->setObjectName(QString::fromUtf8("close_btn"));

        horizontalLayout_5->addWidget(close_btn);


        horizontalLayout_3->addWidget(header_nav);


        verticalLayout_4->addWidget(header_frame);

        frame_8 = new QFrame(frame_2);
        frame_8->setObjectName(QString::fromUtf8("frame_8"));
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        verticalLayout_7 = new QVBoxLayout(frame_8);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        stackedWidget = new QStackedWidget(frame_8);
        stackedWidget->setObjectName(QString::fromUtf8("stackedWidget"));
        stackedWidget->setStyleSheet(QString::fromUtf8("\n"
"#stackedWidget QStackedWidget {\n"
"	background-color: rgb(13, 13, 13);\n"
"}"));
        percentage_bar_chart = new QWidget();
        percentage_bar_chart->setObjectName(QString::fromUtf8("percentage_bar_chart"));
        verticalLayout_8 = new QVBoxLayout(percentage_bar_chart);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        frame_15 = new QFrame(percentage_bar_chart);
        frame_15->setObjectName(QString::fromUtf8("frame_15"));
        frame_15->setFrameShape(QFrame::StyledPanel);
        frame_15->setFrameShadow(QFrame::Raised);
        verticalLayout_9 = new QVBoxLayout(frame_15);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        label_9 = new QLabel(frame_15);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setAlignment(Qt::AlignCenter);

        verticalLayout_9->addWidget(label_9, 0, Qt::AlignTop);


        verticalLayout_8->addWidget(frame_15, 0, Qt::AlignTop);

        frame_16 = new QFrame(percentage_bar_chart);
        frame_16->setObjectName(QString::fromUtf8("frame_16"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_16->sizePolicy().hasHeightForWidth());
        frame_16->setSizePolicy(sizePolicy);
        frame_16->setFrameShape(QFrame::StyledPanel);
        frame_16->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(frame_16);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));

        verticalLayout_8->addWidget(frame_16);

        stackedWidget->addWidget(percentage_bar_chart);
        temperature_bar_chart = new QWidget();
        temperature_bar_chart->setObjectName(QString::fromUtf8("temperature_bar_chart"));
        verticalLayout_11 = new QVBoxLayout(temperature_bar_chart);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        frame_17 = new QFrame(temperature_bar_chart);
        frame_17->setObjectName(QString::fromUtf8("frame_17"));
        frame_17->setFrameShape(QFrame::StyledPanel);
        frame_17->setFrameShadow(QFrame::Raised);
        verticalLayout_10 = new QVBoxLayout(frame_17);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        label_10 = new QLabel(frame_17);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setAlignment(Qt::AlignCenter);

        verticalLayout_10->addWidget(label_10, 0, Qt::AlignTop);


        verticalLayout_11->addWidget(frame_17);

        frame_18 = new QFrame(temperature_bar_chart);
        frame_18->setObjectName(QString::fromUtf8("frame_18"));
        sizePolicy.setHeightForWidth(frame_18->sizePolicy().hasHeightForWidth());
        frame_18->setSizePolicy(sizePolicy);
        frame_18->setFrameShape(QFrame::StyledPanel);
        frame_18->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(frame_18);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));

        verticalLayout_11->addWidget(frame_18);

        stackedWidget->addWidget(temperature_bar_chart);
        nested_donuts = new QWidget();
        nested_donuts->setObjectName(QString::fromUtf8("nested_donuts"));
        verticalLayout_13 = new QVBoxLayout(nested_donuts);
        verticalLayout_13->setObjectName(QString::fromUtf8("verticalLayout_13"));
        frame_19 = new QFrame(nested_donuts);
        frame_19->setObjectName(QString::fromUtf8("frame_19"));
        frame_19->setFrameShape(QFrame::StyledPanel);
        frame_19->setFrameShadow(QFrame::Raised);
        verticalLayout_12 = new QVBoxLayout(frame_19);
        verticalLayout_12->setObjectName(QString::fromUtf8("verticalLayout_12"));
        label_11 = new QLabel(frame_19);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setAlignment(Qt::AlignCenter);

        verticalLayout_12->addWidget(label_11, 0, Qt::AlignTop);


        verticalLayout_13->addWidget(frame_19);

        frame_20 = new QFrame(nested_donuts);
        frame_20->setObjectName(QString::fromUtf8("frame_20"));
        sizePolicy.setHeightForWidth(frame_20->sizePolicy().hasHeightForWidth());
        frame_20->setSizePolicy(sizePolicy);
        frame_20->setFrameShape(QFrame::StyledPanel);
        frame_20->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(frame_20);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));

        verticalLayout_13->addWidget(frame_20);

        stackedWidget->addWidget(nested_donuts);
        line_charts = new QWidget();
        line_charts->setObjectName(QString::fromUtf8("line_charts"));
        verticalLayout_15 = new QVBoxLayout(line_charts);
        verticalLayout_15->setObjectName(QString::fromUtf8("verticalLayout_15"));
        frame_21 = new QFrame(line_charts);
        frame_21->setObjectName(QString::fromUtf8("frame_21"));
        frame_21->setFrameShape(QFrame::StyledPanel);
        frame_21->setFrameShadow(QFrame::Raised);
        verticalLayout_14 = new QVBoxLayout(frame_21);
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        label_12 = new QLabel(frame_21);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setAlignment(Qt::AlignCenter);

        verticalLayout_14->addWidget(label_12, 0, Qt::AlignTop);


        verticalLayout_15->addWidget(frame_21);

        frame_22 = new QFrame(line_charts);
        frame_22->setObjectName(QString::fromUtf8("frame_22"));
        sizePolicy.setHeightForWidth(frame_22->sizePolicy().hasHeightForWidth());
        frame_22->setSizePolicy(sizePolicy);
        frame_22->setFrameShape(QFrame::StyledPanel);
        frame_22->setFrameShadow(QFrame::Raised);
        gridLayout_4 = new QGridLayout(frame_22);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));

        verticalLayout_15->addWidget(frame_22);

        stackedWidget->addWidget(line_charts);
        bar_charts = new QWidget();
        bar_charts->setObjectName(QString::fromUtf8("bar_charts"));
        verticalLayout_17 = new QVBoxLayout(bar_charts);
        verticalLayout_17->setObjectName(QString::fromUtf8("verticalLayout_17"));
        frame_23 = new QFrame(bar_charts);
        frame_23->setObjectName(QString::fromUtf8("frame_23"));
        frame_23->setFrameShape(QFrame::StyledPanel);
        frame_23->setFrameShadow(QFrame::Raised);
        verticalLayout_16 = new QVBoxLayout(frame_23);
        verticalLayout_16->setObjectName(QString::fromUtf8("verticalLayout_16"));
        label_13 = new QLabel(frame_23);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setAlignment(Qt::AlignCenter);

        verticalLayout_16->addWidget(label_13, 0, Qt::AlignTop);


        verticalLayout_17->addWidget(frame_23);

        frame_24 = new QFrame(bar_charts);
        frame_24->setObjectName(QString::fromUtf8("frame_24"));
        sizePolicy.setHeightForWidth(frame_24->sizePolicy().hasHeightForWidth());
        frame_24->setSizePolicy(sizePolicy);
        frame_24->setFrameShape(QFrame::StyledPanel);
        frame_24->setFrameShadow(QFrame::Raised);
        gridLayout_5 = new QGridLayout(frame_24);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));

        verticalLayout_17->addWidget(frame_24);

        stackedWidget->addWidget(bar_charts);

        verticalLayout_7->addWidget(stackedWidget);


        verticalLayout_4->addWidget(frame_8);

        frame_9 = new QFrame(frame_2);
        frame_9->setObjectName(QString::fromUtf8("frame_9"));
        frame_9->setFrameShape(QFrame::StyledPanel);
        frame_9->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(frame_9);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        frame_13 = new QFrame(frame_9);
        frame_13->setObjectName(QString::fromUtf8("frame_13"));
        frame_13->setFrameShape(QFrame::StyledPanel);
        frame_13->setFrameShadow(QFrame::Raised);
        verticalLayout_6 = new QVBoxLayout(frame_13);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        label_8 = new QLabel(frame_13);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        verticalLayout_6->addWidget(label_8);


        horizontalLayout_6->addWidget(frame_13);

        frame_14 = new QFrame(frame_9);
        frame_14->setObjectName(QString::fromUtf8("frame_14"));
        frame_14->setFrameShape(QFrame::StyledPanel);
        frame_14->setFrameShadow(QFrame::Raised);
        size_grip = new QFrame(frame_14);
        size_grip->setObjectName(QString::fromUtf8("size_grip"));
        size_grip->setGeometry(QRect(110, 70, 120, 80));
        size_grip->setFrameShape(QFrame::StyledPanel);
        size_grip->setFrameShadow(QFrame::Raised);

        horizontalLayout_6->addWidget(frame_14);


        verticalLayout_4->addWidget(frame_9);


        horizontalLayout->addWidget(frame_2);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        stackedWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "QT CHARTS", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Percentage Bar Chart", nullptr));
        pushButton_5->setText(QCoreApplication::translate("MainWindow", "Temperature Records", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "Nested Donuts", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "Line Charts", nullptr));
        pushButton_4->setText(QCoreApplication::translate("MainWindow", "Bar Charts", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "SUPPORT ME", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Patreaon", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Sub to YouTube", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "PayPal", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "MENU", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "DASHBOARD", nullptr));
        min_btn->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
        max_btn->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
        close_btn->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Percentage Bar Chart", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "Temperature Bar Chart", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "Nested Donut Chart", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "Line Chart", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "Bar Chart", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "Copyright Something here", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
