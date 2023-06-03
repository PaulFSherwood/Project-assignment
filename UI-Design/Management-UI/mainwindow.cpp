#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "QtAwesome/QtAwesome.h"
#include "QtAwesome/QtAwesomeAnim.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Init QtAwesome
    fa::QtAwesome *awesome = new fa::QtAwesome(qApp);
    awesome->initFontAwesome();

    // Set the icon for your QPushButton
//    ui->min_btn->setIcon(awesome->icon(fa::fa_window_minimize)); //  icon(fa::fa_window_minimize));
    ui->min_btn->setIcon(awesome->icon("fa::fa_window_minimize"));

//    QLineSeries *series = new QLineSeries();

//    series->append(0, 6);
//    series->append(2, 4);
//    series->append(3, 8);
//    series->append(7, 4);
//    series->append(10, 5);

//    *series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 2);

//    QChart *chart = new QChart();
//    chart->legend()->hide();
//    chart->addSeries(series);
//    chart->createDefaultAxes();
//    chart->setTitle("Line Chart Example");

//    QChartView *chartView = new QChartView(chart);
//    chartView->setRenderHint(QPainter::Antialiasing);
//    chartView->scale(.5, .5);
//    chartView->setParent(ui->horizontalFrame);


}

MainWindow::~MainWindow()
{
    delete ui;
}

