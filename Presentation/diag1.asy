settings.render = 200;

unitsize(5cm);

draw((0, 0) -- (2, 0), arrow = ArcArrow(HookHead), red);
label("$T$", (2, 0), SE);

draw((0, 0) -- (0, 2), arrow = ArcArrow(HookHead), red);
label("$H$", (0, 2), NW);

label("$0$", (0,0), SW);
dot((0, 0));

real f(real x) 
{
	return 2.5-cosh(x);
}

path g = graph(f, 0, 1.5667, Hermite);
draw(g, blue);

dot((1.5667, 0));
label("$T_c$", (1.5667,0), S);

dot((0, 1.5));
label("$H_c(0)$", (0, 1.5), W);

label("$H_c (T)$", (0.928, 1.0376), NE);

label("Superconductor", (0.15, 0.15), NE);

label("Normal", (1.3, 1.3), NE);


[/asy]
