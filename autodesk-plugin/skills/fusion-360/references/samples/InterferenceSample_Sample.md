# Interference API Sample

## Description

Demonstrates Interference APIs.

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
        design.designType = adsk.fusion.DesignTypes.DirectDesignType

        # Get the root component of the active design.
        rootComp = design.rootComponent
        features = rootComp.features

        # Create sketch circle on the xz plane.
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 10)

        # Create a collection of entities for extrude
        entities0 = adsk.core.ObjectCollection.create()
        entities0.add(sketch.profiles.item(0))

        # Create a cylinder with ExtrudeFeature using the profile above.
        extrudeFeats = features.extrudeFeatures
        extrudeFeatureInput = extrudeFeats.createInput(entities0, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeFeatureInput.isSolid = True
        extrudeFeatureInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(2.5))
        extrudeFeature = extrudeFeats.add(extrudeFeatureInput)

        # Create second body to do interference
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(5, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 10)

        entities0.clear()
        entities0.add(sketch.profiles.item(0))

        # Create a cylinder with ExtrudeFeature using the profile above.
        extrudeFeatureInput = extrudeFeats.createInput(entities0, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeFeatureInput.isSolid = True
        extrudeFeatureInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(2.5))
        extrudeFeature = extrudeFeats.add(extrudeFeatureInput)

        # Create a collection of bodies
        bodies = adsk.core.ObjectCollection.create()
        for body in rootComp.bRepBodies:
            bodies.add(body)

        # Create InterferenceInput
        input = design.createInterferenceInput(bodies)

        # Analyze interference
        results = design.analyzeInterference(input)

        # Create bodies
        results.createBodies(True)
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
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/InterferenceResult.h>
#include <Fusion/Fusion/InterferenceResults.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
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

    bool res = design->designType(DirectDesignType);
    if (!res)
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

    // Create a collection of entities for extrude
    Ptr<ObjectCollection> entities0 = ObjectCollection::create();
    if (!entities0)
        return false;
    Ptr<Profiles> sketchProfiles = sketch->profiles();
    if (!sketchProfiles)
        return false;
    Ptr<Profile> sketchProfile = sketchProfiles->item(0);
    if (!sketchProfile)
        return false;
    entities0->add(sketchProfile);

    // Create a cylinder with ExtrudeFeature using the profile above.
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;
    Ptr<ExtrudeFeatures> extrudeFeats = features->extrudeFeatures();
    if (!extrudeFeats)
        return false;
    Ptr<ExtrudeFeatureInput> extrudeFeatureInput =
        extrudeFeats->createInput(entities0, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeFeatureInput)
        return false;
    Ptr<ValueInput> distance = adsk::core::ValueInput::createByReal(2.0);
    if (!distance)
        return false;
    extrudeFeatureInput->isSolid(true);
    extrudeFeatureInput->setDistanceExtent(false, distance);
    Ptr<ExtrudeFeature> extrudeFeature = extrudeFeats->add(extrudeFeatureInput);
    if (!extrudeFeature)
        return false;

    // Create second body to do interference
    sketch = sketches->add(rootComp->xZConstructionPlane());
    if (!sketch)
        return false;
    sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    sketchCirles = sketchCurves->sketchCircles();
    if (!sketchCirles)
        return false;
    centerPoint = Point3D::create(5, 0, 0);
    if (!centerPoint)
        return false;
    sketchCircle = sketchCirles->addByCenterRadius(centerPoint, 10);
    if (!sketchCircle)
        return false;

    entities0->clear();
    sketchProfiles = sketch->profiles();
    if (!sketchProfiles)
        return false;
    sketchProfile = sketchProfiles->item(0);
    if (!sketchProfile)
        return false;
    entities0->add(sketchProfile);

    // Create a cylinder with ExtrudeFeature using the profile above.
    extrudeFeatureInput =
        extrudeFeats->createInput(entities0, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeFeatureInput)
        return false;
    distance = adsk::core::ValueInput::createByReal(2.0);
    if (!distance)
        return false;
    extrudeFeatureInput->isSolid(true);
    extrudeFeatureInput->setDistanceExtent(false, distance);
    extrudeFeature = extrudeFeats->add(extrudeFeatureInput);
    if (!extrudeFeature)
        return false;

    // Create a collection of bodies
    Ptr<ObjectCollection> bodies = adsk::core::ObjectCollection::create();
    if (!bodies)
        return false;
    Ptr<BRepBodies> brepBodies = rootComp->bRepBodies();
    if (!brepBodies)
        return false;
    for (auto body : brepBodies)
    {
        bodies->add(body);
    }

    // Create InterferenceInput
    Ptr<InterferenceInput> input = design->createInterferenceInput(bodies);
    if (!input)
        return false;

    // Analyze interference
    Ptr<InterferenceResults> results = design->analyzeInterference(input);
    if (!input)
        return false;

    // Create bodies
    results->createBodies(true);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |