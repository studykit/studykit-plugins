# BaseFeature Sample

## Description

Creates a new base feature.

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
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a base feature
        baseFeats = rootComp.features.baseFeatures
        baseFeat = baseFeats.add()

        baseFeat.startEdit()

        # Create construction plane in base feature
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        planeInput.targetBaseOrFormFeature = baseFeat
        planeInput.setByOffset(rootComp.xYConstructionPlane, adsk.core.ValueInput.createByReal(1))
        plane = planes.add(planeInput)

        # Create sketch in base feature
        sketches = rootComp.sketches
        sketch = sketches.addToBaseOrFormFeature(plane, baseFeat, True)

        # Draw a circle.
        circles = sketch.sketchCurves.sketchCircles
        circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)

        # Get the profile defined by the circle.
        prof = sketch.profiles.item(0)

        # Create an extrusion input to be able to define the input needed for an extrusion
        # while specifying the profile and that a new component is to be created
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm.
        distance = adsk.core.ValueInput.createByReal(5)
        extInput.setDistanceExtent(False, distance)
        extInput.baseFeature = baseFeat

        # Create the extrusion.
        ext = extrudes.add(extInput)
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
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Features/BaseFeature.h>
#include <Fusion/Features/BaseFeatures.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>

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

    design->designType(ParametricDesignType);

    // Get the root component of the active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;

    // Create a base feature
    Ptr<BaseFeatures> baseFeats = feats->baseFeatures();
    if (!baseFeats)
        return false;

    Ptr<BaseFeature> baseFeat = baseFeats->add();
    if (!baseFeat)
        return false;

    baseFeat->startEdit();

    // Create construction plane in base feature
    Ptr<ConstructionPlanes> planes = rootComp->constructionPlanes();
    if (!planes)
        return false;
    Ptr<ConstructionPlaneInput> planeInput = planes->createInput();
    if (!planeInput)
        return false;
    planeInput->targetBaseOrFormFeature(baseFeat);
    planeInput->setByOffset(rootComp->xYConstructionPlane(), ValueInput::createByReal(1));
    Ptr<ConstructionPlane> plane = planes->add(planeInput);
    if (!plane)
        return false;

    // Create sketch in base feature
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;
    Ptr<ConstructionPlane> xyPlane = rootComp->xYConstructionPlane();
    if (!xyPlane)
        return false;
    Ptr<Sketch> sketch = sketches->addToBaseOrFormFeature(xyPlane, baseFeat, true);
    if (!sketch)
        return false;

    // Draw a circle.
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> circles = sketchCurves->sketchCircles();
    if (!circles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> circle1 = circles->addByCenterRadius(centerPoint, 2);
    if (!circle1)
        return false;

    // Get the profile defined by the circle.
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);
    if (!prof)
        return false;

    // Create an extrusion input to be able to define the input needed for an extrusion
    // while specifying the profile and that a new component is to be created
    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);
    if (!extInput)
        return false;

    // Define that the extent is a distance extent of 5 cm.
    Ptr<ValueInput> distance = ValueInput::createByReal(5);
    if (!distance)
        return false;
    extInput->setDistanceExtent(false, distance);
    extInput->targetBaseFeature(baseFeat);

    // Create the extrusion.
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |