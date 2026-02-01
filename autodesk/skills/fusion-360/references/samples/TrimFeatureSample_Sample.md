# Trim Feature API Sample

## Description

Demonstrates creating a new trim feature.

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
        sketchCircle = sketchCircles.addByCenterRadius(centerPoint, 3.0)

        # Create a open profile for extrusion.
        openProfile = rootComp.createOpenProfile(sketchCircle)

        # Create an extrusion input.
        features = rootComp.features
        extrudes = features.extrudeFeatures
        extrudeInput = extrudes.createInput(openProfile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeInput.isSolid = False

        # Define the extent with a distance extent of 3 cm.
        distance = adsk.core.ValueInput.createByReal(3.0)
        extrudeInput.setDistanceExtent(False, distance)

        # Create the extrusion.
        extrude = extrudes.add(extrudeInput)

        # Get the body created by extrusion
        body = extrude.bodies[0]

        # Create sketch 2.
        sketch2 = sketches.add(rootComp.xYConstructionPlane);
        sketchLines = sketch2.sketchCurves.sketchLines;
        startPoint = adsk.core.Point3D.create(-5, 0, 0);
        endPoint = adsk.core.Point3D.create(5, 0, 0);
        sketchLine = sketchLines.addByTwoPoints(startPoint, endPoint);
        openProfile2 = rootComp.createOpenProfile(sketchLine);

        # Create a open profile for extrusion.
        extrudeInput2 = extrudes.createInput(openProfile2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeInput2.isSolid = False

        # Define the extent
        distance2 = adsk.core.ValueInput.createByReal(5.0)
        extrudeInput2.setDistanceExtent(False, distance2)

        # Create the extrusion.
        extrudes.add(extrudeInput2)

        # Create trim feature
        trims = features.trimFeatures
        trimInput = trims.createInput(body)
        cells = trimInput.bRepCells
        cells[0].isSelected = True
        trims.add(trimInput)
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
#include <Core/Application/ObjectCollection.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/Features/BRepCells.h>
#include <Fusion/Features/BRepCell.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/TrimFeatures.h>
#include <Fusion/Features/TrimFeatureInput.h>
#include <Fusion/Features/TrimFeature.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>

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

    // Get the root component of the active design.
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create sketch circle on the xz plane.
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;
    Ptr<Sketch> sketch = sketches->add(rootComp->xZConstructionPlane());
    if (!sketch)
        return false;
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> sketchCirles = sketchCurves->sketchCircles();
    if (!sketchCirles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> sketchCircle = sketchCirles->addByCenterRadius(centerPoint, 3.0);
    if (!sketchCircle)
        return false;

    // Create a open profile for extrusion.
    Ptr<Profile> openProfile = rootComp->createOpenProfile(sketchCircle);

    // Create an extrusion input.
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;
    Ptr<ExtrudeFeatures> extrudes = features->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extrudeInput =
        extrudes->createInput(openProfile, FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeInput)
        return false;
    extrudeInput->isSolid(false);

    // Define the extent with a distance extent of 3 cm.
    Ptr<ValueInput> distance = ValueInput::createByReal(3.0);
    if (!distance)
        return false;
    extrudeInput->setDistanceExtent(false, distance);

    // Create the extrusion.
    Ptr<ExtrudeFeature> extrude = extrudes->add(extrudeInput);
    if (!extrude)
        return false;

    // Get the body created by extrusion.
    Ptr<BRepBodies> bodies = extrude->bodies();
    if (!bodies)
        return false;
    Ptr<BRepBody> body = bodies->item(0);

    // Create sketch 2.
    Ptr<Sketch> sketch2 = sketches->add(rootComp->xYConstructionPlane());
    if (!sketch2)
        return false;
    Ptr<SketchCurves> sketchCurves2 = sketch2->sketchCurves();
    if (!sketchCurves2)
        return false;
    Ptr<SketchLines> sketchLines = sketchCurves2->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<Point3D> startPoint = Point3D::create(-5.0, 0, 0);
    Ptr<Point3D> endPoint = Point3D::create(5.0, 0, 0);
    Ptr<SketchLine> sketchLine = sketchLines->addByTwoPoints(startPoint, endPoint);

    // Create a open profile.
    Ptr<Profile> openProfile2 = rootComp->createOpenProfile(sketchLine);

    // Create an extrusion input.
    Ptr<ExtrudeFeatureInput> extrudeInput2 =
        extrudes->createInput(openProfile2, FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeInput2)
        return false;
    extrudeInput2->isSolid(false);

    // Define the extent.
    Ptr<ValueInput> distance2 = ValueInput::createByReal(5.0);
    extrudeInput2->setDistanceExtent(false, distance2);

    // Create the extrusion.
    extrudes->add(extrudeInput2);

    // Create trim feature.
    Ptr<TrimFeatures> trims = features->trimFeatures();
    if (!trims)
        return false;
    Ptr<TrimFeatureInput> trimInput = trims->createInput(body);
    if (!trimInput)
        return false;
    Ptr<BRepCells> cells = trimInput->bRepCells();
    if (!cells)
        return false;
    Ptr<BRepCell> cell = cells->item(0);
    if (!cell)
        return false;
    cell->isSelected(true);
    trims->add(trimInput);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |