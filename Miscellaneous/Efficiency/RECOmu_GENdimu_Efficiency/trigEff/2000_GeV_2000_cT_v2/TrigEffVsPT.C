void TrigEffVsPT()
{
//=========Macro generated from canvas: c1/c1
//=========  (Mon Apr  4 18:40:36 2016) by ROOT version6.02/05
   TCanvas *c1 = new TCanvas("c1", "c1",20,42,700,500);
   c1->Range(-22,-0.03988803,198,0.3589923);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   Double_t divide_pTNum_by_pTDen_fx3002[160] = {
   0.5,
   1.5,
   2.5,
   3.5,
   4.5,
   5.5,
   6.5,
   7.5,
   8.5,
   9.5,
   10.5,
   11.5,
   12.5,
   13.5,
   14.5,
   15.5,
   16.5,
   17.5,
   18.5,
   19.5,
   20.5,
   21.5,
   22.5,
   23.5,
   24.5,
   25.5,
   26.5,
   27.5,
   28.5,
   29.5,
   30.5,
   31.5,
   32.5,
   33.5,
   34.5,
   35.5,
   36.5,
   37.5,
   38.5,
   39.5,
   40.5,
   41.5,
   42.5,
   43.5,
   44.5,
   45.5,
   46.5,
   47.5,
   48.5,
   49.5,
   50.5,
   51.5,
   52.5,
   53.5,
   54.5,
   55.5,
   56.5,
   57.5,
   58.5,
   59.5,
   60.5,
   61.5,
   62.5,
   63.5,
   64.5,
   65.5,
   66.5,
   67.5,
   68.5,
   69.5,
   70.5,
   71.5,
   72.5,
   73.5,
   74.5,
   75.5,
   76.5,
   77.5,
   78.5,
   79.5,
   80.5,
   81.5,
   82.5,
   83.5,
   84.5,
   85.5,
   86.5,
   87.5,
   88.5,
   89.5,
   90.5,
   91.5,
   92.5,
   93.5,
   94.5,
   95.5,
   96.5,
   97.5,
   98.5,
   99.5,
   100.5,
   101.5,
   102.5,
   103.5,
   104.5,
   105.5,
   106.5,
   107.5,
   108.5,
   109.5,
   110.5,
   111.5,
   112.5,
   113.5,
   114.5,
   115.5,
   116.5,
   117.5,
   118.5,
   119.5,
   120.5,
   121.5,
   122.5,
   123.5,
   124.5,
   125.5,
   126.5,
   127.5,
   128.5,
   129.5,
   130.5,
   131.5,
   132.5,
   133.5,
   134.5,
   135.5,
   136.5,
   137.5,
   138.5,
   139.5,
   140.5,
   141.5,
   142.5,
   143.5,
   144.5,
   145.5,
   146.5,
   147.5,
   148.5,
   149.5,
   150.5,
   151.5,
   152.5,
   153.5,
   154.5,
   155.5,
   156.5,
   157.5,
   158.5,
   159.5};
   Double_t divide_pTNum_by_pTDen_fy3002[160] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0.0006402868,
   0.0001172608,
   0.0002194667,
   0.0003099814,
   0.001702554,
   0.01100268,
   0.09685119,
   0.1282444,
   0.1480211,
   0.1578577,
   0.1685019,
   0.1821404,
   0.1979846,
   0.2050252,
   0.2115385,
   0.2090932,
   0.2216961,
   0.2156495,
   0.2249628,
   0.2214606,
   0.2316049,
   0.2306969,
   0.2252487,
   0.2322984,
   0.2324566,
   0.2197551,
   0.2229307,
   0.2179648,
   0.2163216,
   0.2137108,
   0.2186584,
   0.212504,
   0.2179464,
   0.2099331,
   0.2079733,
   0.2064398,
   0.2177,
   0.2001056,
   0.1870034,
   0.1990769,
   0.1822414,
   0.2057584,
   0.2063369,
   0.171475,
   0.1758653,
   0.1764133,
   0.1878659,
   0.189251,
   0.1605793,
   0.1695594,
   0.1899718,
   0.1797583,
   0.1740924,
   0.174359,
   0.1473881,
   0.1770944,
   0.1697531,
   0.1703878,
   0.1723356,
   0.1411609,
   0.1736909,
   0.1807407,
   0.1553957,
   0.1422018,
   0.1413238,
   0.1440678,
   0.1505792,
   0.1568228,
   0.1446281,
   0.1746725,
   0.1518692,
   0.1830986,
   0.1470588,
   0.1527778,
   0.1322751,
   0.1281337,
   0.1661342,
   0.1314985,
   0.1512346,
   0.1254355,
   0.1026616,
   0.1153846,
   0.1021127,
   0.1072961,
   0.0952381,
   0.1168831,
   0.155,
   0.1407035,
   0.1176471,
   0.1472081,
   0.1099476,
   0.09036145,
   0.1488095,
   0.1219512,
   0.1125828,
   0.1527778,
   0.1543624,
   0.06428571,
   0.1184211,
   0.1111111,
   0.1240876,
   0.1416667,
   0.1025641,
   0.1111111,
   0.1333333,
   0.1315789,
   0.13,
   0.112069,
   0.07692308,
   0.08333333,
   0.07692308,
   0.1190476,
   0.08695652,
   0.09876543,
   0.1538462,
   0.08641975,
   0.0754717,
   0.04,
   0.127907,
   0.1267606,
   0.1176471,
   0.08450704,
   0.1,
   0.09836066,
   0.1454545,
   0.07272727,
   0.06779661,
   0.1403509,
   0.07272727,
   0.1320755,
   0.08196721,
   0.16,
   0.09090909,
   0.1428571,
   0.05555556,
   0.125,
   0.09302326,
   0.2093023,
   0.04081633,
   0.09375,
   0.1041667,
   0.1111111,
   0.06451613,
   0.06896552,
   0.06666667,
   0.09090909,
   0.03125,
   0.1428571,
   0.08823529,
   0.04166667,
   0.1034483};
   Double_t divide_pTNum_by_pTDen_felx3002[160] = {
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5};
   Double_t divide_pTNum_by_pTDen_fely3002[160] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0.0002765374,
   9.700375e-05,
   0.0001417539,
   0.0001686981,
   0.0004086318,
   0.001019863,
   0.00284205,
   0.003185248,
   0.003342954,
   0.003432645,
   0.003472255,
   0.003560817,
   0.003637477,
   0.003749362,
   0.003735419,
   0.003745204,
   0.003837955,
   0.00381502,
   0.003924423,
   0.003911634,
   0.004051422,
   0.004106729,
   0.004126925,
   0.004298119,
   0.004383027,
   0.004454558,
   0.004548413,
   0.004654232,
   0.004802413,
   0.004944174,
   0.005165516,
   0.005239647,
   0.005535337,
   0.005667571,
   0.00572708,
   0.006161868,
   0.006397941,
   0.006551072,
   0.006618862,
   0.007062811,
   0.00709738,
   0.007643995,
   0.008030637,
   0.007663261,
   0.008310402,
   0.008494828,
   0.009104638,
   0.009467408,
   0.009305622,
   0.00979915,
   0.01054912,
   0.01067768,
   0.01102288,
   0.01122804,
   0.01094837,
   0.01260083,
   0.01219826,
   0.01306663,
   0.01289171,
   0.01280531,
   0.01373605,
   0.01504856,
   0.01393519,
   0.01384,
   0.01494289,
   0.01466105,
   0.01595633,
   0.01667852,
   0.01623233,
   0.01806789,
   0.01763864,
   0.01910729,
   0.01782466,
   0.01930312,
   0.01769451,
   0.01790898,
   0.02146911,
   0.01898961,
   0.02027342,
   0.01986298,
   0.01895332,
   0.02010822,
   0.01819107,
   0.02055523,
   0.01870226,
   0.02146702,
   0.02616424,
   0.02514655,
   0.02201556,
   0.02578153,
   0.0229688,
   0.02247599,
   0.02807826,
   0.02600144,
   0.02612508,
   0.03070891,
   0.03031926,
   0.02071706,
   0.02665269,
   0.02659058,
   0.02868759,
   0.03256252,
   0.02840351,
   0.0274628,
   0.02986035,
   0.03231482,
   0.0343188,
   0.02974245,
   0.02617859,
   0.02831906,
   0.03008874,
   0.03593072,
   0.029526,
   0.0334451,
   0.04197915,
   0.03131921,
   0.03576953,
   0.02169121,
   0.03672843,
   0.04023113,
   0.03966428,
   0.03300783,
   0.0361366,
   0.03831726,
   0.04871513,
   0.03448146,
   0.03216483,
   0.04706382,
   0.03448146,
   0.04739635,
   0.03494735,
   0.05339668,
   0.04299648,
   0.05516516,
   0.03580193,
   0.05884244,
   0.04398375,
   0.06499332,
   0.02631971,
   0.05058258,
   0.04424799,
   0.05240584,
   0.04156066,
   0.04441848,
   0.03606267,
   0.04906319,
   0.02586599,
   0.05516516,
   0.04763239,
   0.03449444,
   0.05576285};
   Double_t divide_pTNum_by_pTDen_fehx3002[160] = {
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5,
   0.5};
   Double_t divide_pTNum_by_pTDen_fehy3002[160] = {
   0.2312605,
   0.004782853,
   0.001360776,
   0.0007732394,
   0.0005158483,
   0.000404183,
   0.0003332817,
   0.0002910743,
   0.0002575244,
   0.0004329181,
   0.0002695921,
   0.0002893875,
   0.0003014356,
   0.0005205741,
   0.001117822,
   0.002917265,
   0.003253203,
   0.003405682,
   0.003493594,
   0.003529545,
   0.003615109,
   0.003687934,
   0.003800355,
   0.003783771,
   0.003794649,
   0.003885536,
   0.003864036,
   0.003973072,
   0.003961141,
   0.004100979,
   0.004157963,
   0.004180623,
   0.004353636,
   0.004440698,
   0.004519533,
   0.004614694,
   0.004726052,
   0.004879759,
   0.005027661,
   0.005253579,
   0.005334217,
   0.005636976,
   0.005780257,
   0.005843748,
   0.006298429,
   0.006534014,
   0.006712602,
   0.006800307,
   0.007252028,
   0.007313676,
   0.00785537,
   0.008263039,
   0.007937321,
   0.008622143,
   0.008819256,
   0.009446577,
   0.009833476,
   0.009747552,
   0.01025534,
   0.01100166,
   0.01117852,
   0.01158078,
   0.01180585,
   0.01163419,
   0.01331444,
   0.01290638,
   0.01387603,
   0.01366731,
   0.01380073,
   0.01460818,
   0.01604094,
   0.01497789,
   0.01499439,
   0.01630263,
   0.01593705,
   0.01738666,
   0.01816132,
   0.01779376,
   0.01957395,
   0.01937252,
   0.02068602,
   0.01967294,
   0.02136993,
   0.0197845,
   0.02014046,
   0.02375991,
   0.02142332,
   0.02258883,
   0.02269972,
   0.02227408,
   0.02334628,
   0.02126104,
   0.02427293,
   0.02225066,
   0.02511387,
   0.02993938,
   0.0291131,
   0.02582621,
   0.02971071,
   0.02751044,
   0.02805774,
   0.03269474,
   0.03114183,
   0.03189233,
   0.03606599,
   0.03546251,
   0.02797853,
   0.0322798,
   0.03268047,
   0.03485718,
   0.03927986,
   0.03618806,
   0.03398148,
   0.03595084,
   0.0396315,
   0.04276269,
   0.03737163,
   0.03574744,
   0.0385281,
   0.04311961,
   0.04644355,
   0.04008621,
   0.0450964,
   0.05215945,
   0.04344359,
   0.05566091,
   0.0373819,
   0.04670016,
   0.05250067,
   0.05289027,
   0.04706453,
   0.049704,
   0.05412846,
   0.06388,
   0.05377694,
   0.05036571,
   0.06190674,
   0.05377694,
   0.06387589,
   0.05164659,
   0.0693955,
   0.0660622,
   0.0755709,
   0.06861877,
   0.08785494,
   0.06746077,
   0.08079243,
   0.05131203,
   0.08285909,
   0.06432677,
   0.0791717,
   0.0788281,
   0.08381046,
   0.0606203,
   0.08059045,
   0.06822251,
   0.0755709,
   0.07844157,
   0.08938547,
   0.09049103};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(160,divide_pTNum_by_pTDen_fx3002,divide_pTNum_by_pTDen_fy3002,divide_pTNum_by_pTDen_felx3002,divide_pTNum_by_pTDen_fehx3002,divide_pTNum_by_pTDen_fely3002,divide_pTNum_by_pTDen_fehy3002);
   grae->SetName("divide_pTNum_by_pTDen");
   grae->SetTitle("pTNum");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   grae->SetLineColor(ci);
   
   TH1F *Graph_divide_pTNum_by_pTDen3002 = new TH1F("Graph_divide_pTNum_by_pTDen3002","pTNum",160,0,176);
   Graph_divide_pTNum_by_pTDen3002->SetMinimum(0);
   Graph_divide_pTNum_by_pTDen3002->SetMaximum(0.3191042);
   Graph_divide_pTNum_by_pTDen3002->SetDirectory(0);
   Graph_divide_pTNum_by_pTDen3002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_divide_pTNum_by_pTDen3002->SetLineColor(ci);
   Graph_divide_pTNum_by_pTDen3002->GetXaxis()->SetTitle("GEN p_{T} [GeV]");
   Graph_divide_pTNum_by_pTDen3002->GetXaxis()->SetLabelFont(42);
   Graph_divide_pTNum_by_pTDen3002->GetXaxis()->SetLabelSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetXaxis()->SetTitleSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetXaxis()->SetTitleFont(42);
   Graph_divide_pTNum_by_pTDen3002->GetYaxis()->SetTitle("HLT Efficiency");
   Graph_divide_pTNum_by_pTDen3002->GetYaxis()->SetLabelFont(42);
   Graph_divide_pTNum_by_pTDen3002->GetYaxis()->SetLabelSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetYaxis()->SetTitleSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetYaxis()->SetTitleFont(42);
   Graph_divide_pTNum_by_pTDen3002->GetZaxis()->SetLabelFont(42);
   Graph_divide_pTNum_by_pTDen3002->GetZaxis()->SetLabelSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetZaxis()->SetTitleSize(0.035);
   Graph_divide_pTNum_by_pTDen3002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_divide_pTNum_by_pTDen3002);
   
   grae->Draw("alp");
   
   TPaveText *pt = new TPaveText(0.431092,0.9339831,0.568908,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *AText = pt->AddText("pTNum");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
