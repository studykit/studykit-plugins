# Sweep Feature API Sample

## Description

Demonstrates creating a new sweep feature.

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

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, 3.0)

        # Get the profile defined by the circle.
        prof = sketch.profiles.item(0)

        # Create a vertical sketch and add two lines on it
        sketchVertical = sketches.add(rootComp.yZConstructionPlane)
        sketchLines = sketchVertical.sketchCurves.sketchLines
        startPt = adsk.core.Point3D.create(0, 0, 0)
        midPt = adsk.core.Point3D.create(0, 3, 0)
        endPt = adsk.core.Point3D.create(2, 6, 0)
        line1 = sketchLines.addByTwoPoints(startPt, midPt)
        line2 = sketchLines.addByTwoPoints(midPt, endPt)

        # Merge the two lines
        line1.endSketchPoint.merge(line2.startSketchPoint)

        # Create a path and let it find connected curves automatically
        path = rootComp.features.createPath(line1)

        # Create a sweep input
        sweeps = rootComp.features.sweepFeatures
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput.taperAngle = adsk.core.ValueInput.createByString('5 deg')
        sweepInput.twistAngle = adsk.core.ValueInput.createByString('10 deg')

        # Create the sweep.
        sweep = sweeps.add(sweepInput)

        # Get taperAngel and twistAngle from sweep feature
        taperAngle = sweep.taperAngle
        twistAngle = sweep.twistAngle
        print('taper angle: {}'.format(taperAngle.expression))
        print('twist angle: {}'.format(twistAngle.expression))
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Documents.h>
#include <Core/Application/Document.h>
#include <Core/Application/Product.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Line3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/Path.h>
#include <Fusion/Features/SweepFeature.h>
#include <Fusion/Features/SweepFeatures.h>
#include <Fusion/Features/SweepFeatureInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/ModelParameter.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Fusion/Sketch/SketchPoint.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
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

    // Create sketch
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;
    Ptr<ConstructionPlane> xz = rootComp->xZConstructionPlane();
    if (!xz)
        return false;
    Ptr<Sketch> sketch = sketches->add(xz);
    if (!sketch)
        return false;
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> sketchCircles = sketchCurves->sketchCircles();
    if (!sketchCircles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> circle = sketchCircles->addByCenterRadius(centerPoint, 3.0);
    if (!circle)
        return false;

    // Get the profile defined by the circle.
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);
    if (!prof)
        return false;

    // Create a vertical sketch and add two lines on it
    Ptr<ConstructionPlane> yz = rootComp->yZConstructionPlane();
    if (!yz)
        return false;
    Ptr<Sketch> sketchVertical = sketches->add(yz);
    if (!sketchVertical)
        return false;
    Ptr<SketchCurves> sketchCurvesVertical = sketchVertical->sketchCurves();
    if (!sketchCurvesVertical)
        return false;
    Ptr<SketchLines> sketchLines = sketchCurvesVertical->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<Point3D> startPt = Point3D::create(0, 0, 0);
    if (!startPt)
        return false;
    Ptr<Point3D> midPt = Point3D::create(0, 3, 0);
    if (!midPt)
        return false;
    Ptr<Point3D> endPt = Point3D::create(2, 6, 0);
    if (!endPt)
        return false;
    Ptr<SketchLine> line1 = sketchLines->addByTwoPoints(startPt, midPt);
    if (!line1)
        return false;
    Ptr<SketchLine> line2 = sketchLines->addByTwoPoints(midPt, endPt);
    if (!line2)
        return false;

    // Merge the two lines
    Ptr<SketchPoint> line1EndPt = line1->endSketchPoint();
    if (!line1EndPt)
        return false;
    Ptr<SketchPoint> line2StartPt = line2->startSketchPoint();
    if (!line2StartPt)
        return false;
    line1EndPt->merge(line2StartPt);

    // Create a path and let it find connected curves automatically
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;
    Ptr<Path> path = feats->createPath(line1);
    if (!path)
        return false;

    // Create a sweep input
    Ptr<SweepFeatures> sweeps = feats->sweepFeatures();
    if (!sweeps)
        return false;
    Ptr<SweepFeatureInput> sweepInput = sweeps->createInput(prof, path, FeatureOperations::NewBodyFeatureOperation);
    if (!sweepInput)
        return false;

    Ptr<ValueInput> taper = ValueInput::createByString("5.0 deg");
    Ptr<ValueInput> twist = ValueInput::createByString("10.0 deg");

    // Create the sweep.
    Ptr<SweepFeature> sweep = sweeps->add(sweepInput);
    if (!sweep)
        return false;

    // Get taperAngle and twistAngle from sweep feature
    Ptr<ModelParameter> taperParam = sweep->taperAngle();
    if (!taperParam)
        return false;

    Ptr<ModelParameter> twistParam = sweep->twistAngle();
    if (!twistParam)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |