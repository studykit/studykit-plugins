# API Sample that demonstrates creating sketch lines in various ways.

## Description

Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Draw two connected lines.
        lines = sketch.sketchCurves.sketchLines;
        line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(3, 1, 0))
        line2 = lines.addByTwoPoints(line1.endSketchPoint, adsk.core.Point3D.create(1, 4, 0))

        # Draw a rectangle by two points.
        recLines = lines.addTwoPointRectangle(adsk.core.Point3D.create(4, 0, 0), adsk.core.Point3D.create(7, 2, 0))

        # Use the returned lines to add some constraints.
        sketch.geometricConstraints.addHorizontal(recLines.item(0))
        sketch.geometricConstraints.addHorizontal(recLines.item(2))
        sketch.geometricConstraints.addVertical(recLines.item(1))
        sketch.geometricConstraints.addVertical(recLines.item(3))
        sketch.sketchDimensions.addDistanceDimension(recLines.item(0).startSketchPoint, recLines.item(0).endSketchPoint,
                                                     adsk.fusion.DimensionOrientations.HorizontalDimensionOrientation,
                                                     adsk.core.Point3D.create(5.5, -1, 0));

        # Draw a rectangle by three points.
        recLines = lines.addThreePointRectangle(adsk.core.Point3D.create(8, 0, 0), adsk.core.Point3D.create(11, 1, 0), adsk.core.Point3D.create(9, 3, 0))

        # Draw a rectangle by a center point.
        recLines = lines.addCenterPointRectangle(adsk.core.Point3D.create(14, 3, 0), adsk.core.Point3D.create(16, 4, 0))
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    Ptr<Documents> documents = app->documents();
    if (!documents)
        return false;

    Ptr<Document> doc = documents->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    // Get the root component of the active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create a new sketch on the xy plane.
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;
    Ptr<ConstructionPlane> xyPlane = rootComp->xYConstructionPlane();
    if (!xyPlane)
        return false;
    Ptr<Sketch> sketch = sketches->add(xyPlane);
    if (!sketch)
        return false;

    // Draw two connected lines.
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<SketchLine> line1 = sketchLines->addByTwoPoints(Point3D::create(0, 0, 0), Point3D::create(3, 1, 0));
    if (!line1)
        return false;
    Ptr<SketchLine> line2 = sketchLines->addByTwoPoints(line1->endSketchPoint(), Point3D::create(1, 4, 0));
    if (!line2)
        return false;

    // Draw a rectangle by two points.
    Ptr<SketchLineList> recLines =
        sketchLines->addTwoPointRectangle(Point3D::create(4, 0, 0), Point3D::create(7, 2, 0));
    if (!recLines)
        return false;

    // Use the returned lines to add some constraints.
    Ptr<GeometricConstraints> constraints = sketch->geometricConstraints();
    if (!constraints)
        return false;

    Ptr<HorizontalConstraint> HConstraint = constraints->addHorizontal(recLines->item(0));
    if (!HConstraint)
        return false;
    HConstraint = constraints->addHorizontal(recLines->item(2));
    if (!HConstraint)
        return false;

    Ptr<VerticalConstraint> VConstraint = constraints->addVertical(recLines->item(1));
    if (!VConstraint)
        return false;
    VConstraint = constraints->addVertical(recLines->item(3));
    if (!VConstraint)
        return false;

    Ptr<SketchDimensions> sketchDimensions = sketch->sketchDimensions();
    if (!sketchDimensions)
        return false;
    Ptr<SketchDimension> sketchDimension = sketchDimensions->addDistanceDimension(
        recLines->item(0)->startSketchPoint(),
        recLines->item(0)->endSketchPoint(),
        HorizontalDimensionOrientation,
        Point3D::create(5.5, -1, 0));
    if (!sketchDimension)
        return false;

    // Draw a rectangle by three points.
    recLines = sketchLines->addThreePointRectangle(
        Point3D::create(8, 0, 0), Point3D::create(11, 1, 0), Point3D::create(9, 3, 0));
    if (!recLines)
        return false;

    // Draw a rectangle by a center point.
    recLines = sketchLines->addCenterPointRectangle(Point3D::create(14, 3, 0), Point3D::create(16, 4, 0));
    if (!recLines)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |