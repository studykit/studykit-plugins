# BRep Body Sample

## Description

B-Rep (Boundary Representation) body related functions

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

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create a sketch
        sketches = rootComp.sketches
        sketch1 = sketches.add(rootComp.yZConstructionPlane)

        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines

        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5.0, 5.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)

        # Get the profile
        prof = sketch1.profiles.item(0)

        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(5.0)
        # Set the distance extent
        extInput.setDistanceExtent(False, distance)
        # Set the extrude type to be solid
        extInput.isSolid = True

        # Create the extrusion
        ext = extrudes.add(extInput)

        # Get the body with the extrude
        brepBody = ext.bodies.item(0)

        # Get the original revision id of the BRep Body
        print(brepBody.revisionId)

        # Set the light bulb besides the body node in the browser to off
        brepBody.isLightBulbOn = False

        # Get the revision id of the BRep Body after having the body's light bulb off
        print(brepBody.revisionId)

        # Verify if the light bulb is on or off
        print(brepBody.isLightBulbOn)

        # Verify if the body is visible or not
        print(brepBody.isVisible)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/Document.h>
#include <Core/Application/Documents.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Core/Geometry/Point3D.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>

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

    Ptr<Documents> docs = app->documents();
    if (!docs)
        return false;

    // Create a document.
    Ptr<Document> doc = docs->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Design> design = app->activeProduct();
    if (!design)
        return false;

    // Get the root component of the active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create a new sketch on the yz plane.
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;

    Ptr<ConstructionPlane> yzPlane = rootComp->yZConstructionPlane();
    if (!yzPlane)
        return false;

    Ptr<Sketch> yzSketch = sketches->add(yzPlane);
    if (!yzSketch)
        return false;

    // Create the spline.
    Ptr<SketchCurves> sketchCurves = yzSketch->sketchCurves();
    if (!sketchCurves)
        return false;

    // Get sketch lines
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;

    // Create sketch rectangle
    Ptr<Point3D> startPoint = Point3D::create(0, 0, 0);
    Ptr<Point3D> endPoint = Point3D::create(5.0, 5.0, 0);
    sketchLines->addTwoPointRectangle(startPoint, endPoint);

    // Get the profile
    Ptr<Profiles> profs = yzSketch->profiles();
    if (!profs)
        return false;

    Ptr<Profile> prof = profs->item(0);

    // Create an extrusion input
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;

    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;

    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);

    // Define that the extent is a distance extent of 5 cm
    Ptr<ValueInput> distance = ValueInput::createByReal(5.0);
    // Set the distance extent
    extInput->setDistanceExtent(false, distance);
    // Set the extrude type to be solid
    extInput->isSolid(true);

    // Create the extrusion
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    // Get the body with the extrude
    Ptr<BRepBodies> bodies = ext->bodies();
    if (!bodies)
        return false;

    Ptr<BRepBody> brepBody = bodies->item(0);

    std::string oldRevisionId = brepBody->revisionId();
    bool isVisibleFalse = brepBody->isLightBulbOn(false);
    std::string newRevisionId = brepBody->revisionId();

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |