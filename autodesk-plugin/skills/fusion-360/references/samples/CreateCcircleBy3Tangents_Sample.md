# Create Circle By 3 Tangents API Sample

## Description

Creates three lines and then draws a circle that is tangent to the lines. It then creates tangent constraints to maintain that relationship.

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

        # Draw three lines.
        lines = sketch.sketchCurves.sketchLines;
        line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(3, 1, 0))
        line2 = lines.addByTwoPoints(adsk.core.Point3D.create(4, 3, 0), adsk.core.Point3D.create(2, 4, 0))
        line3 = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(0, 4, 0))

        # Draw circle tangent to the lines.
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByThreeTangents(line1, line2, line3, adsk.core.Point3D.create(0,0,0))

        # Apply tangent contstraints to maintain the relationship.
        constraints = sketch.geometricConstraints
        constraints.addTangent(circle1, line1)
        constraints.addTangent(circle1, line2)
        constraints.addTangent(circle1, line3)
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

    // Draw three lines.
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<SketchLine> line1 = sketchLines->addByTwoPoints(Point3D::create(0, 0, 0), Point3D::create(3, 1, 0));
    if (!line1)
        return false;
    Ptr<SketchLine> line2 = sketchLines->addByTwoPoints(Point3D::create(4, 3, 0), Point3D::create(2, 4, 0));
    if (!line2)
        return false;
    Ptr<SketchLine> line3 = sketchLines->addByTwoPoints(Point3D::create(-1, 0, 0), Point3D::create(0, 4, 0));
    if (!line3)
        return false;

    // Draw circle tangent to the lines.
    Ptr<SketchCircles> sketchCircles = sketchCurves->sketchCircles();
    if (!sketchCircles)
        return false;

    Ptr<SketchCircle> circle = sketchCircles->addByThreeTangents(line1, line2, line3, Point3D::create(0, 0, 0));
    if (!circle)
        return false;

    // Apply tangent contstraints to maintain the relationship.
    Ptr<GeometricConstraints> constraints = sketch->geometricConstraints();
    if (!constraints)
        return false;

    Ptr<TangentConstraint> constraint1 = constraints->addTangent(circle, line1);
    if (!constraint1)
        return false;

    Ptr<TangentConstraint> constraint2 = constraints->addTangent(circle, line2);
    if (!constraint2)
        return false;

    Ptr<TangentConstraint> constraint3 = constraints->addTangent(circle, line3);
    if (!constraint3)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |