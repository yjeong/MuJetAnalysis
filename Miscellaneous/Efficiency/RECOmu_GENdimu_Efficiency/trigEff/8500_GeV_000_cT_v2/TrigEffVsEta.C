void TrigEffVsEta()
{
//=========Macro generated from canvas: c/c
//=========  (Mon Apr  4 18:41:42 2016) by ROOT version6.02/05
   TCanvas *c = new TCanvas("c", "c",0,22,700,500);
   c->Range(-4.5,-0.1086106,4.5,0.9774952);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   Double_t divide_etaNum_by_etaDen_fx3001[60] = {
   -2.95,
   -2.85,
   -2.75,
   -2.65,
   -2.55,
   -2.45,
   -2.35,
   -2.25,
   -2.15,
   -2.05,
   -1.95,
   -1.85,
   -1.75,
   -1.65,
   -1.55,
   -1.45,
   -1.35,
   -1.25,
   -1.15,
   -1.05,
   -0.95,
   -0.85,
   -0.75,
   -0.65,
   -0.55,
   -0.45,
   -0.35,
   -0.25,
   -0.15,
   -0.05,
   0.05,
   0.15,
   0.25,
   0.35,
   0.45,
   0.55,
   0.65,
   0.75,
   0.85,
   0.95,
   1.05,
   1.15,
   1.25,
   1.35,
   1.45,
   1.55,
   1.65,
   1.75,
   1.85,
   1.95,
   2.05,
   2.15,
   2.25,
   2.35,
   2.45,
   2.55,
   2.65,
   2.75,
   2.85,
   2.95};
   Double_t divide_etaNum_by_etaDen_fy3001[60] = {
   0.002747253,
   0.006912442,
   0.006451613,
   0.03809524,
   0.08709677,
   0.1442857,
   0.4087883,
   0.4863861,
   0.5542857,
   0.5579632,
   0.6005917,
   0.6290944,
   0.6061706,
   0.6494253,
   0.652381,
   0.6601307,
   0.6794501,
   0.6870079,
   0.7046527,
   0.7272099,
   0.7169231,
   0.7104946,
   0.717486,
   0.7263711,
   0.7488713,
   0.7515887,
   0.7798271,
   0.7171053,
   0.751004,
   0.7586994,
   0.7619853,
   0.750416,
   0.7264808,
   0.7690531,
   0.7472206,
   0.7527697,
   0.7346939,
   0.7374037,
   0.7181083,
   0.7134831,
   0.6909564,
   0.6941876,
   0.6919918,
   0.6666667,
   0.664128,
   0.65,
   0.6477273,
   0.6009009,
   0.5850662,
   0.562753,
   0.5747614,
   0.521327,
   0.5219072,
   0.4343434,
   0.1676301,
   0.04642857,
   0.03880071,
   0.02083333,
   0.002369668,
   0};
   Double_t divide_etaNum_by_etaDen_felx3001[60] = {
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05};
   Double_t divide_etaNum_by_etaDen_fely3001[60] = {
   0.002272767,
   0.003759689,
   0.003509187,
   0.008348306,
   0.01142065,
   0.01345605,
   0.01846646,
   0.01817315,
   0.01742852,
   0.01694392,
   0.01596837,
   0.01559572,
   0.0152645,
   0.0142032,
   0.01393182,
   0.01407656,
   0.01304469,
   0.01232876,
   0.01232166,
   0.01220789,
   0.01161708,
   0.01156709,
   0.01167803,
   0.01119304,
   0.01072594,
   0.01082119,
   0.01039982,
   0.0109397,
   0.01079016,
   0.01065384,
   0.0105455,
   0.01060963,
   0.01116474,
   0.01057262,
   0.01095156,
   0.01085766,
   0.01109031,
   0.01115191,
   0.01167093,
   0.01174209,
   0.01223618,
   0.01229977,
   0.01255174,
   0.01301149,
   0.01353863,
   0.01418645,
   0.01468681,
   0.01523599,
   0.01569577,
   0.01634451,
   0.01670229,
   0.0178027,
   0.01859289,
   0.0194377,
   0.01441207,
   0.008908602,
   0.008109095,
   0.006444668,
   0.001960383,
   0};
   Double_t divide_etaNum_by_etaDen_fehx3001[60] = {
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05,
   0.05};
   Double_t divide_etaNum_by_etaDen_fehy3001[60] = {
   0.006288795,
   0.006678127,
   0.006235766,
   0.01030648,
   0.01284615,
   0.01452614,
   0.01871818,
   0.01820801,
   0.0173003,
   0.01681425,
   0.01576372,
   0.01533914,
   0.01506598,
   0.0139506,
   0.01368291,
   0.01380715,
   0.01277763,
   0.01207667,
   0.01203792,
   0.01188494,
   0.01134285,
   0.0113064,
   0.01139997,
   0.01092183,
   0.01043745,
   0.01052252,
   0.01006802,
   0.01069554,
   0.01049427,
   0.01035056,
   0.01024183,
   0.01032439,
   0.01089468,
   0.01025319,
   0.01065429,
   0.01055474,
   0.01080923,
   0.01086278,
   0.01139206,
   0.01146831,
   0.01198094,
   0.0120362,
   0.01228158,
   0.01276903,
   0.01328144,
   0.01393329,
   0.0144207,
   0.01504872,
   0.01553004,
   0.01621348,
   0.01653861,
   0.01775046,
   0.01853445,
   0.01963427,
   0.01542069,
   0.01068943,
   0.009911064,
   0.008757176,
   0.005427842,
   0.004950031};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(60,divide_etaNum_by_etaDen_fx3001,divide_etaNum_by_etaDen_fy3001,divide_etaNum_by_etaDen_felx3001,divide_etaNum_by_etaDen_fehx3001,divide_etaNum_by_etaDen_fely3001,divide_etaNum_by_etaDen_fehy3001);
   grae->SetName("divide_etaNum_by_etaDen");
   grae->SetTitle("etaNum");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   grae->SetLineColor(ci);
   
   TH1F *Graph_divide_etaNum_by_etaDen3001 = new TH1F("Graph_divide_etaNum_by_etaDen3001","etaNum",100,-3.6,3.6);
   Graph_divide_etaNum_by_etaDen3001->SetMinimum(0);
   Graph_divide_etaNum_by_etaDen3001->SetMaximum(0.8688846);
   Graph_divide_etaNum_by_etaDen3001->SetDirectory(0);
   Graph_divide_etaNum_by_etaDen3001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_divide_etaNum_by_etaDen3001->SetLineColor(ci);
   Graph_divide_etaNum_by_etaDen3001->GetXaxis()->SetTitle("GEN #eta");
   Graph_divide_etaNum_by_etaDen3001->GetXaxis()->SetLabelFont(42);
   Graph_divide_etaNum_by_etaDen3001->GetXaxis()->SetLabelSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetXaxis()->SetTitleSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetXaxis()->SetTitleFont(42);
   Graph_divide_etaNum_by_etaDen3001->GetYaxis()->SetTitle("HLT Efficiency");
   Graph_divide_etaNum_by_etaDen3001->GetYaxis()->SetLabelFont(42);
   Graph_divide_etaNum_by_etaDen3001->GetYaxis()->SetLabelSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetYaxis()->SetTitleSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetYaxis()->SetTitleFont(42);
   Graph_divide_etaNum_by_etaDen3001->GetZaxis()->SetLabelFont(42);
   Graph_divide_etaNum_by_etaDen3001->GetZaxis()->SetLabelSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetZaxis()->SetTitleSize(0.035);
   Graph_divide_etaNum_by_etaDen3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_divide_etaNum_by_etaDen3001);
   
   grae->Draw("alp");
   
   TPaveText *pt = new TPaveText(0.4275,0.94,0.5725,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *AText = pt->AddText("etaNum");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
