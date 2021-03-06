#####################################
#
# 'ADDITION AND CONVOLUTION' ROOT.RooFit tutorial macro #206
#
# ROOT.Tools for visualization of ROOT.RooAbsArg expression trees
#
#
#
# 07/2008 - Wouter Verkerke
#
# /


import ROOT


def rf206_treevistools():
    # S e t u p   c o m p o s i t e    p d f
    # --------------------------------------

    # Declare observable x
    x = ROOT.RooRealVar("x", "x", 0, 10)

    # Create two Gaussian PDFs g1(x,mean1,sigma) anf g2(x,mean2,sigma) and
    # their parameters
    mean = ROOT.RooRealVar("mean", "mean of gaussians", 5)
    sigma1 = ROOT.RooRealVar("sigma1", "width of gaussians", 0.5)
    sigma2 = ROOT.RooRealVar("sigma2", "width of gaussians", 1)
    sig1 = ROOT.RooGaussian("sig1", "Signal component 1", x, mean, sigma1)
    sig2 = ROOT.RooGaussian("sig2", "Signal component 2", x, mean, sigma2)

    # Sum the signal components into a composite signal p.d.f.
    sig1frac = ROOT.RooRealVar(
        "sig1frac", "fraction of component 1 in signal", 0.8, 0., 1.)
    sig = ROOT.RooAddPdf(
        "sig", "Signal", ROOT.RooArgList(sig1, sig2), ROOT.RooArgList(sig1frac))

    # Build Chebychev polynomial p.d.f.
    a0 = ROOT.RooRealVar("a0", "a0", 0.5, 0., 1.)
    a1 = ROOT.RooRealVar("a1", "a1", -0.2, 0., 1.)
    bkg1 = ROOT.RooChebychev("bkg1", "Background 1",
                             x, ROOT.RooArgList(a0, a1))

    # Build expontential pdf
    alpha = ROOT.RooRealVar("alpha", "alpha", -1)
    bkg2 = ROOT.RooExponential("bkg2", "Background 2", x, alpha)

    # Sum the background components into a composite background p.d.f.
    bkg1frac = ROOT.RooRealVar(
        "bkg1frac", "fraction of component 1 in background", 0.2, 0., 1.)
    bkg = ROOT.RooAddPdf(
        "bkg", "Signal", ROOT.RooArgList(bkg1, bkg2), ROOT.RooArgList(bkg1frac))

    # Sum the composite signal and background
    bkgfrac = ROOT.RooRealVar("bkgfrac", "fraction of background", 0.5, 0., 1.)
    model = ROOT.RooAddPdf(
        "model", "g1+g2+a", ROOT.RooArgList(bkg, sig), ROOT.RooArgList(bkgfrac))

    # P r i n t   c o m p o s i t e   t r e e   i n   A S C I I
    # -----------------------------------------------------------

    # Print tree to stdout
    model.Print("t")

    # Print tree to file
    model.printCompactTree("", "rf206_asciitree.txt")

    # D r a w   c o m p o s i t e   t r e e   g r a p h i c a l l y
    # -------------------------------------------------------------

    # Print GraphViz DOT file with representation of tree
    model.graphVizTree("rf206_model.dot")

    # Make graphic output file with one of the GraphViz tools
    # (freely available from www.graphviz.org)
    #
    # 'Top-to-bottom graph'
    # unix> dot -Tgif -o rf207_model_dot.gif rf207_model.dot
    #
    # 'Spring-model graph'
    # unix> fdp -Tgif -o rf207_model_fdp.gif rf207_model.dot


if __name__ == "__main__":
    rf206_treevistools()
