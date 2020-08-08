[asy]
size(0,300);
import flowchart;


block block2 = roundrectangle(Label("Feedback", blue), (0, 2), palegreen, blue);
block block3 = bevel(Label("Generator Network", blue), (-1, 1), lightblue, blue);
block block4 = bevel(Label("Discriminator Network", blue), (1, 1), paleblue, blue);
block end = roundrectangle(Label("Generated Data", blue), (0, 0), pink, blue);
block seed = diamond(Label("Seed", blue), (-2, 1), cyan, blue);


draw(block2);
draw(block3);
draw(block4);
draw(end);
draw(seed);

add(new void(picture pic, transform t)
{
    blockconnector operator -- = blockconnector(pic, t);
    seed -- Right -- Arrow -- block3;
    block2 -- Left -- Down -- Arrow -- block3;
    block4 -- Up -- Left -- Arrow -- block2;
    end -- Right -- Up -- Arrow -- block4;
    block3 -- Down -- Right -- Arrow -- end;
 });

 [/asy]
