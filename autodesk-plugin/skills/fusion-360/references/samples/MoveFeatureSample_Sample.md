# Move Feature API Sample

## Description

Demonstrates creating a new move feature.

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
        centerPoint = adsk.core.Point3D.create(15, 5, 0)
        sketchCircles.addByCenterRadius(centerPoint, 4)

        # Create a collection of entities for extrude
        profiles = adsk.core.ObjectCollection.create()
        profiles.add(sketch.profiles.item(0))
        profiles.add(sketch.profiles.item(1))

        # Create a cylinder with ExtrudeFeature using the profile above.
        extrudeFeats = features.extrudeFeatures
        extrudeFeature = extrudeFeats.addSimple(profiles,
                                                adsk.core.ValueInput.createByReal(2.0),
                                                adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Create a collection of entities for move
        bodies = adsk.core.ObjectCollection.create()
        bodies.add(extrudeFeature.bodies.item(0))

        # Create a transform to do move
        vector = adsk.core.Vector3D.create(0.0, 10.0, 0.0)
        transform = adsk.core.Matrix3D.create()
        transform.translation = vector

        # Create a move feature
        moveFeats = features.moveFeatures
        moveFeatureInput = moveFeats.createInput2(bodies)
        moveFeatureInput.defineAsFreeMove(transform)
        moveFeats.add(moveFeatureInput)
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
#include <Core/Geometry/Vector3D.h>
#include <Core/Geometry/Matrix3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/MoveFeatures.h>
#include <Fusion/Features/MoveFeature.h>
#include <Fusion/Features/MoveFeatureInput.h>
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
    Ptr<SketchCircles> sketchCircles = sketchCurves->sketchCircles();
    if (!sketchCircles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> sketchCircle = sketchCircles->addByCenterRadius(centerPoint, 10);
    if (!sketchCircle)
        return false;
    centerPoint = Point3D::create(15, 5, 0);
    if (!centerPoint)
        return false;
    sketchCircle = sketchCircles->addByCenterRadius(centerPoint, 4);
    if (!sketchCircle)
        return false;

    // Create a collection of entities for extrude
    Ptr<ObjectCollection> profiles = ObjectCollection::create();
    if (!profiles)
        return false;
    Ptr<Profiles> sketchProfiles = sketch->profiles();
    if (!sketchProfiles)
        return false;
    Ptr<Profile> sketchProfile = sketchProfiles->item(0);
    if (!sketchProfile)
        return false;
    profiles->add(sketchProfile);

    sketchProfile = sketchProfiles->item(1);
    if (!sketchProfile)
        return false;
    profiles->add(sketchProfile);

    // Create two cylinders with ExtrudeFeature using the profiles above.
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
        extrudeFeats->addSimple(profiles, distance, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);

    // Create a collection of entities for move
    Ptr<BRepBodies> brepBodies = extrudeFeature->bodies();
    if (!brepBodies)
        return false;
    Ptr<BRepBody> brepBody = brepBodies->item(0);
    if (!brepBody)
        return false;
    Ptr<ObjectCollection> entities1 = adsk::core::ObjectCollection::create();
    if (!entities1)
        return false;
    entities1->add(brepBody);

    // Create a transform to do move
    Ptr<Vector3D> vector = adsk::core::Vector3D::create(0.0, 10.0, 0.0);
    if (!vector)
        return false;
    Ptr<Matrix3D> transform = adsk::core::Matrix3D::create();
    if (!transform)
        return false;
    transform->translation(vector);

    // Create a move feature
    Ptr<MoveFeatures> moveFeats = features->moveFeatures();
    if (!moveFeats)
        return false;
    Ptr<MoveFeatureInput> moveFeatureInput = moveFeats->createInput2(entities1);
    if (!moveFeatureInput)
        return false;
    moveFeatureInput->defineAsFreeMove(transform);
    Ptr<MoveFeature> moveFeature = moveFeats->add(moveFeatureInput);
    if (!moveFeature)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |