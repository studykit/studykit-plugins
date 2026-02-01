# Sweep with guide rail Feature API Sample

## Description

Demonstrates creating a new Sweep feature that uses a guide rail along with a profile.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
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

    // Create sketch for the profile to sweep
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
    Ptr<SketchCircle> circle = sketchCircles->addByCenterRadius(centerPoint, 1.0);
    if (!circle)
        return false;

    // Get the profile defined by the circle.
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);
    if (!prof)
        return false;

    // Create a vertical sketch and add a spline (for the sweep path) and a line (for the sweep guide rail)
    Ptr<ConstructionPlane> yz = rootComp->yZConstructionPlane();
    if (!yz)
        return false;
    Ptr<Sketch> sketchVertical = sketches->add(yz);
    if (!sketchVertical)
        return false;
    Ptr<SketchCurves> sketchCurves2 = sketchVertical->sketchCurves();
    if (!sketchCurves2)
        return false;
    Ptr<SketchFittedSplines> sketchSplines = sketchCurves2->sketchFittedSplines();
    if (!sketchSplines)
        return false;
    Ptr<SketchLines> sketchLines = sketchCurves2->sketchLines();
    if (!sketchLines)
        return false;

    // Create points for the spline definition
    Ptr<Point3D> splineStartPt = Point3D::create(0, 0, 0);
    if (!splineStartPt)
        return false;
    Ptr<Point3D> splineMidPt = Point3D::create(0, 5, 0);
    if (!splineMidPt)
        return false;
    Ptr<Point3D> splineEndPt = Point3D::create(3, 10, 0);
    if (!splineEndPt)
        return false;

    // Create a collection of the points for the input needed to create the spline
    Ptr<ObjectCollection> fitPoints = ObjectCollection::create();
    if (!fitPoints)
        return false;
    fitPoints->add(splineStartPt);
    fitPoints->add(splineMidPt);
    fitPoints->add(splineEndPt);

    // Create the spline
    Ptr<SketchFittedSpline> spline = sketchSplines->add(fitPoints);
    if (!spline)
        return false;

    // Create points for the line definition
    Ptr<Point3D> lineStartPt = Point3D::create(-2, 0, 0);
    if (!lineStartPt)
        return false;
    Ptr<Point3D> lineEndPt = Point3D::create(-2, 10, 0);
    if (!lineEndPt)
        return false;

    // Create the line
    Ptr<SketchLine> line = sketchLines->addByTwoPoints(lineStartPt, lineEndPt);
    if (!line)
        return false;

    // Create a path for the sweep path and guide rail
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;
    Ptr<Path> path = feats->createPath(spline);
    if (!path)
        return false;
    Ptr<Path> guide = feats->createPath(line);
    if (!guide)
        return false;

    // Create a sweep input
    Ptr<SweepFeatures> sweeps = feats->sweepFeatures();
    if (!sweeps)
        return false;
    Ptr<SweepFeatureInput> sweepInput =
        sweeps->createInput(prof, path, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);
    if (!sweepInput)
        return false;
    sweepInput->guideRail(guide);

    sweepInput->profileScaling(adsk::fusion::SweepProfileScalingOptions::SweepProfileScaleOption);

    // Create the sweep.
    Ptr<SweepFeature> sweep = sweeps->add(sweepInput);
    if (!sweep)
        return false;

    sketchVertical->isVisible(true);
    return true;
}
```

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

        # Create sketch for the profile to sweep
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, 1.0)

        # Get the profile defined by the circle.
        prof = sketch.profiles.item(0)

        # Create a vertical sketch and add a spline (for the sweep path) and a line (for the sweep guide rail)
        sketchVertical = sketches.add(rootComp.yZConstructionPlane)
        sketchSplines = sketchVertical.sketchCurves.sketchFittedSplines
        sketchLines = sketchVertical.sketchCurves.sketchLines

        # Create points for the spline definition
        splineStartPt = adsk.core.Point3D.create(0, 0, 0)
        splineMidPt = adsk.core.Point3D.create(0, 5, 0)
        splineEndPt = adsk.core.Point3D.create(3, 10, 0)

        # Create a collection of the points for the input needed to create the spline
        fitPoints = adsk.core.ObjectCollection.create()
        fitPoints.add(splineStartPt)
        fitPoints.add(splineMidPt)
        fitPoints.add(splineEndPt)

        # Create the spline
        spline = sketchSplines.add(fitPoints)

        # Create points for the line definition
        lineStartPt = adsk.core.Point3D.create(-2, 0, 0)
        lineEndPt = adsk.core.Point3D.create(-2, 10, 0)

        # Create the line
        line = sketchLines.addByTwoPoints(lineStartPt, lineEndPt)

        # Create a path for the sweep path and guide rail
        path = rootComp.features.createPath(spline)
        guide = rootComp.features.createPath(line)

        # Create a sweep input
        sweeps = rootComp.features.sweepFeatures
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput.guideRail = guide
        sweepInput.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption

        # Create the sweep.
        sweep = sweeps.add(sweepInput)

        sketchVertical.isVisible = True

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |