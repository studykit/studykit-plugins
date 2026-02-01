# ReplaceFace Feature

## Description

Demonstrates creating a new replaceface feature.

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
        ui  = app.userInterface

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design.
        rootComp = design.rootComponent
        features = rootComp.features

        # Create sketch circle on the xz plane.
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 10)

        # Get the profile from the sketch.
        profile = sketch.profiles.item(0)

        # Create a cylinder with ExtrudeFeature using the profile above.
        extrudeFeats = features.extrudeFeatures
        distance = adsk.core.ValueInput.createByReal(2.5)
        extrudeFeature = extrudeFeats.addSimple(profile, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Create a collection of source faces for replace
        entities1 = adsk.core.ObjectCollection.create()
        sourceFace = extrudeFeature.endFaces.item(0)
        entities1.add(sourceFace)

        # Create a construction plane as the target face
        offset = adsk.core.ValueInput.createByReal(5)
        ctorPlanes = rootComp.constructionPlanes
        ctorPlaneInput = ctorPlanes.createInput()
        ctorPlaneInput.setByOffset(sourceFace, offset)
        ctorPlane = ctorPlanes.add(ctorPlaneInput)

        # Create a replace feature
        replaceFaceFeas = features.replaceFaceFeatures
        isTangentChain = False
        replaceFaceInput = replaceFaceFeas.createInput(entities1, isTangentChain, ctorPlane)
        replaceFaceFeas.add(replaceFaceInput)
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
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ReplaceFaceFeatures.h>
#include <Fusion/Features/ReplaceFaceFeature.h>
#include <Fusion/Features/ReplaceFaceFeatureInput.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchPoint.h>
#include <Fusion/Sketch/SketchPoints.h>

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
    Ptr<SketchCircle> sketchCircle = sketchCirles->addByCenterRadius(centerPoint, 10);
    if (!sketchCircle)
        return false;

    // Get the profile from the sketch.
    Ptr<Profiles> sketchProfiles = sketch->profiles();
    if (!sketchProfiles)
        return false;
    Ptr<Profile> profile = sketchProfiles->item(0);
    if (!profile)
        return false;

    // Create a cylinder with ExtrudeFeature using the profile above.
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;
    Ptr<ExtrudeFeatures> extrudeFeats = features->extrudeFeatures();
    if (!extrudeFeats)
        return false;
    Ptr<ValueInput> distance = adsk::core::ValueInput::createByReal(2.0);
    if (!distance)
        return false;
    Ptr<ExtrudeFeature> extrudeFeature =
        extrudeFeats->addSimple(profile, distance, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeFeature)
        return false;

    // Create a collection of source faces for replace
    Ptr<BRepFaces> brepFaces = extrudeFeature->endFaces();
    if (!brepFaces)
        return false;
    Ptr<BRepFace> sourceFace = brepFaces->item(0);
    if (!sourceFace)
        return false;
    Ptr<ObjectCollection> entities1 = adsk::core::ObjectCollection::create();
    if (!entities1)
        return false;
    entities1->add(sourceFace);

    // Create a construction plane as the target face
    Ptr<ValueInput> offset = adsk::core::ValueInput::createByReal(5);
    if (!offset)
        return false;
    Ptr<ConstructionPlanes> ctorPlanes = rootComp->constructionPlanes();
    if (!ctorPlanes)
        return false;
    Ptr<ConstructionPlaneInput> ctorPlaneInput = ctorPlanes->createInput();
    if (!ctorPlaneInput)
        return false;
    ctorPlaneInput->setByOffset(sourceFace, offset);
    Ptr<ConstructionPlane> ctorPlane = ctorPlanes->add(ctorPlaneInput);
    if (!ctorPlane)
        return false;

    // Create a replace feature
    Ptr<ReplaceFaceFeatures> replaceFaceFeats = features->replaceFaceFeatures();
    if (!replaceFaceFeats)
        return false;
    bool isTangentChain = false;
    Ptr<ValueInput> thickness = adsk::core::ValueInput::createByReal(0.5);
    if (!thickness)
        return false;
    Ptr<ReplaceFaceFeatureInput> replaceFaceFeatureInput =
        replaceFaceFeats->createInput(entities1, isTangentChain, ctorPlane);
    if (!replaceFaceFeatureInput)
        return false;
    Ptr<ReplaceFaceFeature> replaceFaceFeature = replaceFaceFeats->add(replaceFaceFeatureInput);
    if (!replaceFaceFeature)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |